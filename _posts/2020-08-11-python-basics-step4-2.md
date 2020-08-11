---
layout: post
title:  파이썬 파트 4-2. 딕셔너리와 반복문
subtitle:   파이썬 파트 4-2. 딕셔너리와 반복문
categories: python
tags: basics book python 
comments: true
# header-img:
---
+ __목차__
  - [1. 딕셔너리 선언하기](#1-딕셔너리-선언하기)
  - [2. 딕셔너리의 요소에 접근하기](#2-딕셔너리의-요소에-접근하기)
  - [3. 딕셔너리에 값 추가하기/제거하기](#3-딕셔너리에-값-추가하기제거하기)
  - [4. 딕셔너리 내부에 키가 있는지 확인하기: in](#4-딕셔너리-내부에-키가-있는지-확인하기-in)
  - [5. get() 함수](#5-get-함수)
  - [6. for 반복문: 딕셔너리와 함께 사용하기](#6-for-반복문-딕셔너리와-함께-사용하기)

## 1. 딕셔너리 선언하기
---
```
기본 형태
변수 = {
    키:값,
    키:값,
    ...
    키:값
}

예시
dict_a = {
    "name" : "어밴저스",
    "type" : "히어로 무비"
}
```
+ 딕셔너리는 중괄호{}로 선언하며, 키:값 형태를 쉼표로 연결해서 만든다. 
+ 키는 문자열, 숫자, 불 등으로 선언할 수 있으나 일반적으로 문자열을 사용한다.
+ __선언할 때만 중괄호{} 를 사용하고 참조, 추가, 제거시에는 []를 사용한다.__

<br>

## 2. 딕셔너리의 요소에 접근하기
---
```
dict_a = {
    "name" : "어밴저스",
    "type" : "히어로 무비"
}
print(dict_a["name"])

# 출력
어밴저스

dict_b = {
    "director" : ["안소니 루소","조 루소"],
    "cast" : ["아이언맨","타노스","토르"]
}

print(dict_b)
# 출력
{'director':['안소니 루소','조 루소'], 'cast':['아이언맨','타노스','토르']}

print(dict_b["director"])

#출력
['안소니 루소','조 루소']
```
+ 리스트와 딕셔너리도 하나의 자료이므로, 리스트와 딕셔너리를 값으로 넣을 수 있다.  
+ 키안에 값이 하나일 경우 '' 작은 따옴표 없이 출력되고 값이 여러개면 ''작은 따옴표도 같이 출력된다.  

__cf) 딕셔너리 문자열 키와 관련된 실수__  
```
dict_k = {
    name : "망고",
    type : "당"
}
```
name이라는 이름이 정의되지 않아서 오류가 생긴다. 파이썬 딕셔너리의 키에 단순한 식별자를 입력하면 이를 변수로 인식합니다. 오류 해결을 원하면 dict_k 이전에 name = "이름" 같이 미리 선언을 해줘야 한다. 하지만 미리 선언하고 dict을 이용하는 경우는 드물기 때문에 dict 안에서 반드시 따옴표를 붙여주는게 좋다. type은 type()함수라는 기본 식별자가 있기에 이것이 키로 들어가 오류가 발생하지 않는다.  

<br>

## 3. 딕셔너리에 값 추가하기/제거하기
---
```
기본 형태
딕셔너리[새로운 키] = 새로운값

dict_k = {
    "name" : "망고",
    "type" : "당"
}
dict_k["price"] = 5000 # 마지막 위치에 price 키 추가
dict_k["name"] = "딸기" # 기존의 값을 새로운 값으로 대체
del dic_k["name"] # name 키와 값 삭제
```

__keyError 예외__  
리스트의 길이를 넘는 인덱스 접근시 IndexError가 발생하듯이 딕셔너리도 존재하지 않는 키에 접근하면 KeyError가 발생한다.  
<br>

## 4. 딕셔너리 내부에 키가 있는지 확인하기: in
---
리스트 내부에 값이 있는지 없는지 확인하기 위해 in 키워드를 사용했던 것처럼 딕셔너리도 in 키워드를 사용한다.
```
dict_k = {
    "name" : "망고",
    "type" : "당"
}

key = input("접근하고자 하는 키: ")

if key in dict_k:
    print(dict_k[key])
else :
    print("No")
```
<br>

## 5. get() 함수
---
딕셔너리 키로 값을 추출하는 기능으로 딕서녀리[키]를 입력할 때와 같은 기능을 수행하지만, 존재하지 않는 키에 접근할 경우 KeyError가 아닌 None 을 출력한다.  
```
dict_k = {
    "name" : "망고",
    "type" : "당"
}

value = dict_k.get("what")
print(value)

# 출력
none
```
<br>

## 6. for 반복문: 딕셔너리와 함께 사용하기
---
```
기본 형태
for 변수 in 딕셔너리 :
    코드

dict_k = {
    "name" : "망고",
    "type" : "당"
}
for key in dict_k:
    print(dict_k[key])

# 출력
망고
당
```
주의할 점은 딕셔너리 내부에 있는 키가 변수에 들어간다는 것이다.  
<br>

__문제 : 딕셔너리 안의 값을 출력하기__  
```
character = {
    "name":"기사",
    "level" : 12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) == list:
        for j in character[key]:
            print("{} : {}".format(key,j))
    elif type(character[key]) == dict:
        for i in character[key]:
            print("{} : {}".format(i,character[key][i]))
    else:
        print("{} : {}".format(key,character[key]))
    
```


---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__