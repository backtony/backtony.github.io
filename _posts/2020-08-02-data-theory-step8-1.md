---
layout: post
title:  트리(Tree)
subtitle: 트리(Tree)
categories: data
tags: theory book datastructure tree 트리
comments: true
# header-img:
---
+ __목차__
  - [1. 트리의 개요](#1-트리의-개요)
  - [2. 이진 트리의 구현](#2-이진-트리의-구현)
  - [3. 이진 트리의 순회](#3-이진-트리의-순회)
  - [4. 수식 트리의 구현](#4-수식-트리의-구현)

## 1. 트리의 개요
---
### 트리 관련 용어의 소개
![그림1](https://backtony.github.io/assets/img/post/data/step8/1.PNG)

+ 노드 : node
    - 트리의 구성요소에 해당하는 A, B, C, D, E, F와 같은 요소
+ 간선 : edge
    - 노드와 노드를 연결하는 연결선
+ 루트 노트 : root node
    - 트리 구조에서 최상위에 존재하는 A와 같은 노드
+ 단말 노드 : terminal node
    - 아래로 또 다른 노드가 연결되어 있지 않은 E, F, C, D와 같은 노드
+ 내부 노드 : internal node
    - 단말 노드를 제외한 모든 노드로 A, B와 같은 노드

### 트리의 노드간 관계
![그림2](https://backtony.github.io/assets/img/post/data/step8/2.PNG)

+ 노드 A는 노드 B,C,D의 부모 노드이다.
+ 노드 B, C, D는 노드 A의 자식 노드이다.
+ 노드 B, C, D는 부모 노드가 같으므로 서로가 서로에게 형제 노드이다.  

### 서브 트리의 이해
![그림3](https://backtony.github.io/assets/img/post/data/step8/3.PNG)

+ 서브트리 역시 서브 트리로 이뤄져 있으며, 그 서브 트리 역시 또 다른 서브 트리로 이뤄져 있다. => 재귀적이다.  

### 이진 트리의 이해
![그림4](https://backtony.github.io/assets/img/post/data/step8/4.PNG)

+ 이진 트리의 조건
    - 루트 노드를 중심으로 두 개의 서브 트리로 나뉜다.
    - 나뉘어진 두 서브 트리도 모두 이진 트리이어야 한다.

__cf) 조건에 따르면 D와 E도 이진 트리인가?__  
![그림5](https://backtony.github.io/assets/img/post/data/step8/5.PNG)

보이지 않는 공집합 노드가 존재하기 때문에 이진 트리라고 인지한다. 하나의 노드에 두 개의 노드가 달리는 형태의 트리는 모두 이진 트리이다.  

### 레벨과 높이, 그리고 포화, 완전 이진 트리
![그림6](https://backtony.github.io/assets/img/post/data/step8/6.PNG)

+ 트리의 높이와 레벨의 최대 값은 같다.
+ 레벨은 0부터 시작한다.

![그림7](https://backtony.github.io/assets/img/post/data/step8/7.PNG)

+ 완전 이진 트리
    - 위에서 아래로, 왼쪽에서 오른쪽으로 채워진 트리를 의미한다.
    - 포화 이진 트리는 동시에 완전 이진 트리이지만 그 역은 성립하지 않는다.
    - 그림의 완전 이진 트리에서 I가 빠져도 완전 이진 트리 이다.

## 2. 이진 트리의 구현
---


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
