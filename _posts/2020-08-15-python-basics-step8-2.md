---
layout: post
title:  파이썬 파트 8-2. 외부 모듈
subtitle:   파이썬 파트 8-2. 외부 모듈
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

## 1. 모듈 설치하기
---
```
pip install 모듈 이름
```
<br>

## 2. BeautifulSoup 모듈
---
BeautifulSoup은 파이썬의 유명한 웹 페이지 분석 모듈이다. BeautifulSoup을 주로 다루는 책을 공부하는 것이 아니므로 간단하게만 살펴보자. BeautifulSoup 함수의 매개변수로 HTML 문자열과 "html.parser"라는 문자열을 넣으면 BeautifulSoup이라는 특수한 객체를 리턴한다.  
```
# BeautifulSoup 모듈로 날씨 가져오기

from urllib import request
from bs4 import BeautifulSoup

# urlopen으로 기상청 전국 날씨 읽기
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

# BeautifulSoup를 이용해 웹 페이지 분석
soup = BeautifulSoup(target,"html.parser")

# location 태그 찾기
# 태그를 여러 개 선택할 때는 select() 함수, 하나만 선택할 때는 select_one() 함수 이용
for location in soup.select("location"):
    # 내부의 city 태그를 찾아서 출력
    print("도시:",location.select_one("city").string) 
    # .string 으로 인해 문자열로만 출력됨 : 도시:서울
    # string 없으면 <city>서울</city>
```
<br>

## 3. Flask 모듈
---
일반적으로 파이썬 웹 개발에서는 Django(장고) 또는 Flask(플라스크) 등의 모듈을 사용한다. Django는 매우 다양한 기능을 제공하는 웹 개발 프레임워크이고, Flask는 작은 기능만을 제공하는 웹 개발 프레임워크이다.  
```
# 설치
pip install flask

# 사용하기
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello world!</h1>"

# 실행 방법
# window
set FLASK_APP=파일이름.py
flask run

# mac
export FLASK_APP=파일이름.py
flask run
```
Flask 모듈은 @app.route(경로)처럼 경로에 들어갈 때 실행할 함수를 지정하는 형태로 사용한다. 이때 함수에서 리턴하는 문자열을 기반으로 HTML 파일을 웹 브라우저에 제공한다.  
경로에 들어갈 때 마다 함수가 실행되므로, 이전에 만들었던 BeautifulSoup 스크레이핑을 실행하는 코드를 만든다면 아래와 같이 된다. 단지 이전의 코드를 hello() 함수 내부에 넣고, 문자열을 리턴하도록 바꿨을 뿐이다.  
```
# 모듈 읽어 들이기
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성하기
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen으로 기상청 전국 날씨 읽기
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

    # BeautifulSoup를 이용해 웹 페이지 분석
    soup = BeautifulSoup(target,"html.parser")

    # location 태그 찾기
    output = ""
    for location in soup.select("location"):
        # 내부의 city 태그를 찾아서 출력
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날시: {}<br/>".format(location.select_one("wf").string)
        output +="<hr/>"
    return output        
```
<br>

## 4. 라이브러리와 프레임워크
---

구분|설명
---|---
라이브러리|정상적인 제어를 하는 모듈
프레임워크|제어 역전이 발생하는 모듈

### 라이브러리
제어 역전이랑 말 그대로 제어가 역전되었다는 뜻이다. 따라서 정상적인 제어가 무슨 말인지 알아야 이해할 수 있다. math 모듈로 알아보자.  
```
from math import sin, cos

print(sin(1))
print(cos(1))
```
위와 같이 math 모듈은 모듈 내부의 기능을 '개발자'가 직접 호출했다. 이처럼 개발자가 모듈의 기능을 호출하는 형태의 모듈을 `라이브러리`라고 한다.  

### 프레임워크
Flask 모듈로 알아보자.  
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello world!</h1>"
```
코드를 보면 내부에 함수만 정의했지 직접적으로 무언가 진행하는 코드는 단 하나도 없다. 실행시켜보면 우리가 출력했던 적이 없던 문자들만이 출력된다. 그럼 이것은 어디서 출력된 것일까?  
바로 Flask 모듈 내부이다. 우리는 우리가 작성한 코드를 직접 실행하지 않았다. Flask 모듈이 제공하는 명령어를 실행하면 Flask가 내부적으로 서버를 실행한 뒤 지정한 파일을 읽어 들여 적절한 상황에 스스로 실행하게 된다. 이처럼 모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈을 `프레임워크`라고 한다.  
<br>

__즉, 개발자가 모듈의 함수를 호출하는 것이 일반적인 제어 흐름이고, 개발자가 만든 함수를 모듈이 실행하는 것은 제어가 역전된 것이다.__  
cf) 제어 역전 : IOC(Inverse of Control)  
<br>

## 5. 함수 데코레이터
---
데코레이터는 만드는 방법에 따라 함수 데코레이터와 클래스 데코레이터로 나눌 수 있다. 여기서는 함수 데코레이터를 살펴보자. 함수 데코레이터는 함수에 사용되는 데코레이터이다. 이 말은 대상 함수의 앞뒤에 꾸밀 부가적인 내용을, 혹은 반복할 내용을 데코레이터로 정의해서 손쉽게 사용할 수 있도록 한 것을 말한다.  
```
def trace(func):
    def wrapper():
        print("인사 시작")
        func()
        print("인사 종료")
    return wrapper # ()가 없이 함수 자체를 반환
    
