#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

import os
import sys
import logging
import concurrent.futures
import pandas
import csv
from aws_get_log_events import get_log_events
import time

logging.basicConfig(level=logging.INFO)

current_milli_time = lambda: int(round(time.time() * 1000))
LOG_GROUP="spaceadapter-prod"


class LogFilter(object):
    def __init__(self, name, filter, location_column_nr=None, second_value_column=None, regex=""):
        self.name = name
        self.filter = filter
        self.location_column_nr = location_column_nr
        self.second_value_column = second_value_column
        self.filename = None
        self.filename_csv = None
        self.regex = regex
        self.pdseries = None

    def __str__(self):
        return self.name

    def concatenate_files(self, input_files, output_file):
        logging.debug(f"concatenate_files(): input_files: {input_files}, output_file: '{output_file}'")
        with open(output_file, 'w') as outfile:
            for fname in input_files:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)

    def convert_txt_to_csv(self, input_file, output_file):
        logging.debug(f"convert_txt_to_csv(): input_file: {input_file}, output_file: '{output_file}'")
        with open(input_file, 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.replace(",", "").split(" ") for line in stripped if line)
            with open(output_file, 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(lines)


    def get_filtered_logs(self, start_log_streams_number, end_log_streams_number, day):
        logging.debug(f"get_filtered_logs(): key: {self.name}, filter: '{self.filter}'")

        #cur_time = current_milli_time()
        filename_prefix = f"{self.name}-"
        if day == None:
            logs = get_log_events(
                log_group=LOG_GROUP,
                start_log_streams_number=start_log_streams_number,
                end_log_streams_number=end_log_streams_number,
                filter=self.filter,
                filename_prefix=filename_prefix,
                regex=self.regex,
            )
        else:
            start_time = day + " 00:00:00"
            end_time = day + " 23:59:59"
            logs = get_log_events(
                log_group=LOG_GROUP,
                start_time=start_time,
                end_time=end_time,
                filter=self.filter,
                filename_prefix=filename_prefix,
                regex=self.regex,
            )

        #convert file to csv
        self.filename = f"/tmp/{self.name}"
        self.concatenate_files(logs, self.filename)

        self.filename_csv = f"{self.filename}.csv"
        self.convert_txt_to_csv(self.filename, self.filename_csv)

        return self

    def process_csv(self):
        self._get_aggregated_stats()

    def _get_aggregated_stats(self):
        if self.location_column_nr and self.second_value_column:
            data = pandas.read_csv(self.filename_csv, 
                                   header=None, 
                                   usecols=[self.location_column_nr, self.second_value_column],
                                   names=['location', 'status'],
                                   dtype={'location':'int32','status':'str'},
                                  )
            self.pdseries = data
            column_name = self.name.replace(f"{LOG_GROUP}-", "")
            if column_name == f"nr-of-items-per-store":
                self.pdseries.columns = ['location', column_name]
                self.pdseries['status'] = "200"
                self.pdseries[column_name] = self.pdseries[column_name].apply(lambda x: x.split("/")[1])
                self.pdseries = data.groupby(['location', 'status']).nth(0)
                #print(self.pdseries)
            else:
                #print(f"file: {self.filename}; filter: '{self.filter}'")
                self.pdseries = data.groupby(['location', 'status']).size()
                self.pdseries = self.pdseries.rename(column_name)
                #print(self.pdseries)
        else:
            with open(self.filename, "r") as file:
                print(file.read())



    #destructor
    #def __del__(self):
        #logging.debug(f"cleaning files: {self.filename} and {self.filename_csv}")
        #for file in [self.filename, self.filename_csv]:
            #if file and os.path.exists(file):
                #os.remove(file)

filters = [
    LogFilter(
        name=f"{LOG_GROUP}-process-times",
        filter="END FUNCTIONALITY"
    ),
    LogFilter(
        name=f"{LOG_GROUP}-nr-of-items-per-store",
        filter="items progress 1",
        regex=".*items progress\: 1\/.*",
        location_column_nr=9,
        second_value_column=18
    ),
    LogFilter(
        name=f"{LOG_GROUP}-putProductPlacements", 
        filter="put To ProductPlacement response location status",
        location_column_nr=13,
        second_value_column=17,
    ),
    LogFilter(
        name=f"{LOG_GROUP}-getProductPlacements",
        filter="OSP get product placement location status",
        location_column_nr=11,
        second_value_column=16,
    ),
    LogFilter(
        name=f"{LOG_GROUP}-getSpaceLocations",
        filter="callGetSpaceAPI location status",
        location_column_nr=12,
        second_value_column=16,
    ),
    LogFilter(
        name=f"{LOG_GROUP}-putSiteRange",
        filter="putToSiteRange retailerSiteId status",
        location_column_nr=12,
        second_value_column=14,
    ),
]

if __name__ == "__main__":    
    
    if (len(sys.argv) != 2 and len(sys.argv) != 3):
        print("ERROR: wrong arguments")
        print("Usage: space-range-adapter-log-analysis.sh NUMBER_OF_LOG_STREAMS")
        print("Usage: space-range-adapter-log-analysis.sh 8")
        print("Usage: space-range-adapter-log-analysis.sh 8-16")
        print("Usage: space-range-adapter-log-analysis.sh --day '2020-05-11'")
        sys.exit(1)

    day = None
    start_log_streams_number = 1
    end_log_streams_number = 2
    if (len(sys.argv) == 3 and sys.argv[1] == "--day"):
        day = sys.argv[2]
    else:
        log_streams_number = sys.argv[1]
        if len(log_streams_number.split("-")) == 2:
            start_log_streams_number = int(log_streams_number.split("-")[0])
            end_log_streams_number = int(log_streams_number.split("-")[1])
        else:
            end_log_streams_number = int(log_streams_number)


    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        try:
            stream_futures = {executor.submit(filter.get_filtered_logs, start_log_streams_number, end_log_streams_number, day): filter for filter in filters}
        except Exception as ex:
            logging.error(f"exception: {ex}")

        for future in concurrent.futures.as_completed(stream_futures):
            stream = stream_futures[future]
            filter = future.result()
            logging.debug(f"finished getting logs from stream: {filter}")
            filter.process_csv()
            results.append(filter)

        final_dataframe = None
        for filter in filters:
            if filter.pdseries is not None:
                if final_dataframe is None:
                    final_dataframe = filter.pdseries
                else:
                    final_dataframe = pandas.merge(final_dataframe, filter.pdseries, on=["location", "status"], how="outer")

        print("==================================================")
        final_dataframe = final_dataframe.fillna(0)
        final_dataframe = final_dataframe.astype("int32")
        final_dataframe = final_dataframe.sort_values(['location', 'status'])
        final_dataframe.loc['Total'] = final_dataframe.sum(numeric_only=True, axis=0)
        #list_name= ["putProductPlacements","getProductPlacements", "getSpaceLocations","putSiteRange"]
        #final_dataframe['total']=final_dataframe.loc[:,list_name].sum(axis=1)
        final_dataframe.to_csv("/tmp/space-range-adapter-analysis.csv")
        print(final_dataframe.to_string())

