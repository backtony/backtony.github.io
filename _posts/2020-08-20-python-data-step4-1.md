---
layout: post
title:  파이썬 자료구조 4-1장. 스택
subtitle:   파이썬 자료구조 4-1장. 스택
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 스택](#1-스택)
  - [2. collections.deque로 스택 구현하기](#2-collectionsdeque로-스택-구현하기)
  
  
## 1. 스택
---
스택은 데이터를 임시 저장할 때 사용하는 자료구조로, 데이터의 입력과 출력 순서는 후입선출 방식이다.

### 구현하기
+ 스택 배열(stk) : 푸시한 데이터를 저장하는 스택 본체인 list형 배열이다.
+ 스택 크기(capacity) : 스택의 최대 크기를 나타내는 int형 정수, len(stk)와 같다
+ 스택 포인터(ptr) : 스택에 쌓여있는 데이터의 개수를 나타내는 정수값
+ 예외 처리 클래스 Empty : 스택이 비어있으면 내보내는 예외 처리
+ 예외 처리 클래스 Full : 스택이 가득차있으면 보내는 예외 처리
+ \_\_init\_\_ 함수 : 스택 배열을 생성하는 등 준비작업
+ \_\_len\_\_ 함수 : 스택에 쌓여 있는 데이터 개수
+ is_empty 함수 : 스택이 비어 있는지 판단
+ is_full 함수 : 스택이 가득 차 있는지 판단

```
# module.py
class FixedStack :

    # 아래 설명 참조
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    # 고정 길이 스택 클래스
    def __init__(self,capacity=256):
        self.capacity = capacity
        self.stk = [None] * capacity
        self.ptr = 0 # 스택 포인터

    def __len__(self):
        return self.ptr

    # 혹시 모를 프로그램 오류를 대비해서 ==이 아닌 <= >= 를 사용
    def is_full(self):
        return len(self.stk) >= self.capacity
    def is_empty(self):
        return self.ptr <=0 

    def push(self,value):
        if self.is_full():
            raise FixedStack.Full
        # ptr을 인덱스로도 사용하기 위해서 먼저 대입하고 갯수 추가
        self.stk[self.ptr] = value
        self.ptr +=1
    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        # 현재 ptr 인덱스 위치는 비어있으므로 
        self.ptr -=1 
        return self.stk[self.ptr]
    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    def clear(self):
        self.ptr = 0
        # 배열에 데이터가 존재해도 ptr이 0이면 데이터가 추가될때 다 덮어씌워지므로
        # ptr만 0으로 수정해도 전체 데이터 삭제 효과가 남
    
    def find(self,value):
        for i in range(self.ptr):
            if self.stk[i] == value:
                return i # 검색 성공
        return -1 # 실패
    def count(self,value):
        c=0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c+=1
        return c
    def __contains__(self,value):
        return self.count(value)
    def dump(self):
        if self.is_empty():
            raise FixedStack.Empty
        print(self.stk[:self.ptr])

# main.py
from module import FixedStack
from enum import Enum

Menu = Enum('Menu',"푸시 팝 피크 검색 덤프 종료")

def select_menu():
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True :
        
        print(*s,sep="  ",end=" ")
        n = int(input(": "))
        if 1<= n <= len(Menu):
            return Menu(n)
    
s = FixedStack(64)

while True :
    print(f"현재 데이터 개수: {len(s)} / {s.capacity}")
    menu = select_menu()

    if menu == Menu.푸시 :        
        value = input("value : ")        
        # push 함수에 경우에 따라 예외가 발생하도록 처리했다.
        # 따라서 함수 호출과정에서 예외가 발생시 이를 구분하기 위해서
        # try except를 사용
        try :
            s.push(value)
        except FixedStack.Full: 
            print("가득 차 있다.")
    
    elif menu == Menu.팝 :                     
        try :
            x= s.pop() 
            print(f"pop 데이터 : {x}")
        except FixedStack.Empty:
            print("비어있다.")

    elif menu == Menu.피크 :        
        try :
            x= s.peek()
            print(f"peek 데이터 : {x}")
        except FixedStack.Empty:
            print("비어있다.")


    elif menu == Menu.검색 :        
        value = input("value : ")
        # s.__contains__(value) 대신 value in s 사용
        # 자세한 내용은 아래 설명 참조
        if value in s: 
            print(f"{s.count(value)}개가 있고 맨 앞 인덱스는 {s.find(value)} ")
        else :
            print("찾을 수 없다")
    
    elif menu == Menu.덤프 :        
        s.dump()
    
    else :
        break 
```
push, pop, peek 함수는 경우에 따라 예외가 발생하도록 함수를 구현했다. 따라서 함수를 사용할 때 예외가 발생할 때와 발생하지 않을 때를 구분해서 코딩해야 한다.  
<br>

__cf) \_\_len\_\_() 함수__  
클래스에 \_\_len\_\_()함수를 정의하면 클래스형 인스턴스를 \_\_len\_\_()함수에 전달할 수 있다. 예를 들어 클래스형의 인스턴스 obj에 대한 \_\_len\_\_함수를 호출하는 obj.\_\_len\_\_()를 간단하게 len(obj)로 사용이 가능하다. 따라서 인스턴스 맴버를 리턴값으로 사용할 수 있다.   

<br>

__cf) len와 \_\_len\_\_의 차이__  
\_\_len\_\_() 함수는 클래스 내에 재정의되는 매직 멤버 함수로 내장 함수 len()에 의해 자동으로 호출된다. 두 함수의 차이는 len() 함수의 경우 \_\_len\_\_() 함수를 호출하여 그 값이 정수일 경우만 처리하며 그렇지 않으면 예외가 발생한다.  

