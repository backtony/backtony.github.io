---
layout: post
title:  파이썬 자료구조 8-2장. 원형 이중 연결 리스트
subtitle:   파이썬 자료구조 8-2장. 원형 이중 연결 리스트
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 원형 리스트](#1-원형-리스트)
  - [2. 이중 연결 리스트](#2-이중-연결-리스트)
  - [3. 원형 이중 연결 리스트](#3-원형-이중-연결-리스트)

## 1. 원형 리스트
---
원형 리스트는 연결 리스트의 꼬리 노드가 다시 머리 노드를 가리키는 모양으로 고리 모양의 늘어선 데이터를 표현하는데 알맞은 리스트 구조이다.  
<br>

## 2. 이중 연결 리스트
---
연결 리스트의 가장 큰 단점은 뒤쪽 노드를 찾기 쉬운 반면 앞쪽 노드를 찾기 어렵다는 것이다. 이 단점을 개선한 리스트 구조가 이중 연결 리스트이다. 각 노드에는 뒤쪽 노드에 대한 포인터뿐만 아니라 앞쪽 노드에 대한 포인터가 주어진다.  
<br>

## 3. 원형 이중 연결 리스트
---
위의 두 가지 내용을 합친 것이 원형 이중 연결 리스트이다.  

### 클래스와 함수
+ Node 클래스 : data, next, prev로 구성
+ DoubleLinkedList 클래스 : no, head , current 필드로 구성
    - no : 리스트 노드 개수
    - head : 머리 노드 참조
    - current : 주목 노드 참조
+ is_empty() 함수 : 리스트가 비어 있는지(더미 노드만 존재하는지)검사
+ search() 함수 : 인수로 주어진 데이터와 값이 같은 노드를 선형 검색
+ print_current_nod() 함수 : 주목 노드의 데이터를 출력
+ print() 함수 : 모든 노드를 출력
+ print_reverse() 함수 : 리스트에 있는 모든 노드를 맨 끝부터 역순으로 출력
+ next() 함수 : 주목 노드를 한 칸 뒤로 이동
+ prev() 함수 : 주목 노드를 한 칸 앞으로 이동
+ add() 함수 : 노드 삽입
+ add_first() 함수 : 리스트의 맨 앞에 노드 삽입
+ add_last() 함수 : 리스트의 맨 끝에 노드 삽입
+ remove_current_node() 함수 : 주목 노드 삭제
+ remove() 함수 : 임의의 노드 삭제
+ remove_first() 함수 : 머리 노드를 삭제
+ remove_last() 함수 : 꼬리 노드를 삭제
+ clear() 함수 : 모든 노드 삭제

### 구현하기
```
# module.py
class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.next = next or self # next가 None이면 self를 참조
        self.prev = prev or self # prev도 마찬가지이고 이는 더미 노드를 위함
class DoubleLinkedList:
    def __init__(self):
        self.head = self.current = Node()
        self.no = 0
    def __len__(self):
        return self.no
    def is_empty(self):
        return self.head is self.head.next
    def search(self,data):
        cnt =0
        ptr = self.head.next # 더미노드를 지나서가 시작 노드
        while ptr is not self.head:
            if ptr.data == data:
                self.current=ptr
                return cnt
            cnt+=1
            ptr = ptr.next
        return -1
    def __contains__(self,data):
        return self.search(data)>=0
    def print_current_node(self):
        if self.is_empty():
            print("주목 노드가 없다")
        else :
            print(self.current.data)
    def print(self):
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next
    def print_reverse(self):
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev
    def next(self):
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True
    def prev(self):
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True
    
    # 삭제와 추가 모두 current를 사용하여 먼저 구현하고 이를 활용해서 first,last구현

    def add(self,data): # 주목노드 바로 뒤에 삽입
        node = Node(data,self.current,self.current.next)
        self.current.next.prev= node
        self.current.next = node
        # self.current.next = self.current.next.prev = node 하면 
        # self.current.next = node 실행후 self.current.next.prev가 실행되서 꼬인다.
        self.current = node
        self.no+=1
    # add 함수를 활용하여 current만 수정해서 first와 last의 add 쉽게 가능
    def add_first(self,data):
        self.current=self.head
        self.add(data)
    def add_last(self,data):        
        self.current=self.head.prev
        self.add(data)
    
    def remove_current_node(self):
        if not self.is_empty():            
            self.current.prev.next=self.current.next
            self.current.next.prev=self.current.prev
            self.current = self.current.prev
            self.no-=1
            # 수정한 current가 head면 current를 앞으로 이동
            if self.current is self.head:
                self.current = self.head.next
    def remove(self,p): # p는 노드
        ptr = self.head.next
        while ptr is not self.head:
            if ptr is p:
                self.current=ptr
                self.remove_current_node()
                break
            ptr = ptr.next
    def remove_first(self):
        self.current=self.head.next
        self.remove_current_node()
    def remove_last(self):
        self.current=self.head.prev
        self.remove_current_node()    
    def clear(self):
        while not self.is_empty():
            self.remove_first()
        self.no=0

    def __iter__(self):
        return DoubleLinkedListIterator(self.head)
    def __reversed__(self):
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    def __init__(self,head):
        self.head =head
        self.current = head.next
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        else :
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    def __init__(self,head):
        self.head=head
        self.current=head.prev
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        else :
            data = self.current.data
            self.current=self.current.prev
            return data   

# main.py
from enum import Enum
from module import DoubleLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입',
                     '머리노드삭제', '꼬리노드삭제', '주목노드출력',
                     '주목노드이동', '주목노드역순이동', '주목노드삭제',
                     '모든노드삭제', '검색', '멤버십판단', '모든노드출력',
                     '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList()  # 원형・이중 연결 리스트 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.주목노드바로뒤삽입:  # 주목 노드 바로 뒤에 삽입
        lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요 : ')))

    elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:  # 주목 노드 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드역순이동:  # 주목 노드를 한 칸 앞으로 이동
        lst.prev()

    elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:  # 모두 삭제
        lst.clear()

    elif menu == Menu.검색:  # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:  # 멤버십 판단
        print('그 값의 데이터는 포함되어'
              +(' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:  # 모든 노드를 출력
        lst.print()

    elif menu == Menu.모든노드역순출력:  # 모든 노드 역순 출력
        lst.print_reverse()

    elif menu == Menu.모든노드스캔:  # 모든 노드 스캔
        for e in lst:
             print(e)

    elif menu == Menu.모든노드역순스캔:  # 모든 노드 역순 스캔
        for e in reversed(lst):
             print(e)

    else:  # 종료
        break
```
__cf) 파이썬 대입__  
C, Java 등의 언어에서 대입 연산자 '='는 오른쪽 결합 연산자이다.
```
C와 Java 에서는 a=b=1 의 경우 
b=1
a=1 
이렇게 실행 된다.

하지만 파이썬에서는 다르다.
a=b=1 의 경우
a=1
b=1 
순서로 실행된다. 
```






<br>

  
---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__