from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse

categories = ['사랑',
  '인생',
  '공부',
  '성공',
  '친구',
  '독서',
  '이별',
  '시간',
  '노력',
  '희망',
  '도전',
  '자신감'];
data = {}
for keyword in categories:
  data[keyword] = []

for keyword in categories:
  url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&qvt=0&query={parse.quote(keyword)}%20%EB%AA%85%EC%96%B8"
  #print("url: ", url)
  html = urlopen(url)
  bsObject = BeautifulSoup(html, "html.parser")
  
  for link in bsObject.find_all('p', {"class": "lngkr"}):
    data[keyword].append(link.text)

print(data)