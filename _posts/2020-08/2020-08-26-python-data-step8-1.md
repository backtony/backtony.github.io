---
layout: post
title:  파이썬 자료구조 8-1장. 연결 리스트
subtitle:   파이썬 자료구조 8-1장. 연결 리스트
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 연결 리스트 알아보기](#1-연결-리스트-알아보기)
  - [2. 포인터를 이용한 연결 리스트](#2-포인터를-이용한-연결-리스트)
  - [3. 커서를 이용한 연결 리스트](#3-커서를-이용한-연결-리스트)
  


## 1. 연결 리스트 알아보기
---
구조가 단순한 리스트로 선형 리스트 또는 연결 리스트가 있다. 연결 리스트에서 각각의 원소를 노드라고 한다. 노드가 갖고 있는 것은 데이터와 뒤쪽 노드를 가리키는(참조하는) 포인터이다. 맨 앞에 있는 노드를 머리노드, 맨 끝에 있는 노드를 꼬리 노드라고 한다. 또 각 노드에서 바로 앞에 있는 노드를 앞쪽 노드, 바로 뒤에 있는 노드를 뒤쪽 노드라고 한다.  
<br>

## 2. 포인터를 이용한 연결 리스트
---
노드마다 뒤쪽 노드를 가리키는 포인터가 포함되도록 구현하는 연결 리스트를 알아보자.  
Node는 데이터용 필드 data와는 별도로 자신과 같은 클래스형의 인스턴스를 참조하기 위한 참조용 필드 next를 갖는다. 이처럼 자신과 같은 형의 인스턴스를 참조하는 필드가 있는 구조를 자기 참조형이라고 한다. 여기서 data는 데이터 자체가 아니라 데이터에 대한 참조이고 next는 노드에 대한 참조이다.  

### 클래스와 함수 설명
+ 노드 클래스 Node : data, next의 필드로 구성
    - \_\_init\_\_() 함수 : 전달 받은 data와 next를 해당 필드에 대입
+ 연결 리스트 클래스 LinkedList : 3개의 필드로 구성 -> no(리스트에 등록되어 있는 노드의 개수), head(머리 노드에 대한 참조), current(현재 주목하고 있는 노드에 대한 참조)
    - \_\_init\_\_() 함수 : head, current = None, no = 0 대입
    - \_\_len\_\_() 함수 : 노드의 개수를 반환하는 함수. no값 반환
+ search() 함수 : 인수로 주어진 데이터와 값이 같은 노드를 검색하는 함수
    - 종료조건 : 검색 조건을 만족하는 노드를 발견하지 못하고 꼬리 노드 까지 왔을 경우, 검색 조건을 만족하는 노드를 발견한 경우
+ \_\_contains\_\_() 함수 : 리스트에 data와 값이 같은 노드가 포함되어 있는지를 판단하는 함수. 포함되있으면 True 아니면 False
+ add_first() 함수 : 리스트의 맨 앞에 노드를 삽입하는 함수
+ add_last() 함수 : 리스트의 맨 끝에 노드를 삽입하는 함수
    - 리스트가 비어 있을 때 : add_first() 함수 호출
    - 비어있지 않을 때 : 맨 끝에 노드 삽입
+ remove_first() 함수 : 머리 노드를 삭제하는 함수
+ remove_last() 함수 : 꼬리 노드를 삭제하는 함수
    - 리스트에 노드가 하나만 있을 때 : remove_first() 함수 호출
    - 2개 이상 존재할 때 : 맨 끝 노드 삭제
+ remove() 함수 : 임의의 노드를 삭제. 
    - 머리 노드일 때 : remove_first()
    - 머리 노드가 아닐 때 : 인수로 받은 노드를 삭제
+ remove_current_node() 함수 : 현재 주목하고 있는 노드를 삭제, remove 함수에 인자로 current
+ clear() 함수 : 모든 노드를 삭제하는 함수
+ next() 함수 : 주목 노드를 한 칸 뒤로 이동시키는 함수
+ print_current_node() 함수 : 주목 노드를 출력하는 함수
+ print() 함수 : 모든 노드를 출력하는 함수 

### 구현하기
```
# module.py
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None
        self.no=0
    def __len__(self):
        return self.no    
    def search(self,data):
        if self.head is not None: # 비어있지 않으면 
            cnt=0
            ptr = self.head
            while ptr is not None:
                if ptr.data == data:
                    self.current = ptr
                    return cnt
                ptr = ptr.next
                cnt+=1
        return -1
    def __contains__(self,data):
        return self.search(data)>=0
    def add_first(self,data):
        ptr = self.head
        self.head = self.current = Node(data,ptr)
        self.no +=1
    def add_last(self,data):
        if self.head is None:
            self.add_first(data)
        else :
            ptr = self.head
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next = self.current = Node(data,None)
            self.no +=1
    def remove_first(self) :
        if self.head is not None:
            self.head = self.current= self.head.next
            self.no -=1
    def remove_last(self):
        if self.head.next is None: # 첫노드 유무 검사 필요 X remove_first에서 검사해줌
            self.remove_first()
        else :
            ptr = pre = self.head # 맨 뒤 노드 삭제할 경우 그 앞의 노드에서 끊어줘야함            
            while ptr.next is not None:
                pre = ptr
                ptr = ptr.next
            pre.next = None
            self.current = pre
            self.no -=1
    def remove(self,p): # p는 노드
        if self.head is not None:
            if self.head is p : # 참조하는 객체의 식별번호가 같아야 하므로 is 사용
                self.remove_first()
            else :
                ptr = self.head                
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None :
                        return 
                ptr.next=p.next
                self.current = ptr
                self.no-=1
    def remove_current_node(self):
        if self.head is not None:
            self.remove(self.current)
    def clear(self): # 모든 연결 끊기
        while self.head is not None: 
            self.remove_first()
        self.current = None
        # self.no =0 안해도 while문의 self.remove.first함수에서 처리된다.
    def next(self):
        if self.current is None or self.current.next is None:
            return False 
        else :
            self.current = self.current.next
            return True
    def print_current_node(self):
        if self.current is None:
            print("주목 노드가 존재X")
        else :
            print(self.current.data)
    def print(self): # a모든 노드 출력    
        ptr=self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
    # for, map 과 같이 이터레이터가 사용될때 자동적으로 호출되어 이터레이터를 반환 cf) 이터레이터도 객체
    def __iter__(self): 
        return LinkedListIterator(self.head) # LinkedListIterator(self.head) 객체를 반환

# 이터레이터용 클래스 
# 이터레이터 안에는 iter과 next메소드가 있어야한다.
# 이터레이터도 객체임
class LinkedListIterator:
    def __init__(self,head): # next메소드에서 반환해줄 내용을 위해
        self.current = head
    # 이 LinkedListIterator이라는 클래스는 이터레이터로 사용할 것이라는 가정하에 만들어짐
    # 원래 이터레이터의 iter메소드는 자기 자신을 반환하므로
    def __iter__(self): # 자기 자신을 반환
        return self
    def __next__(self):
        if self.current is None :
            raise StopIteration
        else :
            data = self.current.data
            self.current = self.current.next
            return data

# main.py
from enum import Enum
from module import LinkedList

Menu = Enum("Menu","머리에노드삽입 꼬리에노드삽입 머리에노드삭제\
    꼬리노드삭제 주목노드출력 주목노드이동 주목노드삭제 모든노드삭제 검색 멤버십판단\
        모든노드출력 스캔 종료")
def select_menu():
    s=[f"({m.value}){m.name} " for m in Menu]
    while True :
        print(*s,sep=" ",end=" ")
        n = int(input(": "))
        if 1<=n<=len(s):
            return Menu(n)

lst = LinkedList() # 클래스도 () 필요하니 주의할것

while True:
    menu = select_menu()
    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input("머리 노드에 넣을 값: ")))
    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input("꼬리 노드에 넣을 값: ")))
    elif menu == Menu.머리에노드삭제:
        lst.remove_first()
    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()
    elif menu == Menu.주목노드출력:
        lst.print_current_node()
    elif menu == Menu.주목노드이동:
        lst.next()
    elif menu == Menu.주목노드삭제:
        lst.remove_current_node()
    elif menu == Menu.모든노드삭제:
        lst.clear()
    elif menu == Menu.검색:
        ans = lst.search(int(input('검색할 값 : ')))
        if ans >=0:
            print(f'그 값의 데이터는 {ans}번째 노드에 있다. 0번 노드부터 카운트')
        else :
            print(f"그 값은 없다.")
    elif menu == Menu.멤버십판단:
        ans = int(input("판단할 값을 입력 : "))
        if ans in lst:
            print("포함되어 있다.")
        else :
            print("포함되어 있지 않다")        
    elif menu == Menu.모든노드출력:
        lst.print()
    elif menu == Menu.스캔:
        for e in lst:
            print(e)
    else :
        break
```
모든노드출력과 스캔은 결국 같은데 스캔의 경우 이터레이터를 사용했다.  

__cf) 이터러블 객체와 이터레이터의 구현__  
str형 문자열, list형 리스트, tuple형 튜플 등은 이터러블(iterable, 반복가능)하다는 공통점이 있다. 이터러블 객체는 원소를 1개씩 꺼내는 구조의 객체이다. 이터러블 객체를 내장 함수인 iter() 함수에 인수로 전달하면 그 객체에 대한 이터레이터(iterator, 반복자)를 반환한다.  
이터레이터는 데이터가 줄지어 늘어선 것을 표현하는 객체이다. 이터레이터의 \_\_next\_\_()함수를 호출하거나, 내장 함수인 next() 함수에 반복자를 전달하면 줄지어 늘어선 원소를 순차적으로 꺼낸다. 꺼낼 원소가 없다면 StopIteration 예외처리를 보낸다.  
__추가적 설명__  
이터레이션(Iteration) : 어떤 객체의 원소에 하나씩 차례로 접근하는 것, 명시적으로든 암묵적으로든 반복문을 사용해 객체의 여러 원소에 하나하나 접근하면 그것이 이터레이션이다.  
이터러블은 (for a in iterable) 과 같은 문법을 사용할 수 있는데 이 문법을 사용할 수 있는 이유는 iterable 객체 안에 \_\_iter\_\_메소드가 있기 때문이다. 위의 문법을 사용하면 객체의 \_\_iter\_\_메소드가 실행되어 이터레이터를 반환해준다.  
이터레이터는 \_\_next\_\_메소드로 데이터를 순차적으로 호출할 수 있는 객체이다. 실제로 루프가 돌면서 반복 도중 현재 자기 위치를 기억하는 것이 이터레이터이다. 이터레이터 또한 \_\_iter\_\_메소드를 가지고 있는데 실행하면 자기 자신을 반환한다. 이터레이터는 \_\_next\_\_메소드도 가지고 있다.
for 문, map 등에서는 이터레이터의 \_\_next\_\_가 자동적으로 호출된다.  


__cf) 파이썬의 리스트는 자료구조가 아니다.__  
파이썬의 리스트는 연결 리스트의 자료구조가 아니라 모든 원소를 연속으로 메모리에 배치하는 '배열'로 내부에서 구현하고 있다. 
<br>

## 3. 커서를 이용한 연결 리스트
---
포인터를 이용한 연결리스트의 경우 노드를 삽입, 삭제할 때 데이터를 이동하지 않고 처리하는 특징이 있다. 하지만 노드를 삽입, 삭제할 때마다 내부에서 노드용 인스턴스를 생성하고 소멸한다. 이때 메모리를 확보하고 해제하는 데 비용을 결코 무시할 수 없다. 따라서 프로그램을 실행하면서 데이터 개수가 크게 변하지 않거나 데이터 최대 개수를 예측할 수 있는 경우라면 커서를 이용한 연결 리스트를 사용하는게 좋다.  

### 프리 리스트
연결 리스트인 프리 리스트는 삭제된 레코드 그룹을 관리할 때 사용하는 자료구조이다. 이를 사용해서 삭제 후 비어 있는 배열을 활용할 수 있다.

### 구현하기
```
# module.py
Null = -1

class Node:
    def __init__(self,data=Null,next=Null,dnext=Null):
        self.data = data
        self.next= next
        self.dnext=dnext
class ArrayLinkedList:
    def __init__(self,capacity):
        self.capacity=capacity
        self.head = Null
        self.no = 0
        self.n = [Node()]*self.capacity
        self.max = Null # 사용 중인 꼬리 레코드
        self.deleted =Null # 프리 리스트의 머리 인덱스
        self.current=Null
    def __len__(self):
        return self.no
    def get_insert_index(self): # 넣을 인덱스 위치 찾기
        if self.deleted!=Null:
            rec = self.deleted
            self.deleted=self.n[rec].dnext
            return rec
        else :
            if self.max +1<self.capacity: 
                self.max+=1                
                return self.max
            else :
                return Null
    def delete_index(self,idx): # 삭제된 인덱스 프리 리스트에 넣기
        if self.deleted == Null:
            self.deleted=idx
            self.n[idx].dnext=Null
        else :
            rec = self.deleted
            self.deleted=idx
            self.n[idx].dnext=rec
    def search(self,data):
        cnt=0  # 논리적 인덱스
        ptr = self.head
        while ptr !=Null:
            if self.n[ptr].data is data:
                self.current=ptr # 물리적 인덱스
                return cnt
            ptr = self.n[ptr].next
            cnt+=1
        return Null
    
    def __contains__(self,data):
        return self.search(data)>=0
    def add_first(self,data):
        ptr = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec
            self.n[rec] = Node(data,ptr)
            self.no+=1
    def add_last(self,data):
        if self.head == Null:
            self.add_first(data)
        else :            
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr=self.n[ptr].next
            rec = self.get_insert_index()
            if rec != Null:                    
                self.n[ptr].next = self.current = rec
                self.n[rec]=Node(data)
                self.no +=1
    
    # remove 함수에서는 max 건들면 안된다.
    # 삭제되면서 삭제되는 인덱스 dnext값이 여전히 사용될 예정임
    # 따라서 max는 변화 없다.
    def remove_first(self):
        ptr = self.head
        if ptr != Null:
            self.head=self.current=self.n[ptr].next
            self.delete_index(ptr)
            self.no-=1
    def remove_last(self):
        ptr = self.head
        pre = self.head
        if self.n[ptr].next == Null:
            self.remove_first()
        else :
            while self.n[ptr].next !=Null:
                pre = ptr
                ptr = self.n[ptr].next
            self.n[pre].next = Null
            self.no-=1
            self.current=pre
            self.delete_index(ptr)
    def remove(self,p): # p는 인덱스
        if self.head != Null:
            if self.head == p:
                self.remove_first()
            else :
                ptr = self.head
                while self.n[ptr].next !=p:
                    ptr=self.n[ptr].next
                    if ptr == Null:
                        return
                self.current = ptr
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.no-=1
    def remove_current_node(self):
        self.remove(self.current)
    def clear(self):
        while self.head != Null:
            self.remove_first()        
        self.current=Null
    def next(self):
        if self.current ==Null or self.n[self.current].next == Null:
            return False
        self.current = self.n[self.current].next
        return True
    def print_current_node(self):
        if self.current == Null:
            print("주목노드 없다")
        else:
            print(self.n[self.current].data)
    def print(self):
        ptr = self.head
        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next
    def dump(self):
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')
    def __iter__(self):
        return ArrayLinkedListIterator(self.n,self.head)

class ArrayLinkedListIterator:
    def __init__(self,n,head):
        self.n=n
        self.current=head
    def __iter__(self):
        return self
    def __next__(self):
        if self.current ==Null:
            raise StopIteration
        else :
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data

# main.py
from enum import Enum
from module import ArrayLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = ArrayLinkedList(100)  # 선형 리스트를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:               # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
                                    
    elif menu == Menu.꼬리에노드삽입:             # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:             # 맨 앞 노드를 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:             # 맨 끝 노드를 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:             # 주목 노드를 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:             # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드삭제:             # 주목 노드를 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:             # 모두 삭제
        lst.clear()

    elif menu == Menu.검색:                     # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'이 키를 갖는 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:               # 멤버십을 판단
        print('그 값의 데이터는 포함되어'
              +(' 있습니다.' if int(input('판단할 값을 입력하세요.')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:             # 모든 노드를 출력
        lst.print()

    elif menu == Menu.스캔:                     # 모든 노드 스캔
        for e in lst:
             print(e)

    else:                                       # 종료
        break
```


<br>

  
---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__


