from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def getBaiViet(urlBaiViet):
    driver.get(urlBaiViet)
    baiviet = [urlBaiViet]
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    tieude = page_source.select('.detail-title')
    baiviet.append(tieude[0].getText().strip())
    tomtat = page_source.select('.sapo')
    baiviet.append(tomtat[0].getText().strip())

    anh = page_source.select('figure > img')
    urlanh = anh[0].get('src')
    baiviet.append(urlanh.strip())
    noidung = page_source.select('.contents > div > p')
    for i in noidung:
        baiviet.append(i.getText().strip())
    return baiviet

driver = webdriver.Edge('C:\Windows\msedgedriver.exe')
driver.get("https://baotintuc.vn/the-gioi-130ct0/trang-3.htm")
database = []
links = []
page_source = BeautifulSoup(driver.page_source, 'html.parser')
data = page_source.select('.list-newsest > .item > a')

for i in data:
    links.append(i['href'])
sleep(1)

for i in links:
    url = 'https://baotintuc.vn/' + i
    baiviet = getBaiViet(url)
    database.append(baiviet)

KetQua = pd.DataFrame(database)
print(KetQua)
KetQua.to_csv('out.csv')