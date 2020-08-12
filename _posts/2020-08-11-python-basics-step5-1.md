---
layout: post
title:  파이썬 파트 5-1. 함수 만들기 및 활용
subtitle:   파이썬 파트 5-1. 함수 만들기 및 활용
categories: python
tags: basics book python 
comments: true
# header-img:
---
+ __목차__
  - [1. 함수의 기본](#1-함수의-기본)
  - [2. 가변 매개변수](#2-가변-매개변수)
  - [3. 기본 매개변수](#3-기본-매개변수)
  - [4. 리턴](#4-리턴)
  - [5. 재귀 함수](#5-재귀-함수)
  - [6. 재귀 함수의 문제 해결: 메모화](#6-재귀-함수의-문제-해결-메모화)
  - [7. global 키워드](#7-global-키워드)


## 1. 함수의 기본
---
함수는 한마디로 '코드의 집합'이다.
```
기본 형태
def 함수 이름(매개변수, 매개변수,..) : # 매개변수가 없어도 무관
    문장

# 예시
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("hello",5) 
```
cf) 함수 생성시 매개변수를 만들었는데 함수 호출시 매개변수를 넣지 않거나 더 많이 넣으면 TypeError 예외 발생  
<br>

## 2. 가변 매개변수
---
print() 함수와 같이 매개변수를 원하는 만큼 받을 수 있는 함수를 가변 매개변수라고 부른다.  
+ 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
+ 가변 매개변수는 하나만 사용할 수 있다.
+ 가변 매개변수는 리스트처럼 사용하면 된다.

```
기본 형태
def 함수 이름(매개변수,매개변수,....,*가변 매개변수) :
    문장

예시
def print_n_times(n,*values):
    for i in range(n):
        for value in values:
            print(value)

print_n_times(3,"hello","world","python")

# 출력
hello
world
python
```
<br>

## 3. 기본 매개변수
---
print 함수의 자동 완성 기능으로 나오는 설명을 보면  
```
print(value,..., sep='', end='\n', file=sys.stdout, flush=False)
```
가장 앞에 있는 value가 가변 매개변수이다. 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다. 그런데 특이하게 '매개변수 = 값' 형태로 되어있다. 이는 기본 매개변수라고 하며, 매개변수를 입력하지 않았을 경우 매개변수에 자동으로 들어가는 기본값이다. 기본 매개변수 뒤에는 일반 매개변수가 올 수 없다는 제약이 있다. 따라서 매개변수 순서가 틀리면 TypeError가 발생하니 아래와 같은 형식을 기억해두자.  
```
def 함수(일반 매개변수, 일반 매개변수, 가변 매개변수, 기본 매개변수, 기본 매개변수, ...) # 일반적인 순서를 기억
def 함수(일반 매개변수, 일반 매개변수, 기본 매개변수 , 가변 매개변수) 

예시
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("hello")

# 출력
hello
hello

예시 : 기본 매개변수 변경1
while True:
    print(".",end="") # 원래 end="\n" 이라 줄바꿈이 일어나는데 빈 문자열로 바꿔 일어나지 않음

예시 : 기본 매개변수 변경2 : 기본 매개변수값에 덮어씌워진다.
def test(a, b=10, c=100):
    print(a+b+c)

test(10,20,30) # 기본 형태 순서대로 대입된다. a=10, b=20, c=30
test(a=10,b=100,c=100) # 매개변수로 대입값을 지정
test(c=10,a=100,b=200) # 입력 순서 상관없이 지정
test(10,c=200) # a=10 b=10 c=200
test(10,"hello",300) # a=10 b="hello" c=300
```
<br>

## 4. 리턴
---
값을 반환하는 함수의 결과값을 리턴값이라고 한다. 리턴값이 있으면 리턴값을 반환하면 리턴값 없이 리턴만 있으면 None을 반환
```
def return_test():
    return 100 # 100이 없다면 None이 반환

value = return_test()
print(value) # 100
```
<br>

## 5. 재귀 함수
---
재귀적 구현을 파고 들면 끝도 없다. 어떤 함수를 만들 것이라는 의미를 정한 뒤 그 함수를 만들고 그 안에 다시 호출하면 그 기능을 하겠지라고 생각하고 사고를 끝내야한다.  
### 팩토리얼
```
def fac(n):
    if n ==1 :
        return 1
    return n * fac(n-1)

print(fac(5)) # 120
```
<br>

## 6. 재귀 함수의 문제 해결: 메모화
---
재귀 함수는 상황에 따라 같은 것을 기하급수적으로 많이 반복하는 문제가 발생한다. 이 문제를 해결하기 위해 메모화라는 기술을 사용한다.  
```
# 처리가 오래 걸리는 피보나치 수열
def fibo(n) :
    if n==1 or n== 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(5))

# 문제를 해결한 피보나치 수열
dic = {1:1, 2:1}
def fibo(n) :
    if n in dic:
        return dic[n]
    output = fibo(n-1) + fibo(n-2)
    dic[n] = output
    return output

print(fibo(5))
```
처리가 오래 걸리는 피보나치 수열의 재귀 함수에서는 한 번 구했던 값이라도 처음부터 다시 계산을 하면서 계산 횟수가 기하급수적으로 많아진다. 메모화를 사용해서 했던 계산결과를 딕셔너리에 저장할 경우 했던 계산들은 바로 꺼내서 결과값으로 사용할 수 있다. 따라서 처리 속도가 매우 빨라진다.  
<br>

## 7. global 키워드
---
```
counter =0
def fibo(n):
    counter +=1 
    if n==1 or n==2 :
        return 1
    return fibo(n-1)+ fibo(n-2)

print(fibo(5))

# 오류 해결
counter =0
def fibo(n):
    global counter  # 전역변수 counter을 수정하겠다.
    counter +=1
    if n==1 or n==2 :
        return 1
    return fibo(n-1)+ fibo(n-2)

print(fibo(5))
```
재귀의 횟수를 알아보기 위해 작성한 위 코드를 실행하면 함수안의 counter 에서 밑줄이 표시되면서 Undefined variable 이라고 표시된다. 함수 내에서 전역변수를 사용할 수는 있지만 전역변수를 그냥 수정할 수는 없다. 이를 수정하게 할 수 있도록 해주는 것이 global 키워드이다. 즉, 전역변수를 함수 내에서 수정하기 위해서는 `global 변수명` 을 사용해야 한다.  
참고로 레퍼런스를 나타내는 자료형같은 경우에는 global을 안써도 된다. (딕셔너리 등등) -> 잘 모르겠으면 일단 실행해보고 오류가 나오면 global을 사용한다.  

__문제 : 재귀 함수를 이용해서 리스트를 평탄화 하는 함수 만들기__  
```
def flatten(data) :
    output =[]
    for i in data:
        if type(i) == list:
            output += flatten(i)
        else :
            output +=[i]
            # output.append(i)
    return output

ex = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:",ex)
print("수정:",flatten(ex))
```
<br>

__문제 : 한 개의 테이블에 앉을 수 있는 최대 사람수는 10명, 최소는 2명일때 100명의 사람이 하나 이상의 테이블에 나누어 앉는 패턴을 구하시오__  
```
## 메모화 이전의 풀이
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람수 = 100
count =0

def fuc(남은사람수, 앉힌사람수):
    global count
    #탈출조건
    if 남은사람수 == 0 :
        count +=1
        return 
    if 남은사람수 < 0 : # 1 인경우는 다음 트리로 넘어가면서 0 보다 작은 상태로 넘어감
        return
    # 재귀함수

    for i in range(앉힌사람수,앉힐수있는최대사람수 +1):
        fuc(남은사람수-i,i)
    return count

print(fuc(전체사람수,앉힐수있는최소사람수))

# 메모화 풀이
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람수 = 100
memo = {} # 메모화 딕셔너리

def fuc(남은사람수, 앉힌사람수):
    # 다음과 같은 매개인자가 들어왔을때 메모에 있으면 꺼내쓰기 위해
    key =str([남은사람수, 앉힌사람수]) 

    #탈출조건
    if key in memo :
        return memo[key]
    if 남은사람수 == 0 :
        return 1
    if 남은사람수 < 0 : # 1 인경우는 다음 트리로 넘어가면서 0 보다 작은 상태로 넘어감
        return 0

    # 재귀함수
    count = 0
    for i in range(앉힌사람수,앉힐수있는최대사람수 +1):
        count += fuc(남은사람수-i,i)
    
    # 메모화
    memo[key] = count

    return count

print(fuc(전체사람수,앉힐수있는최소사람수))
```



---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__