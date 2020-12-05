from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
browser = webdriver.Chrome("./chromedriver", options=options)
browser.maximize_window()

# 페이지 이동
URL = "https://play.google.com/store/movies/top"
browser.get(URL)

# 지정한 위치로scroll 내리기 
# browser.execute_script("window.scrollTo(0,1080)") #모니터(해상도)높이인 1080으로
# browser.execute_script("window.scrollTo(0,2080)")

# 화면 가장 아래로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval = 1 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print('스크롤 완료')

 
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'html.parser')

movies = soup.find_all('div', class_="Vpfmgd")
print("len:", len(movies))

for movie in movies:
    title = movie.find('div', class_="WsMG1c nnK0zc").text
    
    # 할인 전 가격
    original_price = movie.find("span", class_="SUZt4c djCuy")
    if original_price:
        original_price = original_price.text
    else:
        #print(title, "<할인되지 않은 영화 제외>")
        continue

    # 할인 된 가격
    price = movie.find("span", class_="VfPpfd ZdBevf i5DZme").text

    # 링크
    a_link = movie.find("a", class_="JC71ub")["href"]
 
    link = "https://play.google.com/" + a_link

    print( f"title:{title}")
    print( f"original_price:{original_price}")
    print( f"price:{price}")
    print( f"link: {link}")
    print("-"*50)

browser.quit()

