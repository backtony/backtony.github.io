---
layout: post
title:  웹스크래핑(크롤링)
subtitle:   웹스크래핑(크롤링)
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 크롤링 기본 세팅](#1-크롤링-기본-세팅)
  - [2. select/select_one](#2-select/selectone)
  - [3. 연습하기](#3-연습하기)    

## 1. 크롤링 기본 세팅
---
기본 형태
```python
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 우리가 웹에서 엔터를 치는 것과 코드가 API 콜을 할 때 headers에서 차이가 있다.
# 그것을 마치 우리가 엔터 친 것과 비슷하게 만들어 주려고 headers 값을 강제로 만들어 넣어준다.
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################
```
<br>

## 2. select/select_one
Beautifulsoup은 select/select_one만 기억하면 된다.  
+ select : 여러 개를 가져오는 것
+ select_one : 한 개를 가져오는 것
+ 태그 안의 텍스트를 찍고 싶을 땐 -> 태그.text
+ 태그 안의 속성을 찍고 싶을 땐 -> 태그['속성']

beautifulsoup 내 select에 미리 정의된 방법
```python
# 선택자를 사용하는 방법 (copy selector)
soup.select('태그명')
soup.select('.클래스명')
soup.select('#아이디명')

soup.select('상위태그명 > 하위태그명 > 하위태그명')
soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

# 태그와 속성값으로 찾는 방법
soup.select('태그명[속성="값"]')

# 한 개만 가져오고 싶은 경우
soup.select_one('위와 동일')
```
<br>


## 3. 연습하기
![그림1](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week3-2.PNG)
```
https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303
```
위의 영화페이지를 활용하여 그림처럼 출력하기
```python
import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
# 크롬에서 select을 원하는 내용을 우클릭 검사를 통해 select copy를 할 수 있다.
# 이 과정에서 #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# 이와 같이 복사가 되는데 tr뒤에 :nth-child(2)는 클릭한 내용에 해당하는 값이다.
movies = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point
# 선택하고 싶은 부분을 크롬에서 각각 검사를 눌러보고 어떤 부분이 공통되는 부분이며
# 어느 것을 넣으면 될까 찾아봐

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_rank = movie.select_one('td:nth-child(1) > img')
    a_tag = movie.select_one('td.title > div > a')
    a_rate = movie.select_one('td.point')
    if a_tag is not None:
        # text는 말그대로 태그를 제외한 text문장 , ['속성']은 해당 속성을 나타냄
        print(a_rank['alt'],a_tag.text,a_rate.text)

```
