---
layout: post
title:  파이썬 파트 4-4. 문자열, 리스트, 딕셔너리와 관련된 기본 함수
subtitle:   파이썬 파트 4-4. 문자열, 리스트, 딕셔너리와 관련된 기본 함수
categories: python
tags: basics book python 
comments: true
# header-img:
---
+ __목차__
  - [1. 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()](#1-리스트에-적용할-수-있는-기본-함수-min-max-sum)
  - [2. reversed() 함수로 리스트 뒤집기](#2-reversed-함수로-리스트-뒤집기)
  - [3. enumerate() 함수와 반복문 조합하기](#3-enumerate-함수와-반복문-조합하기)
  - [4. 딕셔너리의 items()함수와 반복문 조합하기](#4-딕셔너리의-items함수와-반복문-조합하기)
  - [5. 리스트 내포](#5-리스트-내포)
  - [6. 구문 내부에 여러 줄 문자열을 사용했을 때의 문제점](#6-구문-내부에-여러-줄-문자열을-사용했을-때의-문제점)
  - [7. 진수변환과 count() 함수](#7-진수변환과-count-함수)

## 1. 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()
---

함수|설명
---|---
min()|리스트 내부에서 최솟값을 찾는다.
max()|리스트 내부에서 최댓값을 찾는다.
sum()|리스트 내부에서 값을 모두 더한다.

__cf) max와 min 함수에서 매개변수로 리스트를 사용하지 않고 숫자 여러개 나열해도 가능하다.__  
```
numbers =[103,52,273,32,77]

print(max(numbers))
print(min(numbers))
print(sum(numbers))

print(max(103,52,273))
```
<br>

## 2. reversed() 함수로 리스트 뒤집기
---
+ 리스트의 요소의 순서를 뒤집고 싶을때 사용한다.
+ reversed 함수의 결과값이 제너레이터이기 때문에 3행에서 object at~~ 이런 출력값이 나온다.
+ reversed의 결과값은 1회용 값이다.
+ for 문에서 사용시 반복할 때마다 next()함수로 요소를 꺼내준다.

```
list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)

print(list_reversed) # 출력 list_reverseiterator object at ~~~
print(list(list_reversed)) # 출력 [5,4,3,2,1]
print(list(list_reversed)) # 출력 [] 1회용이므로

for i in reversed(list_a):
    print(i)

# 출력
5
4
3
2
1
```
__결과값이 1회용이기 때문에 필요한 시점에 직접 사용한다__  
딱 두 형태로 사용한다고 기억하자.  
+ list(reversed(리스트)) : 리스트를 역으로 돌리기
+ for i in reversed(리스트) : 반복문에 적용하기

```
numbers = [1,2,3,4,5]

for i in reversed(numbers): # 직접 사용
    print("첫 번째 반복문: {}".format(i))

for i in reversed(numbers): # 직접 사용
    print("두 번째 반복문: {}".format(i)) 

print(list(reversed(numbers)))
```
__확장 슬라이싱으로 뒤집기[::-1]__  
```
numbers = [1,2,3,4,5]
print(numbers[::-1]) # 출력 [5,4,3,2,1]
```
비파괴적으로 원본에는 영향이 없고 문자열에도 사용 가능하다.  
<br>

## 3. enumerate() 함수와 반복문 조합하기
---
리스트의 요소를 반복할 때 현재 인덱스가 몇 번째인지 확인해야 하는 경우가 많은데 enumerate 함수로 쉽게 코딩할 수 있다.  
+ 함수의 결과값이 제너레이터이다. -> 일회용 함수
+ for문과 조합시 인덱스값과 요소를 한 번에 받을 수 있다.
+ for 문에서 사용시 반복할 때마다 next()함수로 요소를 자동으로 꺼내준다.

```
ex_list = ["A","B","c"]

print(enumerate(ex_list)) # 출력 enumerate object at ~~
print(list(enumerate(ex_list))) # [(0,'A'),[1,'B'],(2,'C)]
for i, value in enumerate(ex_list):
    print("{}번째 요소는 {}".format(i,value))
```
<br>

## 4. 딕셔너리의 items()함수와 반복문 조합하기
---
딕셔너리는 items() 함수와 함께 사용하면 for i value in enumberate(리스트) 형태 처럼 키와 값을 조합해서 반복문을 쉽게 만들 수 있다.   
```
ex_dic = {
    "키A":"값A",
    "키B":"값B",
    "키C":"값C" 
}

for key, value in ex_dic.items():
    print("ex_dic[{}] = {}".format(key,value))
```
<br>

## 5. 리스트 내포
---
반복문을 사용해 리스트를 재조합 하는 경우 사용한다.  
```
기본 형태
리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]

# 예시
arr = [i for i in range(0,20)] # 0 ~ 19 까지 리스트
arr = [2 for i in range(0,20)] # 2를 20개 요소로 
--------------------------------------------------

응용 if문 추가
리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]

# 예시 1
arr = ["사과","자두","바나나","초콜릿","체리"]
output = [fruit for fruit in arr if fruit != "초콜릿"]
# 초콜릿을 제외하고 리스트 재조합

print(output) # 출력 ['사과','자두','바나나','체리']

# 예시 2
arr = [i for i in range(0,20) if i % 2 == 0]
# 2의 배수만 리스트 요소로 저장
```
<br>

## 6. 구문 내부에 여러 줄 문자열을 사용했을 때의 문제점
---
__문제점__  
```
number = int(input())

if number % 2 == 0 :
    print("""\
        입력한 문자열은 {}
        {} 는 짝수""".format(number,number)
    )
else :
   print("""\
        입력한 문자열은 {}
        {} 는 홀수""".format(number,number)
    )

# 출력시 예싱치 못한 들여쓰기가 발생한다.
# \ 를 지우고 사용시 이상한 구조를 가지게 되고
# 한 줄로 입력시 너무 길다.
```
__해결책__  
+ 괄호 내부에 문자열을 여러개 입력시 모든 문자열을 합친 새로운 문자열 형성
    - 따옴표("") 를 사용하고 사이에 쉼표는 없이!
    - 줄바꿈 (\n) 사용
+ join() 함수 사용

__괄호 예시__  
```
number = int(input())

if number % 2 == 0 :
    print((
        "입력한 문자열은 {}\n"
        "{} 는 짝수").format(number,number)
    )
else :
   print((
        "입력한 문자열은 {}\n"
        "{} 는 홀수").format(number,number)
    )
```

__join 예시__  
```
기본 형태
문자열.join(문자열로 구성된 리스트)
join 앞에 문자열이 리스트 요소 사이마다 들어간다.

number = int(input())

if number % 2 == 0 :
    print("\n".join([
        "입력한 문자열은 {}",
        "{}는 짝수"
    ]).format(number,number))
else :
   print("\n".join([
        "입력한 문자열은 {}",
        "{}는 홀수"
    ]).format(number,number))
```
<br>

## 7. 진수변환과 count() 함수
---
### 진수 변환
+ \{:b}  # 2진수 변환
+ \{:o}  # 8진수 변환
+ \{:x}  # 16진수 변환
+ int("n진수의 값", n) # n진수를 10진수로 변환

2,8,16 진수 변환시 문자열로 반환된다.  

__변환시 따옴표가 있다면 문자열 자료형!!__  
```
print("{:b}".format(10)) # '1010' -> 문자열 자료형
print(int ("1010",2)) # 10
```

### count() 함수
반복 가능한 객체(문자열, 리스트, 범위 등)의 count 함수 사용법은 아래와 같다.
```
기본 형태
객체.count()

예시
"안녕안녕하세요".count("안") # 2
```
<br>

__문제 : 1~100 사이에 2진수로 변환했을때 0이 하나만 포함된 숫자를 찾고, 그 합을 구하시오.__  
```
# 진수 변환시 문자열로 반환되므로 count 매개변수도 문자열이어야 한다. " "
output = [i for i in range(1,101) if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i,"{:b}".format(i)))
print("합계 = {}".format(sum(output)))
```

---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__