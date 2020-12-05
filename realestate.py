from selenium import webdriver
 
url = "https://www.daum.net/"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")

browser = webdriver.Chrome("./chromedriver", options=options)
browser.maximize_window

browser.get(url)
search = browser.find_element_by_id('q')
search.click()
search.send_keys('송파 헬리오시티')
search_btn = browser.find_element_by_class_name('btn_search')
search_btn.click()

import requests
from bs4 import BeautifulSoup 

soup = BeautifulSoup(browser.page_source, 'html.parser')

# with open('house.html','w',encoding="utf8")as f:
#     f.write(soup.prettify())

#lists = soup.find_all('tr')

# count = 0

# for index, item in enumerate(lists[1:5]):
#     거래 = item.find('td', class_='col1').text
#     공급 = item.find('td', class_='col2').text
#     매물가 = item.find('td', class_='col3').text
#     동 = item.find('td', class_='col4').text
#     층 = item.find('td', class_='col5').text
#     count = count + 1
#     print(f'======매물{count}=====')
#     print(f'거래:{거래}', f'공급/전용면적:{공급}', f'매물가(만원):{매물가}', f'동:{동}', f'층:{층}')


data_rows = soup.find('tbody').find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")
    print("=====매물{}=====".format(index+1))
    print("거래 :", columns[0].text.strip())
    print("면적 :", columns[1].text.strip(), "(공급/전용)")
    print("가격 :", columns[2].text.strip(), "(만원)")
    print("동 :", columns[3].text.strip())
    print("층 :", columns[4].text.strip())