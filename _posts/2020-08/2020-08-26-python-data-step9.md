---
layout: post
title:  파이썬 자료구조 9장. 트리
subtitle:   파이썬 자료구조 9장. 트리
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 트리 구조](#1-원형-리스트)
  - [2. 이진 트리](#2-이진-트리)
  - [3. 이진 검색 트리](#3-이진-검색-트리)

## 1. 트리구조
---
### 트리의 구조와 관련 용어
+ 루트 : 트리의 가장 위쪽에 있는 노드
+ 리프 : 가장 아래쪽에 있는 노드, 단말 노드라고도 함
+ 비단말 노드 : 리프를 제외한 노드(루트 포함)
+ 자식 : 어떤 노드와 가지가 연결되었을 때 아래쪽 노드
+ 부모 : 어떤 노드와 가지가 연결되었을 때 가장 위쪽에 있는 노드
+ 형제 : 부모가 같은 노드
+ 조상 : 어떤 노드에서 위쪽으로 가지를 따라가면 만나는 모든 노드
+ 자손 : 어떤 노드에서 아래쪽으로 가지를 따라가면 만나는 모든 노드
+ 레벨 : 루트에서 얼마나 멀리 떨어져 있는지를 나타내는 것, 루트는 레벨 0 자식노드는 레벨 1
+ 차수 : 각 노드가 갖는 자식의 수
+ 높이 : 루트에서 가장 멀리 있는 리프까지의 거리, 리프 레벨의 최댓값
+ 서브트리 : 어떤 노드를 루트로 하고 그 자손으로 구성된 트리
+ 빈 트리 : 노드와 가지가 전혀 없는 트리, 널 트리라고도 함

### 순서 트리와 무순서 트리
트리는 형제 노드의 순서 관계가 있는지에 따라 2종류로 분류된다. 형제 노드의 순서 관계가 있으면 순서트리, 구별하지 않으면 무순서 트리라고 한다.

### 순서 트리의 검색
순서 트리의 노드를 스캔하는 방법은 크게 2가지이다. 
+ 너브 우선 검색 : 낮은 레벨부터 왼쪽에서 오른쪽으로 검색하고, 한 레벨에서 검색을 마치면 다음 레벨로 내려가는 방법, 즉 맨 위에서부터 왼쪽에서 오른쪽, 왼쪽에서 오른쪽으로 검색하는법
+ 깊이 우선 검색 : 리프에 도달할 때까지 아래쪽으로 내려가면서 검색하는 것을 우선으로 하는 방법, 리프에 도달해서 더 이상 검색할 곳이 없으면 일단 부모 노드로 돌아가고 그 뒤 다시 자식 노드로 내려간다.
  - 전위순회 : 노드 방문 -> 왼쪽 자식 -> 오른쪽 자식
  - 중위순회 : 왼쪽 자식 -> 노드 방문 -> 오른쪽 자식
  - 후위순회 : 왼쪽 자식 -> 오른쪽 자식 -> 노드 방문

<br>

## 2. 이진 트리
---
노드가 왼쪽 자식과 오른쪽 자식만을 갖는 트리를 이진 트리라고 한다. 이때 두 자식 가운데 하나 또는 둘 다 존재하지 않는 노드가 있어도 상관없다.  
루트부터 아래쪽 레벨로 노드가 가득 차 있고, 같은 레벨 안에서 왼쪽부터 오른쪽으로 노드가 채워져 있는 이즌트리를 완전 이진 트리라고 한다. 높이가 k인 완전 이진 트리가 가질 수 있는 노드 수는 최대 2^(k+1) - 1이므로, n개의 노드를 저장할 수 있는 완전 이진 트리의 높이는 log n 이다.  

__cf) 균형 검색 트리__  
이진 검색 트리는 키의 오름차순으로 노드가 삽입되면 트리의 높이가 깊어지는 단점이 있다. 예를 들면 1,2,3,4,5 순으로 노드를 삽입하면 계속 오른쪽으로 이어지면서 높이가 4가 된다. 이를 개선해서 높이를 O(log n)으로 제한하여 고안된 검색 트리를 균형 검색 트리라고 한다. 이진의 균형 검색 트리로는 AVL 트리, 레드블랙 트리가 있다.  
<br>

## 3. 이진 검색 트리
---
### 조건
+ 왼쪽 서브트리 노드의 키값을 자신의 노드 키값보다 작아야 한다.
+ 오른쪽 서브트리 노드의 키값은 자신의 노드 키값보다 커야한다.
+ 키값이 같은 노드는 복수로 존재할 수 없다.

### 특징
+ 구조가 단순
+ 중위 순회의 깊이 우선 검색을 통하여 노드값을 오름차순으로 얻을 수 있다.
+ 이진 검색과 비슷한 방식으로 빠르게 검색 가능
+ 노드 삽입이 단순

### 클래스와 함수
+ Node 클래스 : key, value, left(왼쪽 자식 노드 참조), right(오른쪽 자식 노드 참조) 4개의 필드
+ BinarySearchTree : 이진 검색 트리를 나타내는 클래스
+ search() 함수 : 검색을 수행하는 함수
  - 루트에 주목한다. 루트를 p라고 하자
  - p가 None이면 검색을 실패하고 종료
  - 검색하는 key와 주목 노드 p의 키를 비교
    + key = p : 검색 성공 종료
    + key < p : 주목 노드를 왼쪽 자식 노드로 이동
    + key > p : 주목 노드를 오른쪽 자식 노드로 이동
  - 2번 과정으로 돌아감
+ add() 함수 : 노드 삽입, 노드 삽입한 뒤에 트리의 형태가 이진 검색 트리의 조건을 유지
  - 루트에 주목한다. 주목하는 노드를 node라고 하자
  - 삽입하는 key와 주목 노드 node의 키를 비교
    + key = node인 경우 : 삽입을 실패하고 종료
    + key < node인 경우 
      - 왼쪽 자식 노드가 없으면 그자리에 노드 삽입하고 종료
      - 왼쪽 자식 노드가 있으면, 주목 노드를 왼쪽 자식 노드로 옮긴다.
    + key < node : 인 경우
      - 오른쪽 자식 노드가 없으면 그 자리에 노드 삽입후 종료
      - 오른쪽 자식 노드가 있으면 주목 노드를 오른쪽 자식 노드로 옮긴다.
  - 2번 과정으로 돌아간다.
+ remove() 함수 : 노드를 삭제하는 과정
  - 자식 노드가 없는 노드를 삭제하는 경우
    + 삭제할 노드가 부모 노드의 왼쪽 자식이면, 부모의 왼쪽 포인터를 None으로 한다.
    + 삭제할 노드가 부모 노드의 오른쪽 자식이면, 부모의 오른쪽 포인터를 None으로 한다.
  - 자식 노드가 1개인 노드를 삭제하는 경우
    + 삭제할 노드가 부모 노드의 왼쪽 자식인 경우 : 부모의 왼쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트
    + 삭제할 노드가 부모 노드의 오른쪽 자식인 경우 : 부모의 오른쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트
  - 자식 노드가 2개인 노드를 삭제하는 경우
    + 삭제할 노드의 왼쪽 서브트리에서 키값이 가장 큰 노드를 검색
    + 검색한 노드를 삭제 위치로 옮긴다. 즉, 검색한 노드의 데이터를 삭제할 노드 위치에 복사
    + 옮긴 노드를 삭제
      - 옮긴 노드에 자식이 없으면 : 자식 노드가 없는 노드를 삭제하는 경우에 따라 노드 삭제
      - 옮긴 노드에 자식이 1개만 있으면 : 자식 노드가 1개인 노드의 삭제에 따라 노드 삭제
+  dump() 함수 : 모든 노드를 키의 오름차순으로 출력 => 중위 순회의 깊이 우선 검색
+ min_key(), max_key() 함수 : 가장 작은 키와 가장 큰 키를 반환

### 구현
```
# module.py
class Node:
    def __init__(self,key,value,left,right):
        self.key =key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None # 루트
    def search(self,key):
        p = self.root
        while p is not None :
            if p.key == key:
                return p.value
            elif p.key < key :
                p = p.right
            else :
                p = p.left
        return None
    def add(self,key,value):
        # 키가 key이고 값이 value인 노드 삽입
        # 메소드 안에서 재귀구현 하려면 함수 새로 정의하는게 좋다
        def add_node(node,key,value):
            # node를 루트로 하는 서브 트리에 키가 key이고 값이 value인 노드를 삽입
            if node.key ==key :
                return False
            elif node.key > key:
                if node.left is None:
                    node.left = Node(key,value,None,None)
                else :
                    add_node(node.left,key,value)
            else :
                if node.right is None:
                    node.right = Node(key,value,None,None)
                else :
                    add_node(node.right,key,value)
            return True
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else :
            # return 반드시 있어야 한다. 재귀를 마치고 결과값이 나오면 그것을 return 해줘야함
            return add_node(self.root,key,value)

    def remove(self,key):
        p=self.root
        parent = None
        # is_left_child = True  굳이 미리 정의 안해도 된다.
        
        # 삭제할 키를 검색
        while True:
            if p is None:
                return False
            if p.key == key:
                break
            else :
                parent = p
                if p.key < key:
                    # 삭제할때 부모노드의 왼쪽인가 오른쪽인가를 판단해주는 용도
                    is_left_child = False 
                    p = p.right
                else :
                    p = p.left
                    # 삭제할때 부모노드의 왼쪽인가 오른쪽인가를 판단해주는 용도
                    is_left_child = True
        
        
        if p.left is None: # 왼쪽 노드가 없는 경우 오른쪽 노드가 있을때 없을 때를 한 번에 처리
            if p is self.root: # p가 self.root일경우 left_child가 없으므로 따로 처리
                self.root = p.right                
            elif is_left_child :
                parent.left=p.right # 오른쪽 노드가 있으면 그대로 들어가고 없으면 None이 들어가고
            else :
                parent.right=p.right
        elif p.right is None: # 오른쪽 노드가 없는 경우 왼쪽 노드가 있을때 없을 때를 한 번에 처리
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else :
                parent.right=p.left
        else : # 양쪽 노드가 있는 경우
            parent = p
            left = p.left
            is_left_child=True
            while left.right is not None:
                parent = left
                left=left.right
                is_left_child=False
            p.key = left.key
            p.value=left.value
            if is_left_child : # 삭제 대상일 기준으로 왼쪽 서브 트리에서 계속 왼쪽 노드만 있을 때
                parent.left=left.left
            else : # 삭제 대상을 기준으로 왼쪽 서브 트리에 오른쪽 노드도 있는 경우
                # 이때 left의 자식 노드가 있다면 왼쪽 노드만 있을 수 밖에 없음
                # 오른쪽 자식 노드가 있었다면 그 노드가 left가 되었을 것임
                parent.right = left.left
        return True
    def dump(self,reverse=False): # 중위 순회의 깊이 우선 탐색으로 오름차순 출력
        # 메소드 안에서 재귀구현 하려면 함수 새로 정의하는게 좋다
        def print_subtree(node): # 오름차순
            if node is not None: # 재귀 탈출 조건
                print_subtree(node.left)
                print(f'({node.key}) {node.value}')
                print_subtree(node.right)
        def print_subtree_rev(node): # 내림차순
            if node is not None: # 재귀 탈출 조건
                print_subtree_rev(node.right) # 오른쪽 노드 출력
                print(f'({node.key}) {node.value}')
                print_subtree_rev(node.left) # 왼쪽 노드 출력
        print_subtree_rev(self.root) if reverse else print_subtree(self.root)
    def min_key(self):
        p=self.root
        if p is None:
            return None
        while p.left is not None:
            p=p.left
        return p.key
    def max_key(self):
        p=self.root
        if p is None:
            return None
        while p.right is not None:
            p=p.right
        return p.key

# main.py
from enum import Enum
from module import BinarySearchTree

Menu = Enum('Menu', ['삽입', '삭제', '검색', '오름차순덤프', '내림차순덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()  # 이진 검색 트리를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.삽입:  # 삽입
        key = int(input('삽입할 키를 입력하세요.: '))
        val = input('삽입할 값을 입력하세요.: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        tree.remove(key)

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.오름차순덤프:  # 오름차순 덤프
        tree.dump()


    elif menu == Menu.내림차순덤프:  # 내림차순 덤프
        tree.dump(reverse = True)

    elif menu == Menu.키의범위 :  # 키의 범위(최솟값과 최댓값)
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최댓값은 {tree.max_key()}입니다.')
        
    else:# 종료
        break
```




<br>

  
---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__