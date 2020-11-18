from bs4 import BeautifulSoup

import requests

from fake_useragent import UserAgent

import selenium

from selenium import webdriver

from nltk.tokenize import sent_tokenize


ua={"UserAgent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

url = "https://www.thehindu.com/news/cities/kolkata/soumitra-chatterjees-condition-deteriorates-to-very-critical-doctors/article32940359.ece"

res = requests.get(url , headers=ua)

soup = BeautifulSoup(res.content , features='lxml')

data = soup.findAll('p')
para = data[0].get_text()

data = sent_tokenize(para)
print(len(data))
print(data)
text = open("kunal.txt",'w')

for i in data:
    # print(i)
    text.write(i)
    text.write("\n")