@trace 
def hello():
    print("hello")
# 결국 hello 함수 호출시 wrapper이라는 함수 자체가 반환

hello()

# 출력
인사 시작
hello
인사 종료

# 데코레이터를 여러 개 사용
def trace1(func):
    def wrapper():
        print("인사 할까요?")
        func()        
    return wrapper 
def trace2(func):
    def wrapper():
        print("인사 할게요")
        func()        
    return wrapper # 
    
@trace1   # 위에서부터 순서대로 
@trace2
def hello():
    print("hello")

hello()

# 출력
인사 할까요?
인사 할게요
hello
```
[![그림1](https://backtony.github.io/assets/img/post/python/basics/8-2.PNG)](https://dojang.io/mod/page/view.php?id=2427)

'함수에 데코레이터를 붙일 경우 기존 함수를 수정하지 않고 내용을 추가할 수 있다' 정도로 알아두자.  
<br>

## 6. 모듈 만들기
---
C언어의 헤더와 유사하다. 매우 간단한 내용이다.  
```
# my_module.py
PI = 3.141592

def number_input():
    output = input("숫자 입력: ")
    return float(output)
def get_circumference(radius):
    return 2*PI*radius
def get_circle_area(radius):
    return PI*(radius**2)

# test.py
import my_module as m # 모듈을 가져오고 이름 수정

radius = m.number_input()
print(m.get_circumference(radius))
print(m.get_circle_area(radius))
```
<br>

## 7. \_\_name\_\_ == "\_\_main\_\_"
---
프로그래밍 언어에서는 프로그램의 진입점을 `엔트리 포인트` 또는 `메인`이라고 한다. 그리고 이러한 엔트리 포인트 또는 메인 내부에서의 \_\_name\_\_은 "\_\_main\_\_"이다.  

### 모듈의 \_\_name\_\_
모듈 내부에서 \_\_name\_\_을 입력하면 모듈의 이름을 나타낸다.  
```
6. 모듈만들기에서 사용했던 코드에서 my_module.py와 test.py에 print(__name__) 를 추가하고 
test.py를 실행시

# 출력
my_module
__main__

test.py에서 import my_module로 인해 my_module.py로 이동해서 print(__name__) 이 실행되는데 
엔트리 포인트가 아니므로 모듈 이름인 my_module 를 출력한다.
다시 test.py로 돌아와 print(__name__) 에서 __main__이 출력된다. 
엔트리 포인트에서는 __name__이 __main__으로 출력된다.
```

### \_\_name\_\_ 활용하기
엔트리 포인트 내부에서는 \_\_name\_\_이 "\_\_main\_\_"이라는 값을 갖기 때문에 현재 파일이 모듈로 실행되는지, 엔트리 포인트로 실행되는지 확인할 수 있다. 따라서 이를 활용하면 엔트리 포인트일 경우에만 작동하는 코드를 만들 수 있다.
```
# my_module.py
PI = 3.141592

def number_input():
    output = input("숫자 입력: ")
    return float(output)
def get_circle_area(radius):
    return PI*(radius**2)
if __name__ == "__main__":  # 엔트리포인트면 작동
    print(get_circle_area(10))

# test.py
import my_module as m 

radius = m.number_input()
print(m.get_circle_area(radius))
```
<br>

## 8. 패키지
---
### 만들기 및 사용하기
쉬운 이해를 위해 import로 가져오는 모든 것을 모듈이라고 이해했는데, pip은 Python Package Index의 줄임말로 패키지 관리 시스템이다. 그럼 패키지와 모듈은 무엇이 다를까? 결론부터 말하면 모듈이 모여서 구조를 이루면 패키지이다.  
만드는 방법은 간단하다. 모듈을 넣을 폴더를 만들고 그 안에 모듈을 넣으면 된다. 폴더명을 'test_package'라고 하고 안에 module_a.py와 module_b.py를 넣어두었다고 하면 main.py에서 사용할 때는 import test_package.module_a 와 같이 사용하면 된다.  

### \_\_init\_\_.py파일
패키지를 읽을 때 어떤 처리를 수행해야 하거나 패키지 내부의 모듈들을 한꺼번에 가져오고 싶을 때가 있다. 이때 패키지 폴더 내부에 \_\_init\_\_.py파일을 만들어 사용한다.  
패키지 폴더 내부에 \_\_init\_\_.py를 추가하게 되면 패키지를 읽어 들일 때 \_\_init\_\_.py를 가장 먼저 실행하게 된다. \_\_init\_\_.py에서는 \_\_all\_\_이라는 이름의 리스트를 만드는데, 이 리스트에 지정한 모듈들이 from 패키지이름 import * 를 사용시 전부 읽어 들여지는 것이다.


---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__

