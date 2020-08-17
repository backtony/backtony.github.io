---
layout: post
title:  파이썬 파트 8-1. 표준 모듈
subtitle:   파이썬 파트 8-1. 표준 모듈
categories: python
tags: basics book python 모듈
comments: true
# header-img:
---
+ __목차__
  - [1. 시작하기 전](#1-시작하기-전)
  - [2. 모듈 사용의 기본: math 모듈](#2-모듈-사용의-기본-math-모듈)
  - [3. from 과 as 구문](#3-from-과-as-구문)
  - [4. random 모듈](#4-random-모듈)
  - [5. sys 모듈](#5-sys-모듈)
  - [6. os 모듈](#6-os-모듈)
  - [7. datetime 모듈](#7-datetime-모듈)
  - [8. time 모듈](#8-time-모듈)
  - [9. urllib 모듈](#9-urllib-모듈)
  - [10. 정리하기](#10-정리하기)


## 1. 시작하기 전
---
파이썬은 모듈이라는 기능을 활용해 코드를 분리하고 공유한다. 모듈은 여러 변수와 함수를 가지고 있는 집합체로, 크게 표준 모듈과 외부 모듈로 나뉜다. 파이썬에 기본적으로 내장되어있는 모듈을 표준 모듈이라고 하고, 다른 사람들이 만들어 공개한 모듈을 외부 모듈이라고 한다. 일반적으로 모듈을 가져올 때는 import 구문을 사용한다.  
```
import 모듈 이름
```
<br>

## 2. 모듈 사용의 기본: math 모듈
---
math 모듈은 수학과 관련된 기능을 가지고 있다.  
```
import math

# 사용 예시
print(math.pi)
print(math.sin(10))
```
__math 모듈 기능 몇 가지 정리__  

변수 또는 함수|설명
---|---
sin(x)|사인값
cos(x)|코사인값
tan(x)|탄젠트값
log10(x)|상용로그값
log(x)|자연로그값
ceil(x)|올림
floor(x)|내림
round(x)|반올림인데 소수가 5일때 정수가 짝수이면 내림, 홀수이면 올림

<br>

## 3. from 과 as 구문
---
### from
모듈에는 정말 많은 변수와 함수가 들어있는데 사용하고자 하는 기능이 극히 일부일 때 사용한다.  
```
# 기본 형태
from 모듈이름 import 가져오고 싶은 변수 또는 함수
from 모듈이름 import *   # 모든 기능을 가져오고 싶다면 *를 사용

# 예시
from math import floor, ceil

print(floor(2.2)) # 일반적인 import 구문과 다르게 바로 floor, ceil을 사용한다.
print(ceil(2.2))
```

### as
모듈을 가져올 때 이름 충돌이 발생하는 경우, 모듈 이름이 너무 길어서 짧게 사용하고 싶은 경우에 사용한다.  
```
# 기본 형태
import 모듈 as 사용하고 싶은 식별자

# 예시
import math as m # math를 이제부터 m으로 사용가능

print(m.pi)
```
<br>

## 4. random 모듈
---
랜덤한 값을 생성할 때 사용한다.  
```
# 기본 형태
import random

# 예시
import random

# random : 0.0 <= x <1.0 사이의 float 값을 리턴
print(random.random())

# uniform(min,max): 지정한 범위 사이의 float 값을 리턴
print(random.uniform(10,20))

# randrange(max) : 0 부터 max 사이의 int값 리턴
# randrange(min, max) : min 부터 max 사이의 int값 리턴
print(random.randrange(20))

# choice(list) : 리스트 내부에 있는 요소를 랜덤하게 선택
print(random.choice([1,2,3,4]))

# shuffle(list) : 리스트의 요소를 랜덤하게 섞는다.
a = [1,2,3,4,5]
random.shuffle(a)
print(a)

# sample(list, k=숫자): 리스트의 요소 중 k개를 뽑는다.
print(random.sample([1,2,3,4,5],k=3))
```
__주의 사항: 파일 이름은 모듈 이름과 달라야한다.__  
파일 이름을 모듈 이름으로 저장했다간 오류가 발생한다. 사실 파이썬의 모듈도 파이썬 파일이다. 따라서 같은 이름으로 저장하게 되면 import에서 모듈을 불러오는게 아니라 내가 저장한 파일 즉, 같은 파일을 불러오게 되는 것이므로 오류가 발생한다.  

<br>

## 5. sys 모듈
---
시스템과 관련된 정보를 가지고 있는 모듈이다.  
```
# 기본 형태
import sys

# 예시
import sys

# 명령 매개변수를 출력
print(sys.argv) 

# 컴퓨터 환경과 관련 정보 출력 
print(sys.getwindowsversion())
print(sys.copyright)
print(sys.version)
```
sys.argv는 명령 배개변수이다. 프로그램을 실행할 때 추가로 입력하는 값들을 의미한다. python 파일이름.py 10 20 30 이렇게 코드 실행시 sys.argv에 \['파일이름.py', '10', '20', '30'] 이라는 리스트가 들어온다.  
<br>

## 6. os 모듈
---
운영체제와 관련된 기능을 가진 모듈이다.
```
# 기본 형태
import os

# 예시
import os

print(os.name) # 현재 운영체제
print(os.getcwd()) # 현재 폴더
print(os.listdir()) # 현재 폴더 내부 요소

# 폴더 만들고 제거(폴더가 비어있을 때만 제거 가능)
os.mkdir("makeitrain")
os.rmdir("makeitrain")

# 파일 생성하고 파일 이름 변경
with open("original.txt","w") as file:
    file.write("hello")
os.rename("original.txt","new.txt")

# 파일 제거
os.remove("new.txt")
```
<br>

## 7. datetime 모듈
---
날짜와 시간과 관련된 모듈로 날짜 형식을 만들 때 자주 사용된다.  
```
# 기본 형태
import datetime

# 예시
import datetime

now = datetime.datetime.now()

# 여러가지 시간 출력 방법 : strftime
output_a = now.strftime("%Y년 %m월 %d일 %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,now.day,now.hour,now.minute,now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
# 문자열, 리스트 등 앞에 *를 붙이면 요소 하나하나가 매개변수로 지정

print(output_a)
print(output_b)
print(output_c)

# 특정 시간 이후의 시간 구하기 : timedelta
after = now + datetime.timedelta(\
    weeks=1, days=1, hours=1, minutes=1, seconds=1)
print(after.strftime("%Y년 %m월 %d일 %H:%M:%S"))

# 특정 시간 요소 교체: replace
output = now.replace(year=(now.year+1))
print(output.strftime("%Y년 %m월 %d일 %H:%M:%S"))
```
<br>

## 8. time 모듈
---
시간 관련 기능을 다룰때 사용한다. 날짜와 관련된 처리가 가능하긴 하지만 날짜 관련 처리는 datetime을 사용한다.  
```
# 기본 형태 
import time

# 예시
import time

print("지금부터 5초간 정지")
time.sleep(5)
print("프로그램 종료")
```
<br>

## 9. urllib 모듈
---
url 을 다루는 라이브러리라는 뜻이다. 간단하게 웹 브라우저의 주소창에 입력하는 주소를 다룬다고 생각하면 된다.  
```
# 기본 형태
import urllib

# 예시
from urllib import request

target = request.urlopen("https://youtube.com")
output = target.read()

print(output)
```
urllib 모듈에 있는 request를 가져왔다. request도 모듈이라 request 내부에 있는 urlopen 함수를 request.urlopen 형태로 사용한다. urlopen은 url 주소 페이지를 열어주는 함수이다. read 함수는 해당 내용을 읽어서 가져온다.  
<br>

## 10. 정리하기
---
+ 표준 모듈은 파이썬이 기본적으로 제공하는 모듈
+ import 구문은 모듈을 읽어 들일 때 사용하는 구문
+ as 키워드는 모듈을 읽어 들이고 별칭을 붙일 때 사용하는 구문
+ 파이썬 문서는 모듈의 자세한 사용 방법이 들어있는 문서

__cf) 버그, 디버그, 디버거__  
+ 버그 : 사소한 결함, 프로그램의 예상하지 못한 오류
+ 디버그 : 버그를 제거하는 것
+ 디버거 : 그걸 도와주는 프로그램

vscode에서 중단점을 만들고 왼쪽 벌레가 그려진 실행 탭을 누르고 디버그해서 하나씩 확인해 나가면서 오류 수정  
<br>

__문제 : os모듈의 os.listdir() 함수와 os.path.isdir() 함수를 사용하면 특정 디렉터리를 읽어 파일 디렉터리인지를 확인할 수 있다. 이를 활용하여 '폴더라면 또 탐색하기'라는 재귀 구성으로 현재 폴더 내부에 있는 모든 파일을 탐색하는 코드를 작성하시오.__  
```
import os
def read_folder(path):
    output =os.listdir(path) # 현재 폴더안의 파일들을 리스트로 만들고 output에 저장
    for item in output:
        # 디렉터리인지 아닌지 확인    
        if os.path.isdir(item):  
            read_folder(path+"/"+item) # 맞으면 디렉터리 안에서 다시 조사
        else :
            print("파일:",item)  # 파일이면 바로 출력


read_folder(".") # .는 현재 폴더를 의미
```
<br>


---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__

