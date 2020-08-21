---
layout: post
title:  파이썬 자료구조 4-2장. 큐
subtitle:   파이썬 자료구조 4-2장. 큐
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 큐 알아보기](#1-큐-알아보기)
  - [2. 배열로 큐 구현하기](#2-배열로-큐-구현하기)
  - [3. 링 버퍼로 큐 구현하기](#3-링-버퍼로-큐-구현하기)
  - [4. 구현하기](#4-구현하기)
  - [5. 링 버퍼의 활용](#5-링-버퍼의-활용)
    
  
## 1. 큐 알아보기
---
큐는 가장 먼저 넣은 데이터를 가장 먼저 꺼내는 선입선출 구조이다. 예들 들어 은행 창구에서 차례를 기다리거나 마트에서 계산을 기다리는 줄을 생각하면 된다. 큐에 데이터를 추가하는 작업은 인큐, 데이터를 꺼내는 작업은 디큐, 데이터를 꺼내는 쪽을 프런트, 데이터를 넣는 쪽을 리어라고 한다.  
<br>

## 2. 배열로 큐 구현하기
---
배열로 큐를 구현하다 보면 디큐이후 모든 원소를 한 칸씩 앞으로 당겨와야하는 문제가 생긴다. 이때 처리 복잡도는 O(n) 이므로 효율적이지 못하다.  
<br>

## 3. 링 버퍼로 큐 구현하기
---
디큐할 때 배열 안의 원소를 옮기지 않는 큐를 구현할 때 사용하는 자료구조가 링 버퍼이다. 배열 맨 끝의 원소 뒤에 맨 앞의 원소가 연결되는 자료구조이다. 어떤 원소가 맨 앞이고 맨 끝인지 식별하는 변수가 front와 rear이다. 따라서 원소를 옮길 필요가 없어지므로 처리 복잡도가 O(1)이 되므로 효율적이다. 
<br>

## 4. 구현하기
---
+ \_\_init\_\_() 함수 : 큐 배열을 생성하는 등의 준비작업
  - que : 큐 배열로서 밀어 넣는 데이터를 저장하는 list형 배열
  - capacity : 큐의 최대 크기를 나타내는 int형 정수
  - front : 맨 앞의 원소를 나타내는 인덱스
  - rear : 가장 마지막에 넣은 맨 끝 원소의 바로 다음 인덱스, 다음에 인큐할 때 데이터를 저장하는 원소의 인덱스
  - no : 큐에 쌓여 있는 데이터 개수를 나타내는 int형 정수, 가득차있는지 비어있는지 구별하기 위해 필요
+ \_\_len\_\_() 함수 : 큐에 추가한 데이터 개수 반환
+ is_empty() 함수 : 비어있는지 판단
+ is_full() 함수 : 가득 차 있는지 판단
+ enque() 함수 : 큐에 데이터를 인큐
+ deque() 함수 : 데이터를 디큐하여 그 값을 반환
+ peek() 함수 : 다음 디큐에서 꺼낼 데이터를 들여다본다.
+ find() 함수 : value와 같은 데이터가 포함되어 있는 위치 확인
+ count() 함수 : 큐에 있는 value의 갯수 반환
+ \_\_contains\_\_() 함수 : 큐에 value가 들어 있는지 판단
  - 실제 find 함수 사용할 때 찾기 전에 먼저 있는지 없는지 확인할때 사용
+ clear() 함수 : 큐 데이터 모두 삭제
+ dump() 함수 : 모든 데이터 출력

```
# module.py
class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    
    def __init__(self,capacity):
        self.capacity=capacity
        self.que = [None]*capacity
        self.front = 0
        self.rear = 0
        self.no = 0
    
    def __len__(self):
        return self.no

    def is_empty(self):
        return self.no<=0
    def is_full(self):
        return self.no>=self.capacity
    
    def enque(self,value):
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear]=value
        self.rear+=1
        self.no+=1
        if self.rear == self.capacity:
            self.rear =0
    
    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty
        x= self.que[self.front]
        self.front+=1
        self.no-=1
        if self.front == self.capacity:
            self.front =0
        return x
    
    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self,value):
        if self.is_empty():
            raise FixedQueue.Empty
        for i in range(self.no):
            if self.que[(i+self.front)%self.capacity]== value:
                return (i+self.front)%self.capacity
        return -1

    def count(self,value):
        c=0        
        for i in range(self.no):
            if self.que[(i+self.front)%self.capacity]== value:
                c+=1
        return c
    
    def __contains__(self,value):
        return self.count(value)
    
    # 인큐와 디큐는 no, front, rear값을 바탕으로 수행
    # 그러므로 값을 0으로만 하면 처음 상태로 돌아간 효과
    def clear(self):
        self.front=self.rear=self.no=0
    
    def dump(self):
        if self.is_empty():
            print("비어있다")
        else :
            for i in range(self.no):
                a = self.que[(self.front+i)%self.capacity]
                print(f"{a}",end =" ")
            print()
        
# main.py
from module import FixedQueue
from enum import Enum

# 첫 번째 인자는 열거형 이름
Menu = Enum('Menu',"인큐 디큐 피크 검색 덤프 종료")

def select_menu(): 
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s,sep="  ",end=" ")
        n = int(input(": "))
        if 1<=n<=len(Menu) :
            return Menu(n)
  
q = FixedQueue(64)
while True:
    print(f"현재 데이터 개수: {q.no}/{q.capacity}")
    menu = select_menu()
    
    if menu == Menu.인큐:
        value = int(input("인큐할 데이터 입력 : "))
        try:
            q.enque(value)
        except FixedQueue.Full:
            print("가득 찼다")

    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f"디큐한 데이터 : {x}")
        except FixedQueue.Empty:
            print("비어있다.")
    
    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f"피크한 데이터 : {x}")
        except FixedQueue.Empty:
            print("비어있다.")


    ## 일일이 찾지 말고 먼저 contain을 이용해서 안에 있는지 확인
    elif menu == Menu.검색:
        value = int(input("찾는 데이터 : "))
        if value in q:
            print(f"{q.count(value)}개의 {value}가 있고 맨 앞 idx : {q.find(value)}")
        else : 
            print("찾을 수 없다.")
    
    elif menu == Menu.덤프:
        q.dump()
    else : 
        break
```
<br>

## 5. 링 버퍼의 활용
---
링 버퍼는 오래된 데이터를 버리는 용도로 활용할 수 있다. 예를 들면 원소 수가 n인 배열에 데이터를 계속해서 입력할 때 가장 최근에 들어온 데이터 n개만 저장하고 나머지 오랜된 데이터는 버리는 경우이다.  
```
n = int(input("정수 몇 개 저장? : "))
a = [None] * n
cnt =0
while True:
    a[cnt%n] = int(input(f'{cnt+1}번째 정수를 입력 : '))
    cnt +=1

    retry = input('계속할까요? Y... Yes / N... No')
    if retry in ['N','n']:
        break

i = cnt - n
if i<0:
    i = 0
while i<cnt:
    # 배열인덱스와 몇 번째 입력 차이는 1
    # 2개 차이가 난다면 3번 째 값부터 저장되는데 
    # 3번째 값의 인덱스는 2
    print(f'{i+1}번 째 = {a[i%n]}')
    i+=1
```
<br>


---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
