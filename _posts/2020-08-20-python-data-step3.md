---
layout: post
title:  파이썬 자료구조 3장. 배열 검색(선형검색, 이진검색, 해시법)
subtitle:   파이썬 자료구조 3장. 배열 검색(선형검색, 이진검색, 해시법)
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 선형 검색](#1-선형-검색)
  - [2. 이진 검색](#2-이진-검색)
  - [3. 복잡도](#3-복잡도)
  - [4. index 함수로 검색하기](#4-index-함수로-검색하기)
  - [5. 해시법](#5-해시법)
  
## 1. 선형 검색
---
배열에서 검색하는 방법 중 가장 기본적인 알고리즘이다. 직선 모양(선형)으로 늘어선 배열에서 검색하는 경우에 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘이다.  
__선형 검색 종료 조건__  
+ 검색할 값을 찾지 못하고 배열의 맨 끝을 지나간 경우 : 실패
+ 검색할 값과 같은 원소를 찾은 경우 : 성공

```
# module.py
def seq_search(a,key):
    for i in range(len(a)):
        if a[i] == key:
            return i # 성공시
    return -1 # 실패시 

if __name__ == "__main__":
    n = int(input("원소 수 : "))
    a = [None] * n
    for i in range(n):
        a[i] = int(input("원소값:"))
    
    key = int(input("key : "))
    idx = seq_search(a,key)
    if idx == -1 :
        print("존재하지 않는다.")
    else :
        print(f"{key}는 a[{idx}]에 있다.")    
```
위에서 구현한 seq_search 함수는 임의의 자료형 시퀀스에서 검색할 수도 있다. 시퀀스형에는 리스트형, 바이트 배열형, 문자열형, 튜플형, 바이트열형이 있다.  
```
from module import seq_search # 위에서 작성한 seq_search 가져오기

t = (4,7,5.6,2,3.14)
s='string'
a=['abc','aac','flex']

print(f"{t}에서 5.6 idx는 {seq_search(t,5.6)}이다.")
print(f"{s}에서 t idx는 {seq_search(s,'t')}이다.")
print(f"{a}에서 'abc' idx는 {seq_search(a,'abc')}이다.")
```

### 보초법
위에서는 for문으로 보여서 if문이 1개만 있지만 while문으로 종료조건을 구현시 선형 검색은 반복할 때마다 2가지 종료 조건을 체크한다. 단순하지만 이 과정을 계속 반복하면 종료 조건을 검사하는 비용을 무시할 수 없다. 이 비용을 반으로 줄이는 방법이 보초법이다.  
검색하고자 하는 키값을 맨 끝에 새로 저장하게되면 선형 검색의 종료 조건에서 배열의 끝에 도달한 경우의 종료 조건이 필요 없게 된다. 따라서 while문으로 구현했을 때보다 if문의 판단 횟수가 반으로 줄어들게 된다.  
```
import copy
def seq_search(a,key):
    x=copy.deepcopy(a) # 실제 인수에 영향을 주지않기위해서
    x.append(key)
    i=0
    while True:
        if x[i] == key:
            break
        i+=1
    return i if i != len(a) else -1
```
<br>

## 2. 이진 검색
---
이진 검색은 원소가 오름차순이나 내림차순으로 정렬된 배열에서 좀 더 효율적으로 검색할 수 있는 알고리즘이다. 배열을 반으로 나누는 중간지점을 기준으로 key값이 오른쪽에 있는지 왼쪽에 있는지 판단하고 중간지점을 잘라버리고 해당하는 방향에서 다시 위와 같은 과정을 반복해서 key값을 찾는 방법이다. 오름차순으로 정렬된 배열을 가지고 진행하겠다.  
__정리__  
+ a[mid] < key : mid를 기준으로 오른쪽 한 칸 이동한 곳을 새로운 a[first]로 정하고 검색 범위를 절반으로 줄인다.
+ a[mid] > key : mid를 기준으로 왼쪽으로 한 칸 이동한 곳을 새로운 a[last]로 정하고 검색범위를 절반으로 줄인다.
+ 종료조건 
  - a[mid]와 key가 일치하는 경우
  - 검색범위가 더 이상 없는 경우

```
def bin_search(a,key):
    first = 0
    last = len(a)-1

    while True:
        mid = (first+last)//2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            last = mid -1            
        else :
            first = mid +1
        if first>last: # 역전시 실패
            return -1

if __name__ == "__main__":
    n = int(input("원소 수 : "))
    a = [None] * n
    a[0] = int(input("a[0] = ")) # 오름차순 설정을 위해
    for i in range(1,n):
        while True:
            x = int(input("원소값:"))
            if x>=a[i-1]:
                a[i] = x
                break       
    
    key = int(input("key : "))
    idx = bin_search(a,key)
    if idx == -1 :
        print("존재하지 않는다.")
    else :
        print(f"{key}는 a[{idx}]에 있다.") 
```
<br>

## 3. 복잡도
---
알고리즘의 성능을 객관적으로 평가하는 기준을 복잡도라고 한다. 복잡도는 다음과 같이 2가지로 구분한다.  
+ 시간 복잡도 : 실행하는데 필요한 시간을 평가
  - 복잡도는 차원이 더 높은 쪽의 복잡도를 우선시 한다.
+ 공간 복잡도 : 메모리와 파일 공간이 얼마나 필요한가를 평가

### 선형 검색의 시간 복잡도
선형 검색에서는 주요 판단 기준이 if문이다. 요소의 갯수가 n개이므로 평균적으로 if문은 n/2번 실행될 것이다. 따라서 O(n) 이다.  

### 이진 검색의 시간 복잡도
예를 들어 8개의 원소를 이진 검색한다고 가정하자. 처음에는 8개 2번 째는 4개 3번 째는 2개로 3번의 과정을 수행하게 된다. 따라서 O(log n) 이다.  
<br>

## 4. index 함수로 검색하기
---
모든 검색 과정을 위와 같이 직접 구현해야 하는 것은 아니다. 리스트 또는 튜플에서 검색은 각 클래스의 index() 함수로 수행할 수 있다. index 함수는 다음과 같은 형식으로 호출할 수 있고 호출할 때 인수는 j또는 i,j를 생략할 수 있다.  
```
obj.index(x,i,j) # j는 포함하지 않음
```
리스트 또는 튜플 obj[i:j] 안에 x와 같은 값이 있으면 그 중 가장 작은 인덱스를 반환한다. 없다면 예외 처리로 ValueError을 보낸다.  
<br>

## 5. 해시법
---
해시법은 '데이터를 저장할 위치 = 인덱스'를 간단한 연산으로 구하는 것을 말한다. 이 방법은 원소의 검색뿐 아니라 추가, 삭제도 효율적으로 수행할 수 있다.  
+ 해시 테이블 : 해시값을 인덱스로 하여 원소를 새로 저장한 배열
+ 버킷 : 해시 테이블에서 만들어진 원소

키와 해시값은 일반적으로 N:1이기 때문에 충돌이 발생한다. 따라서 이를 해결하는 방법은 체인법과 오픈 주소법이 있다.  

### 체인법(오픈 해시법)
체인법이란 해시값이 같은 데이터를 체인모양의 연결 리스트로 연결하는 방법을 말하며 오픈 해시법이라고도 한다.  
__Node 클래스 만들기__  
+ key : 키(임의의 자료형)
+ value : 값(임의의 자료형)
+ next : 뒤쪽 노드를 참조(Node형)

__ChainedHash 해시 클래스 만들기__  
+ capacity : 해시 테이블의 크기(배열 원소수)
+ table : 해시 테이블을 저장하는 list형 배열

__search 함수__  
1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 스캔. 키와 같은 값 발견시 성공, 원소의 맨 끝까지 스캔해서 발견되지 않으면 실패

__add 함수__  
1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 선형 검색, 키와 같은 값 발견시 이미 등록된 경우이므로 추가에 실패, 끝까지 발견되지 않으면 해시값인 리스트의 맨 앞에 노드를 추가

__remove 함수__  
1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결 리스트 맨 앞부터 차례로 선형 검색, 키와 같은 값이 발견되면 그 노드를 리스트에서 삭제, 그렇지 않으면 실패

__dump 함수__  
배열 내부 전부 꺼내서 출력

__cf) 해시 함수__  
충돌하지 않기 위해 해시 테이블을 충분히 크게 만들 수 있으나 메모리가 낭비된다. 따라서 충돌을 피하려면 해시 함수가 해시 테이블 크기보다 작거나 같은 정수를 고르게 생성해야 한다. 해시 테이블의 크기는 소수를 선호한다. ChainedHash 클래스의 hash_value 함수는 해시값을 key가 int형인 경우와 아닌 경우로 구분한다.  
+ key가 int형인 경우 : key를 해시의 크기인 capacity로 나눈 나머지를 해시값으로 한다.
+ key가 int형이 아닌 경우 : 표준 라이브러리로 형 변환을 해서 해시값을 얻는다.
    - sha256 알고리즘 : hashlib 모듈에서 제공하는 sha256은 주어진 바이트(byte) 문자열의 해시값을 구하는 해시 알고리즘 생성자이다. hashlib 모듈은 sha256 외에도 MD5 알고리즘인 md5 등 다양한 해시 알고리즘을 제공한다.
    - encode() 함수 : hashlib.sha256에는 바이트 문자열의 인수를 전달해야 한다. 그래서 key를 str형 문자열로 변한한 뒤 그 문자열을 encode() 함수에 전달하여 바이트 문자열로 생성해야 한다.
    - hexdigest() 함수 : sha256 알고리즘에서 해시값을 16진수 문자열로 꺼내준다.
    - int() 함수 : hexdigest 함수로 꺼낸 16진수 문자열을 int형 십진수로 변환해준다.

```
# module.py
import hashlib

class Node:
    # 해시를 구성하는 노드
    def __init__(self,key,value,next):
        self.key = key
        self.value=value
        self.next=next

class ChainedHash:
    # 체인법으로 해시 클래스 구현
    def __init__(self,capacity):
        self.capacity=capacity
        self.table = [None] * self.capacity # 배열만들기
    
    def hash_value(self,key):
        if isinstance(key,int):
            return key % self.capacity
        # 위에서 설명
        return int(hashlib.sha256(str(key).encode()).hexdigest(),16)%self.capacity
    
    def search(self,key):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return p.value
            p=p.next
        return None # 검색 실패

    def add(self,key,value):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return False # 추가 실패 이미 존재
            p=p.next
        # 새 노드 만들고 next에는 해시값을 인덱스로 하는 버킷이 참조하던것 연결
        tmp = Node(key,value,self.table[hash]) 
        # 해시값을 인덱스로 하는 버킷이 tmp를 참조하도록 연결 
        self.table[hash] = tmp 
        return True # 추가 성공
    
    def remove(self,key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None 
        # 제거를 위해서는 제거 앞에 있는 노드를 알아야함
        # 제거 앞 노드와 제거 뒤 노드를 이어줘야하기 때문
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next                    
                else :
                    pp.next = p.next
                return True # 삭제 성공
            pp=p
            p=p.next
        return False # key가 존재하지 않음
    
    def dump(self):
        for i in range(self.capacity):
            print(i,end=" ")
            p = self.table[i]
            while p is not None:
                print(f" -> {p.key} ({p.value})", end=" ")
                p=p.next
            print()

# main.py 구현한 체인해시 클래스를 직접 사용
from module import ChainedHash
from enum import Enum

Menu = Enum('Menu',"추가 삭제 검색 덤프 종료")

def select_menu():
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True :
        print(*s,sep="  ",end=" ")
        n = int(input(": "))
        if 1<= n <= len(Menu):
            return Menu(n)
    
hash = ChainedHash(13)

while True :
    menu = select_menu()

    if menu == Menu.추가 :
        key = int(input("key : "))
        value = input("value : ")
        if not hash.add(key,value):
            print("추가 실패")
    
    elif menu == Menu.삭제 :
        key = int(input("key : "))
        if not hash.remove(key):
            print("삭제 실패")
    
    elif menu == Menu.검색 :
        key = int(input("key : "))
        if hash.search(key) is not None:
            print(f"{key}가 갖는 값 : {hash.search(key)}")
        else :
            print("찾는 데이터가 없다.")
    
    elif menu == Menu.덤프 :
        hash.dump()
    else :
        break
```
<br>

### 오픈 주소법(닫힌 해시법)
오픈 주소법은 충돌이 발생했을 때 재해시를 수행하여 빈 버킷을 찾는 방법이다. 
```
import hashlib
from enum import Enum

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket :
    # 해시를 구성하는 버킷
    # 기본매개변수로 값을 지정
    def __init__(self,key=None,value=None,stat=Status.EMPTY):
        self.key = key # None
        self.value = value # None
        self.stat = stat # Status.EMPTY
    
    def set(self,key,value,stat):
        self.key = key 
        self.value = value 
        self.stat = stat 
    
    # 삭제이후 값 변경을 위한
    def set_status(self,stat):
        self.stat=stat

class OpenHash:
    def __init__(self,capacity):
        self.capacity=capacity
        self.table = [Bucket()] * self.capacity
    
    def hash_value(self,key):
        if isinstance(key,int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(),16)%self.capacity
    
    def rehash_value(self,key):        
        # capacity를 넘는 경우를 대비해서 나머지 연산
        return (self.hash_value(key) +1) % self.capacity
     
    def search_node(self,key):
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(key)
            p = self.table[hash]
        return None 
    
    def search(self,key):
        p = self.search_node(key)
        if p is not None:
            return p.value
        return None            

    def add(self,key,value):
        if self.search(key) is not None:
            return False # 이미 등록된 키
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key,value,Status.OCCUPIED)
                return True
            hash = self.rehash_value(key)
            p = self.table[hash]
        return False 
    
    def remove(self,key):
        p =self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True     
            
    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]
            if p.stat == Status.EMPTY:
                print("--미등록--")
            elif p.stat == Status.DELETED:
                print("--삭제 완료--")
            else :
                print(f"{p.key} ({p.value})")       
```
OpenHash 클래스 안에 다 적용시켜 놨으므로 실제 사용할때는 import OpenHash만 하면 된다. 실습문제는 위에 체인해시 예시의 main.py로 OpenHash로만 수정하면 된다.

<br>


---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__