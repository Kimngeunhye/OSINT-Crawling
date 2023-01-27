import time from urllib.parse 
import quote_plus from urllib.request
import urlopen 
import pymongo 
import requests from bs4 
import BeautifulSoup from pymongo
import MongoClient from selenium 
import webdriver

#string에서 이름, 비번 번호는 중괄호까지 빼주고 넣어주기, 간혹 비번에 특수문자가 포함되면 에러가 나기도 함.
connection = pymongo.MongoClient("mongodb+srv://{name}:{password}@cluster0.qnxnj.mongodb.net/?retryWrites=true&w=majority")
connection = MongoClient('localhost', {port}) 
db = connection.dbsparta 
baseUrl = 'https://www.google.com/search?q=' 
plusUrl = input('Enter the search word:') 
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome(executable_path= r'{driver path}')

driver.get(url)

html = driver.page_source 
soup = BeautifulSoup(html)

v = soup.select('.yuRUbf') #Stroe the crawling data

for i in v: 
    Title = i.select_one('.LC20lb.DKV0Md').text
    URL = i.a.attrs['href'] 
    print()
    print(Title, URL)

doc = {
    'Title':Title,
    'URL' : URL
}

db.{db name}.insert_one(doc)
driver.close()