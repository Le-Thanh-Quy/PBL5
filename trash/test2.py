from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Edge('C:\Windows\msedgedriver.exe')
driver.get("https://oto.com.vn/mua-ban-xe-cu-da-qua-su-dung/p0")

page_source = BeautifulSoup(driver.page_source, 'html.parser')
data = page_source.select('.item-car > .photo > a')

# print(data[0]['href'])
driver.get("https://oto.com.vn/" + data[0]['href'])
sleep(1)

page_source = BeautifulSoup(driver.page_source, 'html.parser')
data = page_source.select('.group-title-detail > .title-detail')
dataDetails = page_source.select('.box-info-detail > .list-info > li')
InforCols = ['Năm sản xuất', 'Kiểu dáng', 'Tình trạng', 'Xuất xứ', 'Số km đã đi', 'Tỉnh thành', 'Hộp số', 'Nhiên liệu']
for dataDetail in dataDetails:
    print(dataDetail.get_text())