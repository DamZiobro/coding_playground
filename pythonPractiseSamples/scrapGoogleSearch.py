#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import requests
import time
from bs4 import BeautifulSoup
import multiprocessing
 
 
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'en-GB;en;q=0.8',
    'Referrer':'https://www.google.com',
    'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml,q=0.8,image/webp,*/*,q=0.8',
}
 
 
def get_results(search_term, number_results, language_code):
    escaped_search_term = search_term.replace(' ', '+')
 
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=HEADERS)
    response.raise_for_status()
 
    return search_term, response.text

def parse_results(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')

    found_results = []
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:

        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        if link and title:
            link = link['href']
            if link != '#':
                found_results.append(link)
    return found_results

def scrap_google(search_term, number_results, language_code):
    try:
        keyword, html = get_results(search_term, number_results, language_code)
        results = parse_results(html, keyword)
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")

def scrap_keyword(keyword):
    return scrap_google(keyword, 30, "en");

if __name__ == '__main__':

    keywords = ['damian ziobro', 'football', 'test', 'python', 'story', 'london', 'paris', 'rome']

    cpus = multiprocessing.cpu_count()/2;
    results = []
    if cpus == 1:
        for keyword in keywords:
            results += scrap_keyword(keyword)
    else:
        pool = multiprocessing.Pool(cpus)
        results = pool.map(scrap_keyword, keywords)
        #results = pool.imap_unordered(scrap_keyword, keywords)

    for urls in results:
        for url in urls:
            print "url: {}".format(url)
