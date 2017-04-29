# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:22:53 2016

@author: JosephNelson
"""

# make a request
import requests
r = requests.get('http://www.abrahamlincolnonline.org/lincoln/speeches/quotes.htm')

# verify the success
r.status_code

# parse the HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text)

# print it out
quotes = soup.find_all(name='p')

for quote in quotes:
    print quote.find(name='b')
