#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import pytest
 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# Constants
 
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'
 
# Scenarios
 
scenarios('../features/duckduckgo.feature')

# Fixtures
 
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()
 
# Given Steps
 
@given('the DuckDuckGo home page is displayed')
def test_ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)
 
# When Steps
 
@when(parsers.parse('the user searches for "{phrase}"'))
def test_search_phrase(browser, phrase):
    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(phrase + Keys.RETURN)
 
# Then Steps
 
@then(parsers.parse('results are shown for "{phrase}"'))
def test_search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase

