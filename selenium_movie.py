import requests
from bs4 import BeautifulSoup

URL = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

res = requests.get(URL, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

movies = soup.find_all('div', class_="ImZGtf mpg5gc")
print(len(movies))

#with open("movie.html","w",encoding="utf8")as f:
#    #f.write(res.text)
#    f.write(soup.prettify()) #html 문서 예쁘게 출력

lst = []
for movie in movies:
    title = movie.find('div', class_="WsMG1c nnK0zc").text
    print(title)