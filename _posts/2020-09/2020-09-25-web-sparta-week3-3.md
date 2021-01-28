---
layout: post
title:  mongoDB와 pymongo
subtitle:   mongoDB와 pymongo
categories: web
tags: sparta web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. DB 설치 확인](#1-db-설치-확인)
  - [2. DB개괄](#2-db개괄)
  - [3. pymongo로 DB조작하기](#3-pymongo로-db조작하기)
  - [4. 연습하기](#4-연습하기)    

## 1. DB 설치 확인
---
주소창에 localhost:27017 이라고 쳤을 때 아래와 같은 내용이 나오면 mongoDB가 돌아가고 있는 것이다.
```
It looks like you are trying to access MongoDB over HTTP on the native driver port.
```
<br>

### robo 3T의 역할
mongoDB는 눈에 보이지 않는다. 유식한 말로는 그래픽인터페이스(=GUI)를 제공하지 않는다고 표현한다. 데이터를 저장했는데 눈으로 보이진 않고 답답하기 때문에 DB내부에 살펴보기 위한 프로그램을 따로 설치해야 한다. 그것이 바로 robo3T의 역할이다.
<br>

## 2. DB개괄
---
### RDBMS(SQL)
행/열의 생김새가 정해진 엑셀에 데이터를 저장하는 것과 유사하다. 데이터 50만 개가 적재된 상태에서, 갑자기 중간에 열을 하나 더하기는 어려울 것이다. 그러나, 정형화되어 있는 만큼 데이터의 일관성이나 분석에 용이할 수 있다. ex) My-SQL 등
<br>

### No-SQL
딕셔너리 형태로 데이터를 저장해두는 DB이다. 고로 데이터 하나 하나 마다 같은 값들을 가질 필요가 없게 된다. 자유로운 형태의 데이터 적재에 유리한 대신, 일관성이 부족할 수 있다. ex)MongoDB
<br>

## 3. pymongo로 DB조작하기
---
pymongo 기본 코드
```python
from pymongo import MongoClient  # pymongo를 쓰겠다
client = MongoClient('localhost', 27017) # 내 컴퓨터에서 돌아가고 있는 파이몽고에 접근해라
db = client.dbsparta # dbsparta라는 이름의 DB에 접근해라, 없다면 자동 생성

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)
# users는 그냥 우리가 정해주는 콜렉션 이름이다.
# 콜렉션이란 몽고db도 아무리 비정형적이라고 하지만 그래도
# 비슷한 애들끼리 묶어놓자는 의미에서 나온 개념
# 없으면 자동으로 생성
# insert_one()은 인자를 DB에 저장함

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})
# {} 안에 아무것도 없으면 맨 위에서 찾아지고 user을 출력하면 '_id'값이 나오는데
# 이 값의 출력을 원하지 않으면 
# user = db.users.find_one({'name':'bobby'},{'_id':False}) 
# 뒤에 값을 0이나 False 주며 된다

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))
# age:21인 모든 값을 리스트로

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
```
<br>

## 4. 연습하기
---
웹스크래핑(크롤링) [[클릭](https://backtony.github.io/web/2020/09/27/web-sparta-week3-2/)] 의 연습하기에서 사용했던 코드를 사용해 pymongo를 연습해보자.
```python
from pymongo import MongoClient  # pymongo를 쓰겠다

client = MongoClient('localhost', 27017)  # 내 컴퓨터에서 돌아가고 있는 파이몽고에 접근해라
db = client.dbsparta  # dbsparta라는 이름의 DB에 접근해라, 없다면 자동 생성됨

import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_rank = movie.select_one('td:nth-child(1) > img')
    a_tag = movie.select_one('td.title > div > a')
    a_rate = movie.select_one('td.point')
    if a_tag is not None:
        # text는 말그대로 태그를 제외한 text문장 , ['속성']은 해당 속성을 나타냄
        doc = {
            'rank': a_rank['alt'],
            'title': a_tag.text,
            'rate': a_rate.text
        }
        db.movies.insert_one(doc)
```
<Br>

위에 결과로 인해 db에 저장된 것들을 그대로 활용하여  
1. 매트릭스 평점 가져오기
2. 매트릭스의 평점과 같은 평점의 영화 이름 출력하기
3. 매트릭스 영화의 평점을 0으로 만들기


__1번__  
```python
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


movie = db.movies.find_one({'title':'매트릭스'})
print(movie['rate'])
```
<br>

__2번__  
```python
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['rate']
movies = list(db.movies.find({'rate':target_star}))

for movie in movies:
    print(movie['title'])
```
<Br>

__3번__  
```python
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


db.movies.update_one({'title':'매트릭스'},{'$set':{'rate':'0'}})
```
<br>

__지니뮤직 순위, 곡 제목, 가수 스크래핑하기__  
```python
import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    rank = music.select_one('td.number')
    title = music.select_one('td.info > a.title.ellipsis')
    singer = music.select_one('td.info > a.artist.ellipsis')
    print(rank.text.split()[0],title.text.strip(),singer.text)
```