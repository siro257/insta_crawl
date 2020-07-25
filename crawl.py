from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

base_url = 'https://www.instagram.com/'
plus_url = input('Enter the username that you wish to crawl: ')

url = base_url + quote_plus(plus_url)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')

if not os.path.exists('img'):
    os.makedirs('img')

n = 1
for i in insta:
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + plus_url +'_'+ str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    driver.execute_script('window.scrollTo(0,1200)')

driver.close()