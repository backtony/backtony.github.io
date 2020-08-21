---
layout: post
title:  파이썬 자료구조 5장. 재귀 알고리즘
subtitle:   파이썬 자료구조 5장. 재귀 알고리즘
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 재귀 알아보기](#1-재귀-알아보기)
  - [2. 팩토리얼](#2-팩토리얼)
  - [3. 유클리드 호제법](#3-유클리드-호제법)
  - [4. 재귀 알고리즘 분석](#4-재귀-알고리즘-분석)
  - [5. 하노이의 탑](#5-하노이의-탑)
  - [6. 8퀸 문제](#6-8퀸-문제)


## 1. 재귀 알아보기
---
자기 잔신을 포함하고 다시 자기 자신을 사용하여 정의되는 경우를 재귀라고 한다.  
+ 직접 재귀 : 자신과 똑같은 함수를 호출하는 방식
+ 간접 재귀 : 다른 함수를 통해 자신과 똑같은 함수를 호출하는 방식. a함수가 b를 호출하고 b 함수가 다시 a함수를 호출하는 구조
<br>

## 2. 팩토리얼
---
### 구현
```
def fac(n):
    if n <1:
        return 1
    else :
        return n * fac(n-1)

print(fac(3))
```

### math.factorial() 함수
파이썬에서는 팩토리얼값을 구하는 표준 라이브러리로 math 모듈에서 factorial 함수를 제공한다.
```
from math import factorial

print(factorial(3))
print(factorial(-1)) # 음수 전달시 ValueError 예외 처리
```
<br>

## 3. 유클리드 호제법
---
두 정수값의 최대 공약수를 재귀적으로 구하는 방법을 생각해보면 이 문제를 2개의 정숫값을 직사각형 두 변의 길이라고 생각하고 직사각형 안을 정사각형 여러 개로 가득 채워 나가면서 만들 수 있는 정사각형 가운데 가장 작은 정사각형의 변의 길이를 구하는 문제와 같다.
```
def gcd(x,y):    
    if y==0:
        return x
    else :
        gcd(y,x%y)
```
나머지 연산자 한 것을 y값에 넣었으므로 재귀로 들어오는 y값은 항상 x값보다 작다. 함수 시작 처음에 들어오는 값이 만약 y가 x보다 더 크더라도 재귀로 들어오는 인자 위치 x자리에 y값이 대입되므로 결국에는 인자로 들어오는 x값이 항상 y보다 크다.  

### math.gcd() 함수
파이썬에서 최대 공약수를 구하는 표준 라이브러리로 math 모듈에서 gcd() 함수를 제공한다.  
```
from math import gcd

print(gcd(22,8))
```
<br>

## 4. 재귀 알고리즘 분석
---
```
def recur(n):
  if n>0:
    recur(n-1)
    print(n)
    recur(n-2)

# 거꾸로는 recur (n-1) 과 n-2 위치만 바꾸면 된다.
```
위와 같이 재귀 호출을 여러 번 실행하는 함수를 순수한 재귀라고 한다.  

### 하양식 분석
__recur(4) 의 실행 과정__  
1. recur(3) 실행
2. 4를 출력
3. recur(2) 실행

트리처럼 줄줄이 그릴 수 있는데 가장 위쪽에 위치한 상자의 함수 호출부터 시작하여 계단식으로 자세히 조사해 나가는 분석 방법을 하양식 분석이라고 한다. 하지만 이 과정에서 recur(1)과 recur(2)를 여러 번 호출하게 되므로 효율적이라고는 할 수 없다.  

### 상향식 분석
하양식 분석과는 반대로 아래쪽부터 쌓아 올리며 분석하는 방법이다. recur 함수는 n이 양수일 때만 실행하므로 먼저 recur(1)이 어떻게 처리되는지 알아야 한다.  
__recur(1) 의 실행 과정__  
1. recur(0) 실행
2. 1을 출력
3. recur(-1) 실행

recur(1)을 실행하면 과정 1의 recur(0)과 과정 3의 recur(-1)은 출력할 내용이 없으므로 결국 과정 2의 1만 출력되는 것을 알 수 있다.

__recur(2) 의 실행 과정__  
1. recur(1) 실행 # 이미 위에서 구함.
2. 2을 출력
3. recur(0) 실행

recur(2)를 실행하면 과정 1에서 recur(1)은 출력하지만 과정 3의 recur(0)은 아무것도 출력하지 않는다. 따라서 과정 1,2를 거쳐 1과 2를 출력한다. 이 작업을 계속하면 최종 출력 recur(4)를 얻을 수 있다.  

### 재귀알고리즘의 비재귀적 표현
__1. 꼬리 재귀 제거하기__  
recur(n-2) 함수의 의미는 인수로 n-2의 값을 전달하고 recur 함수를 호출하는 것이다. 따라서 쉽게 제거할 수 있다.
```
def recur(n):
  while n>0:
    recur(n-1)
    print(n)
    n=n-2
```
__2. 재귀 제거하기__  
맨 앞의 재귀는 꼬리와 같이 제거할 수 없다. 왜냐하면 n의 값을 출력하기 전에 recur(n-1)을 실행햐아 하기 때문이다. 따라서 n의 값을 임시적으로 저장해줘야하는데 이때 스택을 이용한다.
```
from stack import Stack # stack.py에서 Stack클래스 임포트

def recur(n):
    s = Stack(n)

    while True:
        if n>0:
            s.push(n) # n-1실행전에 푸시
            n=n-1
            continue # n>0 이면 계속 반복
        if not s.is_empty():
            n = s.pop() # 꺼내고
            print(n) # 출력하고
            n=n-2 # recur(n-2)
            continue
        break

recur(3)
```
<br>

## 5. 하노이의 탑
---
[[하노이의 탑 이론](https://backtony.github.io/data/2020/07/28/data-theory-step2/#4-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%80%EC%9B%8C)] 를 참고하자.  

```
def tower(n,start,mid,to):
    if n>1: # 1개면 그냥 바로 옮기면 된다.
        tower(n-1,start,to,mid)
    
    print(f"{n}을 {to}로 옮겼다.")

    if n>1: # 1개면 애초에 재옮김을 할 필요가 없다. 바로 옮겨지므로
        tower(n-1,mid,start,to)

tower(3,1,2,3)
```
<br>

## 6. 8퀸 문제
---
8개의 퀸이 서로 공격하여 잡을 수 없도록 8 * 8 체스판에 배치하시오.  
__규칙__  
+ 각 열에 퀸을 1개만 배치
+ 각 행에 퀸을 1개만 배치
+ 각 대각선에 퀸을 1개만 배치
+ i열에 배치한 퀸의 위치가 j행에 있다면, pos[i] = j로 나타내자.
+ set()는 pos[i]에 0~7까지의 값을 차례로 대입하여 i열에 퀸을 1개만 배치하는 8가지 조합을 만드는 재귀 함수

```
# i는 열 j는 행

pos = [None] * 8
flag_a = [False] * 8 # 행 중복 확인
flag_b = [False] * 15 # 오른쪽 위쪽 방향 대각선
flag_c = [False] * 15 # 오른쪽 아래 방향 대각선

def put():
    print(*pos,sep="  ")

# 모형으로 보기
"""
def put():
    for i in range(8):
        for j in range(8):
            print('O' if pos[i] == j else 'X', end= " ")
        print()
    print()
"""

def set(i):
    for j in range(8):                       
        if flag_a[j] == flag_b[i+j] == flag_c[i-j+7] == False:
            pos[i] = j
            if i==7:
                put()
                return 
            # 마지막 i==7일때는 True로 안바꾸기 위해 뒤쪽에 작성
            flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True 
            
            # 일부만 생각해보면 다음 열이 7이되면 하나의 방법이 완성
            # 리턴으로 다시 6열로 돌아오고 False로 바꿔주면서 덮어씌움이 가능하게 바꿈
            set(i+1) 
            flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False
            # False로 바뀐후 for문이 돌아 다음 j행으로 이동되고 다른 방법을 형성
set(0)
```
<br>


---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__



