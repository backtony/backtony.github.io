---
layout: post
title:  파이썬 파트 7-2. 클래스의 추가적인 구문
subtitle:   파이썬 파트 7-2. 클래스의 추가적인 구문
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

## 1. 시작하기 전
---
클래스를 사용하는 것은 작정하고 속성과 기능을 가진 객체를 만들겠다는 뜻이다. 그래서 파이썬은 그에 따른 부가적인 기능을 제공한다. 예를 들어 어떤 클래스를 기반으로 속성과 기능을 물려받아 새로운 클래스를 만드는 `상속`, 이러한 상속 관계에 따라서 객체가 어떤 클래스를 기반으로 만들었는지 확인해주는 `isinstance() 함수`, 파이썬 기본적으로 제공하는 `str() 함수` 혹은 연산자를 사용해서 클래스의 특정 함수를 호출할 수 있게 해주는 기능이 대표적이다.  
<br>

## 2. 어떤 클래스의 인스턴스인지 확인하기: isinstance()
---
객체(인스턴스)가 어떤 클래스로부터 만들어졌는지 확인할 수 있도록 isinstance() 함수를 제공한다.  
```
# 기본 형태
isinstance(인스턴스, 클래스) # 맞으면 True 틀리면 False 리턴

# 예시
class Student:
  def __init__(self):
    pass

student = Student()

print(isinstance(student,Student)) # True
```
__cf type과 isinstance 비교__  
```
class Human:
  def __init__(self):
    pass
class Student(Human):
  def __init__(self):
    pass

student = Student()

print(isinstance(student,Student)) # True
print(type(student) == Human) # False
```
Student 클래스는 Human 클래스를 상속받아서 만들었다. isinstance 는 이러한 상속 관계까지 고려해서 확인하지만 type 은 상속 관계는 확인하지 않는다.  
<br>

## 3. 특수한 이름의 메소드
---
객취 뒤에.(마침표)를 입력해서 자동 완성 기능을 보면 \__이름\__() 형태의 메소드가 보인다. 이러한 형태의 메소드는 특수한 상황에 자동으로 호출되도록 만들어졌다.  
```
class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.korean,self.math)

student = [Student("장보고",85,95), Student("이순신",90,93), Student("손오공",85,90)]
print("이름","총점","평균",sep="\t")
for i in student:
    print(str(i))    # str(객체)
```

__cf) 크기 비교 함수 이름__  
이름|영어|설명
---|---|---
eq|equal|같다
ne|not equal|다르다
gt|greater than|크다
ge|greater than or equal|크거나 같다
lt|less than|작다
le|less than or equal|작거나 같다

```
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
        
    def __eq__(self,value):
        if isinstance(value,Student): # 자료형을 한정하고 싶다면
          raise TypeError("Student 클래스의 인스턴스만 비교 가능합니다")
        return self.get_sum() == value.get_sum()
    def __ne__(self,value):
        return self.get_sum() != value.get_sum()
    def __gt__(self,value):
        return self.get_sum() > value.get_sum()
    def __ge__(self,value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self,value):
        return self.get_sum() < value.get_sum()
    def __le__(self,value):
        return self.get_sum() <= value.get_sum()

a = Student("장보고",85,95)
b = Student("이순신",90,93)

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
```
<br>

## 4. 클래스 변수와 메소드
---
인스턴스가 속성과 기능을 가질 수도 있지만, 클래스가 속성(변수)와 기능(함수)를 가질 수도 있다.  

### 클래스 변수
```
# 클래스 변수 만들기
class 클래스 이름:
  클래스 변수 = 값

# 클래스 변수에 접근하기
클래스 이름.변수 이름

# 예시
class Student :
  count =0

  def __init__(self,name,korean,math):
    self.name = name
    self.korean = korean
    self.math = math

    Student.count+=1
    print("{}번째 학생이 생성".format(Student.count))

students = [Student("이순신",80,85), Student("해신",88,95)]

print(" 현재 생성된 학생 수 : {}".format(Student.count))
```

### 클래스 함수
클래스 함수도 클래스 변수처럼 그냥 클래스가 가진 함수이다. 일반적인 함수로 만드나 클래스 함수로 만드나 사용에는 큰 차이가 없지만 클래스가 가진 기능이라고 명시적으로 나타내는 것 뿐이다. 다만 생성 방법이 특이하다. @를 사용하는데 @로 시작하는 것을 파이썬에서는 `데코레이터` 라고 하며 꾸며주는 것이라는 의미를 가진다. 인스턴스 함수와 비슷하게 클래스 함수도 첫 인자로 cls(클래스 자체)가 들어간다.  
```
# 클래스 함수 만들기
class 클래스 이름:
  @classmathod # 아무이름이나 무관
  def 클래스 함수(cls,매개변수):
    pass

# 클래스 함수 호출하기
클래스 이름.함수 이름(매개변수)

# 예시
# 클래스 선언
class Student:
    # 클래스 변수
    count =0
    students =[]

    # 클래스 함수
    @classmethod
    def print(cls):
        print("------- 학생 목록 -------")
        print("이름\t총점\t평균")
        for student in cls.students: # 매개변수로 받은 cls활용, Student.students 해도 무관
            print(str(student))

    # 인스턴스 함수
    def __init__(self, name, korean, math):
            self.name = name
            self.korean = korean
            self.math = math
            Student.count +=1
            Student.students.append(self)
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.korean,self.math)
    def get_sum(self):
            return self.korean + self.math
    def get_avg(self):
        return self.get_sum() / 2  # ()는 자동적으로 self

Student("장보고",85,95)
Student("이순신",90,93)
Student("손오공",85,90)

Student.print()
```
<br>

