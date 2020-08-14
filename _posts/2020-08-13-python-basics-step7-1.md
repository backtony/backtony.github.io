---
layout: post
title:  파이썬 파트 7-1. 클래스의 기본
subtitle:   파이썬 파트 7-1. 클래스의 기본
categories: python
tags: basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 객체](#1-객체)
  - [2. 클래스 선언하기](#2-클래스-선언하기)
  - [3. 생성자와 소멸자](#3-생성자와-소멸자)
  - [4. 메소드](#4-메소드)
  - [5. 정리](#5-정리)

## 1. 객체
---
```
students = [
    {"name" : "장보고", "math":75 },
    {"name" : "손오공" , "math":95},
]
```
예를 들어 딕셔너리로 학생을 표현하고 이를 리스트로 묶어 학생을 표현했다고 하면, 이렇게 여러 가지 속성을 가질 수 있는 대상을 객체라고 한다. 즉, 속성을 가질 수 있는 모든 것을 `객체`라고 한다.  
cf 1)파이썬은 객체 지향 언어로 `클래스`라는 것을 기반으로 `객체`를 만들고, 그러한 객체를 우선으로 생각해서 프로그래밍을 한다.  
cf 2) 추상화 : 프로그램에서 필요한 요소만을 사용해서 객체를 표현하는 것  
<br>

## 2. 클래스 선언하기
---
+ 클래스를 선언하면 이후 클래스 이름과 같은 함수(생성자)를 이용해서 객체를 만들 수 있다.
+ 인스턴스 이름(변수 이름) = 클래스 이름()  # 여기서 클래스 이름() 이 생성자 함수이다.
+ 클래스를 기반으로 만들어진 객체를 인스턴스 라고 부른다.

```
# 클래스 선언 기본 형태
class 클래스 이름 :     ## 클래스 첫글자는 대문자
    클래스 내용

# 객체 만들기 기본 형태
인스턴스 이름(번수 이름) = 클래스 이름() # 여기서 클래스 이름() 이 생성자 함수

# 예시
# 클래스 선언
class Student :
    pass
# 객체 만들기
student = Student()

# 객체 리스트
students = [Student(), Student(), Student()]
```

## 3. 생성자와 소멸자
---
### 생성자
+ 클래스 이름과 같은 함수를 생성자라고 한다. 
+ 클래스 내부에 \__init__라는 함수를 만들면 객체를 생성하면서 처리할 내용을 작성할 수 있다. 
+ 클래스 내부의 함수의 첫 매개인자로는 반드시 self를 입력해야 한다. 이때 self는 자기 자신을 나타내는 딕셔너리라고 생각하면 된다.
+ self가 가지고 있는 속성과 기능에 접근할 때는 self.식별자 형태로 접근한다.

__cf) \__함수명\__ 형태의 함수는 특수한 경우에 자동으로 호출되는 함수이다.__  
```
# 기본 형태
class 클래스 이름:
    def __init__(self, 추가적 매개변수):
        pass

# 예시
# 클래스 선언
class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math

student = [Student("장보고",85,95), Student("이순신",90,93), Student("손오공",85,90)]

# 접근 방법
student[0].name
student[0].math
```

### 소멸자
프로그램이 종료될 때 자동적으로 소멸자가 호출된다.
```
# 기본 형태
class 클래스 이름:
    def __del__(self):
        pass

# 예시
class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
    def __del__(self):
        print("{}-파괴되었다.".format(self.name))

student = [Student("장보고",85,95), Student("이순신",90,93), Student("손오공",85,90)]
```
<br>

## 4. 메소드
---
클래스가 가지고 있는 함수를 메소드라고 한다. 반드시 첫 번째 매개변수로 self를 넣어야 한다.
```
# 기본 형태
class 클래스 이름:
    def 메소드 이름(self, 추가적 매개변수):
        pass
    
# 예시 
class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math

    def get_sum(self):
        return self.korean + self.math

    def get_avg(self):
        return self.get_sum() / 2  # ()는 자동적으로 self

student = [Student("장보고",85,95), Student("이순신",90,93), Student("손오공",85,90)]
for i in student:
    print("{}의 평균 : {}".format(i.name,i.get_avg()))    
```
__cf) self__  
```
# 클래스 메소드라고 가정
def setdata(self,first,second):
    self.first =first
    self.second = second

a.setdata(4,2)
```
setdata 메소드에는 매개변수가 3개인데 왜 2개의 값만 전달할까? 그 이유는 a.setdata(4,2) 처럼 호출하면 setdata 메소드의 첫 번째 매개변수 self에는 setdata 메소드를 호출한 객체 a가 자동으로 전달되기 때문이다.  

![그림1](https://backtony.github.io/assets/img/post/python/basics/7-1.PNG)(https://wikidocs.net/28)

<br>

## 5. 정리
---
+ 객체 : 속성을 가질 수 있는 모든 것
+ 객체 지향 프로그래밍 언어 : 객체를 기반으로 프로그램을 만드는 프로그래밍 언어
+ 추상화 : 복잡한 자료, 모듈, 시스템 등으로부터 핵심적인 개념 또는 기능을 간추려 내는 것
+ 클래스 : 객체를 쉽고 편리하게 생성하기 위해 만들어진 구문
+ 인스턴스 : 클래스 기반으로 생성한 객체
+ 생성자 : 클래스 이름과 같은 인스턴스를 생성할 때 사용하는 함수
+ 메소드 : 클래스가 가진 함수



---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__