<br>

__cf)\_\_contains\_\_ 함수 알아보기__  
클래스에 \_\_contains\_\_() 함수를 정의하면 클래스형의 인스턴스에 멤버십 판단 연산자인 in을 적용할 수 있다. 예를 들어 클래스형의 인스턴스 obj에 대한 \_\_contains\_\_()함수를 호출하는 obj.\_\_contains\_\_(x) 를 더 간단하게 x in obj로 작성할 수 있다.  
<br>

__cf) raise문을 통한 예외 처리__  
ValueError 클래스, ZeroDivisionError 클래스 등 파이썬이 제공하는 예외 처리를 표준 내장 예외처리라고 한다. 표준 내장 예외 처리는 BaseException 클래스와 직간접적으로 파생한 클래스로 제공된다.  
프로그래머가 정의하는 사용자 정의 예외 처리는 BaseException 클래스가 아니라 Exception클래스(또는 그 파생 클래스)에서 파생하는 것이 원칙이다. 왜냐하면 BaseException 클래스는 사용자 정의 클래스가 파생하는 것을 전제로 하기 때문이다.
<br>

## 2. collections.deque로 스택 구현하기
---
파이썬의 내장 컨테이너는 딕셔너리, 리스트, 집합 , 튜플이 있다. 이 외에도 여러 컨테이너를 collections 모듈로 제공한다. 주요 컨테이너는 namedtuple(), deque, ChainMap, Counter, OrderedDict, defaultdic, UserList, UserString 같은 컬랙션 이다. 이 가운데 deque 모듈을 사용하면 스택을 간단히 구현할 수 있다. deque는 맨 앞과 맨 끝 양쪽에서 원소를 추가, 삭제하는 자료구조인 덱을 구현하는 컨테이너이다.  

### 속성과 함수
+ maxlen 속성 : deque의 최대 크기를 나타내는 속성, 크기 제한이 없으면 None
+ append(x) 함수 : deque의 맨 끝(오른쪽)에 x를 추가
+ appendleft(x) 함수 : dequed의 맨 앞(왼쪽)에 x를 추가
+ clear() 함수 : deque의 모든 원소를 삭제하고 크기를 0으로
+ copy() 함수 : deque의 얕은 복사
+ count(x) 함수 : deque 안에 있는 x와 같은 원소의 개수를 계산
+ extend(iterable) 함수 : 순차 반복 인수 iterable에서 가져온 원소를 deque 맨 끝(오른쪽) 에 추가하여 확장
+ extendleft(iterable) 함수 : 순차 반복 인수 iterable에서 가져온 원소를 deque의 맨 앞(왼쪽)에 추가하여 확장
+ index(x[, start [, stop]]) 함수 : start부터 stop-1 까지 범위에서 가장 앞쪽에 있는 원소의 위치를 반환, 없다면 ValueError
+ insert(i,x) 함수 : x를 deque의 i 위치에 삽입, 크기 제한 deque일 경우 maxlen 초과한 삽입은 IndexError 
+ pop() 함수 : deque의 맨 끝(오른쪽)에 있는 원소 1개를 삭제하고 반환, 비어있는 경우 IndexError 
+ popleft() 함수 : deque의 맨 앞(왼쪽)에 있는 원소 1개 삭제하고 반환, 비어있는 경우 IndexError 
+ remove(value) 함수 : value의 첫 번째 항목을 삭제, 없는 경우 ValueError
+ reverse() 함수 : deque 원소를 역순으로 재정렬하고 None 반환
+ rotate(n=1) 함수 : deque의 모든 원소를 n값만큼 오른쪽으로 밀어낸다. n이 음수라면 왼쪽으로

양쪽 끝의 데이터를 인덱스로 접근하는 것은 O(1)로 빠르지만, 가운데 부분에 있는 데이터를 접근하는 것은 O(n)으로 느리다. 그러므로 인덱스를 사용하여 임의의 원소를 무작위로 접근하는 것은 비효율적이라는 것을 알아두자.  

### 구현
```
from collections import deque

#  class collections.deque([iterable[, maxlen]]
class Stack:
    def __init__(self,maxlen=256):
        self.capacity= maxlen
        self.__stk = deque([],maxlen)
    
    def __len__(self):
        return len(self.__stk)
    
    def is_empty(self):
        # 논리 연산자 not으로 인해 비어있으면 False가 True
        # 들어있으면 True가 False
        return not self.__stk
    def is_full(self):
        return len(self.__stk) == self.__stk.maxlen
    def push(self,value):
        self.__stk.append(value)
    def pop(self):
        return self.__stk.pop()
    def peek(self):
        return self.__stk[-1]
    def clear(self):
        self.__stk.clear()
    # 찾고자 하는 값의 idx 찾기
    def find(self,value):
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1
    # 찾고자 하는 값 갯수 
    def count(self,value):
        return self.__stk.count(value)
    # 찾고자 하는 값이 들어 있는지
    def __contains__(self,value):
        return self.count(value)
    def dump(self):
        print(list(self.__stk)) # ['1','2','3'] 출력
        # print(self.__stk) 코딩시
        # deque(['1','2','3'], maxlen=64) 출력    
```



---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__



