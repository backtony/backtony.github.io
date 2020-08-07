---
layout: post
title:  탐색 (Search) 2 균형 잡힌 이진 탐색 트리
subtitle: 탐색 (Search) 2 균형 잡힌 이진 탐색 트리
categories: data
tags: theory book datastructure search 탐색
comments: true
# header-img:
---
+ __목차__
  - [1. 균형 잡힌 이진 탐색 트리](#1-균형-잡힌-이진-탐색-트리)
  - [2. AVL 트리의 구현](#2-avl-트리의-구현)

## 1. 균형 잡힌 이진 탐색 트리
---
### 이진 탐색 트리의 문제점
![그림1](https://backtony.github.io/assets/img/post/data/step11/4.PNG)

이진 탐색 트리의 균형 문제를 해결한 트리 : AVL 트리

### 자동으로 균형 잡는 AVL 트리와 균형 인수
![그림2](https://backtony.github.io/assets/img/post/data/step11/5.PNG)

AVL 트리는 균형 인수를 기준으로 트리의 균형을 잡기 위한 재조정의 진행 시기를 결정한다.

### LL 상태와 LL회전
![그림3](https://backtony.github.io/assets/img/post/data/step11/6.PNG)

5가 저장된 노드의 왼쪽에 3이 저장된 자식 노드가 하나 존재하고 그 자식 노드의 왼쪽에 1이 저장된 자식 노드가 또 하나 존재하는 이러한 상태를 LL 상태라고 하고 이를 균형잡기 위해서 LL회전을 진행한다.  

![그림4](https://backtony.github.io/assets/img/post/data/step11/7.PNG)

cNode의 오른쪽 자식 노드로 pNode를 두고 이전에 cNode의 오른쪽 노드를 pNode의 왼쪽 노드로 연결시킨다.  

### RR상태와 RR회전
![그림5](https://backtony.github.io/assets/img/post/data/step11/8.PNG)

cNode의 왼쪽 자식 노드로 pNode를 두고 이전에 cNode의 왼쪽 노드를 pNode의 오른쪽 노드로 연결 시킨다.  

### LR 상태와 LR회전
![그림6](https://backtony.github.io/assets/img/post/data/step11/9.PNG)

LL과 RR 상태와 같이 한 번에 균형을 잡을 수 없다. 따라서 한번은 RR회전으로 LL상태로 만들어 준 후 LL 회전을 사용해서 균형을 맞춘다.  

### RL 상태 RL회전
![그림7](https://backtony.github.io/assets/img/post/data/step11/10.PNG)

LR 상태와 회전과 방향에서만 차이를 보인다. 즉, LL회전이후에 RR회전하여 균형을 맞춘다.  
<br>

## 2. AVL 트리의 구현
---
+ BinaryTree3.h // 이진 트리의 헤더 파일
+ BinaryTree3.c // 이진 트리를 구성하는데 필요한 도구 모임
+ BinarySearchTree.h // 이진 탐색 트리의 헤더 파일
+ BinarySearchTree.c // 이진 탐색 트리의 구현
+ AVLRebalance.h // 리밸런싱 관련 함수들의 선언
+ AVLRebalance.c // 리밸런싱 관련 함수들의 정의

__AVL 트리도 이진 탐색 트리의 일종이므로 앞서 구현한 이진 탐색 트리를 기반으로 구현한다.__  

### 
