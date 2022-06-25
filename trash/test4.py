from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import warnings
import threading
import urllib.request
warnings.filterwarnings('ignore')

def getBaiViet(urlBaiViet, indexAnh):
    driver.get(urlBaiViet)
    baiviet = [urlBaiViet]
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    tieude = page_source.select('.detail-title')
    baiviet.append(tieude[0].getText().strip())

    anh = page_source.select('figure > img')
    try:
        urlanh = anh[0].get('src')
    except:
        urlanh = 'None'
    
    # pathAnh = f'media//blog_banner//thegioi1_{indexAnh}.jpg'
    pathAnh = f'media//blog_banner//GiaoDuc1_{indexAnh}.jpg'
    print(pathAnh)
    try:
        urllib.request.urlretrieve(urlanh, pathAnh)
    except:
        urllib.request.urlretrieve('https://uploads-eu-west-1.insided.com/ovo-boost-en/attachment/56cc8c77-d6bc-4728-bd06-524127763d88_thumb.png', pathAnh)
    
    baiviet.append(pathAnh.replace(".jpg", ''))
    noidung = page_source.select('.contents > div > p')
    noidungchinh = ''
    tomtat = page_source.select('.sapo')
    noidungchinh += tomtat[0].getText().strip() + '\n'
    for i in noidung:
        noidungchinh += i.getText().strip() + '\n'
    baiviet.append(noidungchinh)
    return baiviet

driver = webdriver.Edge('C:\Windows\msedgedriver.exe')
# driver.get("https://baotintuc.vn/the-gioi-130ct0/trang-1.htm")
# driver.get("https://baotintuc.vn/phap-luat-475ct0/trang-2.htm")
driver.get("https://baotintuc.vn/giao-duc-135ct0.htm")
database = []
links = []
page_source = BeautifulSoup(driver.page_source, 'html.parser')
data = page_source.select('.list-newsest > .item > a')

for i in data:
    links.append(i['href'])
sleep(1)

stt = 0

for i in links:
    url = 'https://baotintuc.vn/' + i
    try:
        baiviet = getBaiViet(url, stt)
        database.append(baiviet)
        stt += 1
    except:
        pass
    
     
KetQua = pd.DataFrame(database, columns= ['url', 'title', 'image', 'content'])
print(KetQua)
# KetQua.to_csv('TheGioi.csv')
KetQua.to_csv('GiaoDuc.csv')