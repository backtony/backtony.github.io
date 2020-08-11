---
layout: post
title:  파이썬 파트 4-3. 반복문과 while 반복문
subtitle:   파이썬 파트 4-3. 반복문과 while 반복문
categories: python
tags: basics book python 
comments: true
# header-img:
---
+ __목차__
  - [1. 범위(range)](#1-범위range)
  - [2. for 반복문: 범위와 함께 사용하기](#2-for-반복문-범위와-함께-사용하기)
  - [3. for 반복문: 리스트와 범위 조합하기](#3-for-반복문-리스트와-범위-조합하기)
  - [4. for 반복문: 반대로 반복하기](#4-for-반목문-반대로-반복하기)
  - [5. while 반복문](#5-while-반복문)
  - [6. while 반복문: for 반복문처럼 사용하기](#6-while-반복문-for-반복문처럼-사용하기)
  - [7. while 반복문: 상태를 기반으로 반복하기](#7-while-반복문-상태를-기반으로-반복하기)
  - [8. while 반복문: 시간을 기반으로 반복하기](#8-while-반복문-시간을-기반으로-반복하기)
  - [9. while 반복문: break/continue](#9-while-반복문-breakcontinue)

## 1. 범위(range)
---
for 반복문과 함께 많이 사용된다.  
+ 매개변수에 숫자를 한 개 넣는 방법
+ 매개변수에 숫자를 두 개 넣는 방법
+ 매개변수에 숫자를 세 개 넣는 방법
```
range(A) # 0부터 A-1까지
range(A,B) # A부터 B-1 까지
range(A,B,C) # A부터 B-1 까지, 공차가 C
```

__range(0,10) 에서 10은 포함되지 않는다.__  
10을 반드시 포함해야 한다는 것을 강조하고 싶을때 아래와 같이 작성한다. 이후에 코드를 볼 때 더욱 쉽게 이해할 수 있다.
```
range(0,10+1)
```

__주의점__  
range() 함수의 매개변수로는 반드시 정수를 사용해야한다.  
```
a = rang(0,n/2) # 실수가 나오므로 TypeError 발생
a = rang(0m n//2) # 몫만 나오는 정수 나누기 연산자를 사용해야 한다.
```
<br>

## 2. for 반복문: 범위와 함께 사용하기
---
```
기본 형태
for 숫자변수 in 범위:
    코드

예시
for i in range(5):
    print(str(i) + " = 반복 변수")
```
<br>

## 3. for 반복문: 리스트와 범위 조합하기
---
반복을 적용하다 보면 몇 번째 반복인지 알아야 하는 경우가 있다. 이때 가장 쉬운 방법은 범위를 조합해서 사용하는 것이다.
```
arr = [273,32,103,57,52]

for i in range(len(arr)):
    print("{}번째 반복 : {}".format(i,arr[i]))
```
<br>

## 4. for 반복문: 반대로 반복하기
---
```
# 방법 1
for i in range(4, 0-1, -1) # 공차 -1, 범위 0포함을 강조
    print("현재 변수 : {}".format(i))

# 방법 2
for i in reversed(range(5)) : # 거꾸로 뒤집는 함수 reversed
    print("현재 변수 : {}".format(i))    
```
<br>

## 5. while 반복문
---
```
기본 형태
while 불 표현식 :
    코드
```
+ for 반복문 이외에도 범용적으로 사용할 수 있는 반복문이다.
+ 무한 반복시 Ctrl + C 를 입력해서 강제 종료

<br>

## 6. while 반복문: for 반복문처럼 사용하기
---
```
i =0
while i< 10:
    print("{}번째 반복".format(i))
    i+=1
```
<br>

## 7. while 반복문: 상태를 기반으로 반복하기
---
```
list_a = [1,2,1,2]
value = 2

while value in list_a :  # value값이 list_a에 있을때 반복
    list_a.remove(value)

print(list_a)
```
<br>

## 8. while 반복문: 시간을 기반으로 반복하기
유닉스 타임이란 세계 표순시로, 1970년 1월 1일 0시 0분 0초를 기준으로 몇 초가 지났는지를 정수로 나타낸 것을 말한다. 유닉스 타임을 구할 때는 아래 코드를 사용한다.  
```
# 시간 관련 기능 가져오기
import time

# 유닉스 타임(time.time) 변수에 대입하기
target = time.time() +5
number = 0
while time.time() < target:
    number += 1

print("5초 동안 {}번 반복".format(number))
```
시간을 기반으로 조건을 걸때는 while 반복문을 사용한다는 것을 기억할 것.
<br>

## 9. while 반복문: break/continue
---
+ break : 반복문을 벗어날 때 사용하는 키워드
+ continue : 현재 반복을 생략하고 다음 반복을 넘어갈 때 사용하는 키워드

```
# break
i=0
while True :
    print("{}번째 반복".format(i))
    i += 1
    input_a = input("종료하려면 y: ")
    if input_a in ["y","Y"] :
        print("end")
        break # 반복 중단

# continue
numbers = [5,15,6,20,7,25]

for number in numbers:
    if number < 10 :  # if else 보다 이후 처리의 들여쓰기를 줄일 수 있음
        continue # 아래 코딩 생략하고 다시 for문 반복
    print(number)
```
<br>

__문제 : 1부터 100까지 숫자가 있을때 1*99 2*98 3* 97 로 계산한다 했을때 최대 값__  
```
max_value = 0
a=0
b=0

for i in range(1,100//2+1):
    j= 100-i
    if i*j > max_value:
        max_value=i*j
        a=i
        b=j
print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))
```


---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__