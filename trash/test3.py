from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Edge('C:\Windows\msedgedriver.exe')
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=samsung&_sacat=15032&LH_TitleDesc=1&_pgn=1")

page_source = BeautifulSoup(driver.page_source, 'html.parser')
data = page_source.select('.s-item__image-section > .s-item__image > a')
print(len(data))
print(data[1]['href'])
# sleep(1)
driver.get(data[1]['href'])
# # sleep(1)

page_source = BeautifulSoup(driver.page_source, 'html.parser')
# data = page_source.select('.group-title-detail > .title-detail')
dataDetails = page_source.select('.ux-labels-values__values-content > div > .ux-textspans')
# i = 0
for i in range(38, 58):
    print(dataDetails[i].getText())
# print(len(dataDetails))