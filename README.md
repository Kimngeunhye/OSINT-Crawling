# OSINT-Crawling
import time
from urllib.parse import quote_plus
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('Enter the search word:')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome(executable_path= r'{enter the your chrome driver path}')
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

v = soup.select('.yuRUbf')

for i in v:
    print(i.select_one('.LC20lb.DKV0Md').text)
    print(i.a.attrs['href'])
    print()

driver.close()