## 5. 가비지 컬렉터
---
프로그램 내부에서 무언가를 생성한다는 것은 `메모리 위에 올린다`는 의미이다. 참고로 메모리가 부족해지면 컴퓨터는 하드디스크를 메모리처럼 사용해 무언가를 올리기 시작한다. 이러한 동작을 `스왑`이라고 하는데, 하드디스크는 메모리보다 훨씬 느리므로 스왑을 처리하는 속도가 느리다.  
어쨋든 프로그램에서 변수를 만들면 데이터가 메모리에 올라가고 계속 만들다보면 메모리가 가득 찰 것이다. 하지만 파이썬 프로그래밍 언어에는 `가비지 컬렉터`라는 것이 있다. 가비지 컬렉터는 더 사용할 가능성이 없는 데이터를 메모리에서 제거하는 역할을 한다. 대표적인 사용할 가능성이 없는 데이터는 변수에 저장되지 않거나, 함수 등에서 나오면서 변수를 활용할 수 없게 되는 경우이다.  
```
class Test:
    def __init__(self,name):
        self.name = name
        print("{} 이 생성되었다.".format(self.name))
    def __del__(self):
        print("{} 이 제거되었다.".format(self.name))

Test("A") # 생성되었다 제거되었다
Test("B") # 생성되었다 제거되었다
Test("C") # 생성되었다 제거되었다

a = Test("A")
b = Test("B")
c = Test("C")
```
A가 생성되고 다음줄로 넘어갈 때 이것을 변수에 저장하지 않으면 가비지 컬렉터는 이후에 활용하지 않겠다는 의미로 이해하고 메모리를 아끼기 위해 과감히 지워버린다. 변수에 저장했을 경우에는 나중에 활용한다는 의미로 이해하고 프로그램이 종료될 때 del 을 실행하게 된다.  
<br>

## 6. 프라이빗 변수
---
### 프라이빗 변수
클래스 내부의 변수를 외부에서 사용하는 것을 막고 싶을 때 인스턴스 변수 이름을 __변수이름 형태로 선언한다.  
```
# 예시
# 모듈 가져오기
import math

# 클래스 선언
class Circle:
    def __init__(self,radius):
        self.__radius = radius # __이 있으므로 외부에서 사용 불가
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)

circle = Circle(10)
print("원의 둘레 :",circle.get_circumference())
print("원의 넓이 :",circle.get_area())

print("__radius 에 접근")
print(circle.__radius)
# AttributeError: 'Circle' object has no attribute
```
<br>

## 7. 게터와 세터
---
프라이빗 변수로 선언했는데 만약 수정하고 싶다면 이때 게터와 세터를 사용한다. 게터와 세터는 프라이빗 변수의 값을 추출하거나 변경할 목적으로, 간접적으로 속성에 접근하도록 해주는 함수이다. 게터와 세터를 사용할 경우 여러가지 추가적 처리가 가능하다. 그저 말만 게터와 세터이지 메소드와 다름 없다.   
### 데코레이터 사용 전
```
# 모듈 가져오기
import math

# 클래스 선언
class Circle:
    def __init__(self,radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)
    def get_radius(self):
        return self.__radius
    def set_radius(self,value):
        if value<=0 : # 추가적 처리
            raise TypeError("길이가 양의 숫자여야 한다.")
        self.__radius = value        

circle = Circle(10)
print("원의 둘레 :",circle.get_circumference())
print("원의 넓이 :",circle.get_area())

print("__radius 에 접근")
print(circle.get_radius())
circle.set_radius(15)
print(circle.get_radius())
```
### 데코레이터 사용후
게터와 세터로 함수를 만드는 일이 많아져 쉽게 만들기 위해 데코레이터를 이용해 쉽게 만들고 사용할 수 있게 되었다.  
+ 게터에는 @property ,세터에는 @변수이름.setter  라는 데코레이터를 붙인다.
+ 함수의 이름은 변수 이름과 같게 한다.
+ 더욱 짧은 코딩으로 접근이 가능
+ 연산자를 이용해서 수정 가능

```
# 모듈 가져오기
import math

# 클래스 선언
class Circle:
    def __init__(self,radius):
        if radius <= 0:
            raise TypeError("양수를 넣어주세요")
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        if value<=0 :
            raise TypeError("길이가 양의 숫자여야 한다.")
        self.__radius = value        

circle = Circle(10)
print("원의 둘레 :",circle.get_circumference())
print("원의 넓이 :",circle.get_area())

print("원래 반지름 :",circle.radius)
circle.radius = 15  # 데코 이전처럼 사용시 오류발생, 연산자사용
print("변경된 반지름 :",circle.radius)

# 데코레이터 이전 접근 및 수정
# print(circle.get_radius())
# circle.set_radius(15)
```
<br>

## 8. 상속
---



---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
