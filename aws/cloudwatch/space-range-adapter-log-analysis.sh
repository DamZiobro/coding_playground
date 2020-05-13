#! /bin/bash
#
# space-range-adapter-log-analysis.sh
# Copyright (C) 2020 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.
#

if [[ "$#" != 1 && "$#" != 2 ]]; then
  echo "ERROR: wrong arguments"
  echo "USAGE: $0 number_of_log_streams [mode ex. DAYONE]"
  exit 1 
fi

NUMBER_OF_STREAMS=$1
MODE=$2

ENDTIME_FILE=/tmp/endtimes
PUT_PRODUCT_PLACEMENT_FILE=/tmp/putProductPlacements
GET_PRODUCT_PLACEMENT_FILE=/tmp/getProductPlacements
PUT_SITE_RANGE_FILE=/tmp/putSiteRange
GET_SPACE_LOCATION_FILE=/tmp/getSpaceLocations

#echo -e "GETTING BATCH PROCESSING END TIMES"
#aws_get_log_events.py spaceadapter-prod --log-streams-number $NUMBER_OF_STREAMS --filter " END $MODE FUNCTIONALITY" --is_print yes > $ENDTIME_FILE &

#echo -e "GETTING PUTs PRODUCT PLACEMENTS"
#aws_get_log_events.py spaceadapter-prod --log-streams-number $NUMBER_OF_STREAMS --filter "put To ProductPlacement response location status" --is_print yes > $PUT_PRODUCT_PLACEMENT_FILE &

#echo -e "GETTING GETs PRODUCT PLACEMENTS"
#aws_get_log_events.py spaceadapter-prod --log-streams-number $NUMBER_OF_STREAMS --filter "OSP get product placement location status" --is_print yes > $GET_PRODUCT_PLACEMENT_FILE &

#echo -e "GETTING PUTs SITE RANGE"
#aws_get_log_events.py spaceadapter-prod --log-streams-number $NUMBER_OF_STREAMS --filter "putToSiteRange retailerSiteId status" --is_print yes > $PUT_SITE_RANGE_FILE &

#echo -e "GETTING GETs SPACE LOCATION"
#aws_get_log_events.py spaceadapter-prod --log-streams-number $NUMBER_OF_STREAMS --filter "callGetSpaceAPI location status" --is_print yes > $GET_SPACE_LOCATION_FILE &

#echo -e "waiting for logs getting to finish..."
#wait

column -t $ENDTIME_FILE > $ENDTIME_FILE.bkp && mv $ENDTIME_FILE.bkp $ENDTIME_FILE &
column -t $PUT_PRODUCT_PLACEMENT_FILE > $PUT_PRODUCT_PLACEMENT_FILE.bkp && mv $PUT_PRODUCT_PLACEMENT_FILE.bkp $PUT_PRODUCT_PLACEMENT_FILE &
column -t $GET_PRODUCT_PLACEMENT_FILE > $GET_PRODUCT_PLACEMENT_FILE.bkp && mv $GET_PRODUCT_PLACEMENT_FILE.bkp $GET_PRODUCT_PLACEMENT_FILE &
column -t $PUT_SITE_RANGE_FILE > $PUT_SITE_RANGE_FILE.bkp && mv $PUT_SITE_RANGE_FILE.bkp $PUT_SITE_RANGE_FILE &
column -t $GET_SPACE_LOCATION_FILE > $GET_SPACE_LOCATION_FILE.bkp && mv $GET_SPACE_LOCATION_FILE.bkp $GET_SPACE_LOCATION_FILE &

echo -e "converting files to column,based form..."
wait

sort -k15n -k19n $PUT_PRODUCT_PLACEMENT_FILE > $PUT_PRODUCT_PLACEMENT_FILE.bkp && mv $PUT_PRODUCT_PLACEMENT_FILE.bkp $PUT_PRODUCT_PLACEMENT_FILE

echo -e "======================================"
echo -e "BATCH PROCESSING END TIMES"
cat $ENDTIME_FILE

echo -e "======================================"
echo -e "PUT product placements"
NUMBER_OF_PUT_PRODUCT_PLACEMENTS=$(cat $PUT_PRODUCT_PLACEMENT_FILE | wc -l)
echo -e "NUMBER_OF_PUT_PRODUCT_PLACEMENTS: $NUMBER_OF_PUT_PRODUCT_PLACEMENTS"

echo -e "======================================"
echo -e "GET product placements"
NUMBER_OF_GET_PRODUCT_PLACEMENTS=$(cat $GET_PRODUCT_PLACEMENT_FILE | wc -l)
echo -e "NUMBER_OF_GET_PRODUCT_PLACEMENTS: $NUMBER_OF_GET_PRODUCT_PLACEMENTS"

echo -e "======================================"
echo -e "PUT site range"
NUMBER_OF_PUT_SITE_RANGE=$(cat $PUT_SITE_RANGE_FILE | wc -l)
echo -e "NUMBER_OF_PUT_SITE_RANGE: $NUMBER_OF_PUT_SITE_RANGE"

echo -e "======================================"
echo -e "GET Space Location"
NUMBER_OF_GET_SPACE_LOCATION=$(cat $GET_SPACE_LOCATION_FILE | wc -l)
echo -e "NUMBER_OF_GET_SPACE_LOCATION: $NUMBER_OF_GET_SPACE_LOCATION"
