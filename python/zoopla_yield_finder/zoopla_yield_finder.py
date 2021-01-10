#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.


"""

"""

import json
import logging
import os
import re
from enum import Enum
from json import JSONDecodeError

import requests

logging.basicConfig(level="INFO")
logger = logging.getLogger("zoopla_api_client")

class Success(Enum):
    SUCCESS = 0

class Errors(Enum):
    ZOOPLA_API_KEY_NOT_SET = 0

def lambda_handler(event, context):

    base_url = "http://api.zoopla.co.uk/api/v1/property_listings.js"

    api_key = os.environ.get("ZOOPLA_API_KEY")
    if not api_key:
        logging.error("ZOOPLA_API_KEY not set. Please export ZOOPLA_API_KEY env var.")
        return Errors.ZOOPLA_API_KEY_NOT_SET

    keywords = ["yield", "return"]

    for keyword in keywords:
        query_params = {
            "area" : os.environ.get("REGION", "West Yorkshire"),
            "api_key" : api_key,
            "order_by" : "price",
            "listing_status": "sale",
            "keywords": keyword,
            "page_size": 100,
            "page_number": 1,
        }

        page_size = 1
        number_of_props = 0
        number_of_props_with_keyword = 0
        page_number = 1

        #get property_list using pagination
        while page_size > 0:
            resp = requests.get(
                url=base_url,
                params=query_params
            )

            try:
                property_list_prettyprint = json.dumps(resp.json(), indent=4, sort_keys=True)
            except JSONDecodeError:
                logger.error(f"non-json response: {resp.content}")
                return 100
            property_list = resp.json().get("listing")
            page_size = len(property_list)
            if page_size:
                logger.debug(f"{property_list_prettyprint}")
                for prop in property_list:
                    desc = prop.get('description')
                    if keyword in desc:
                        before_keyword, keyword, after_keyword = prop.get('description').partition(keyword)
                        before_keyword = before_keyword.split(' ')[-5:]
                        after_keyword = after_keyword.split(' ')[:5]
                        around_keyword_string = " ".join(before_keyword) + keyword + " ".join(after_keyword)
                        #logger.info(f"Description: {prop.get('description')}")
                        yield_value = None
                        if "%" in around_keyword_string:
                            yield_search = re.search(r"(?P<yield_value>\d+\.?\d{0,2})%", around_keyword_string)
                            if yield_search:
                                yield_value = float(yield_search.group("yield_value"))

                            if yield_value and yield_value > int(os.environ.get("YIELD_MIN", 10)):
                                logger.info(f"URL     : {prop.get('details_url')}")
                                logger.info(f"price   : {prop.get('price')}")
                                logger.info(f"yield:  {yield_value}%")
                                logger.info("===============================================")
                                number_of_props_with_keyword += 1

            page_number += 1
            number_of_props += page_size
            query_params["page_number"] = page_number

        logger.info(f"number of properties found: {number_of_props}")
        logger.info(f"number of properties with yield or return found: {number_of_props_with_keyword}")

    return  Success.SUCCESS

if __name__ == "__main__":
    ret = lambda_handler(None, None)
    logging.info(f"lambda_handler return: {ret}")
