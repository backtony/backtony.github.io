---
layout: post
title:  최소 비용 신장 트리
subtitle: 최소 비용 신장 트리
categories: data
tags: theory book datastructure graph 
comments: true
# header-img:
---
+ __목차__
  - [1. 사이클의 이해](#1-사이클-이해와)
  - [2. 크루스칼 알고리즘 1](#2-크루스칼-알고리즘-1)
  - [3. 크루스칼 알고리즘 2](#3-크루스칼-알고리즘-2)
  - [4. 구현](#4-구현)

## 1. 사이클의 이해
---
![그림1](https://backtony.github.io/assets/img/post/data/step13/7.PNG)

+ 단순 경로 : 간선을 중복 포함 하지 않고 이동하는 경로
+ 사이클 : 시작점과 끝점이 같은 단순 경로

### 신장트리
![그림2](https://backtony.github.io/assets/img/post/data/step13/8.PNG)

위 그림을 회전시켜보면 일종의 트리로 볼 수 있다. 어떠한 경로를 구성하더라도 '사이클'을 형성하지 않는 그래프를 신장 트리라고 한다.  
__특징__  
+ 그래프의 모든 정점이 간선에 의해서 하나로 연결되어 있다.
+ 그래프 내에서 사이클을 형성하지 않는다.

### 최소 비용 신장 트리 구성의 예
![그림3](https://backtony.github.io/assets/img/post/data/step13/9.PNG)

<br>

## 2. 크루스칼 알고리즘 1
---
가중치를 기준으로 간선을 정렬한 후에 MST가 될 때까지 간선을 하나씩 선택해 나가는 방식  
![그림4](https://backtony.github.io/assets/img/post/data/step13/10.PNG)

최소 비용 신장트리의 조건인 (간선의 수 +1 = 정점의 수)를 만족하면 이것으로 최소 비용 신장 트리 형성 완료!  
<br>

## 3. 크루스칼 알고리즘 2
---
높은 가중치의 간선을 하나씩 빼는 방식
![그림5](https://backtony.github.io/assets/img/post/data/step13/11.PNG)

![그림6](https://backtony.github.io/assets/img/post/data/step13/12.PNG)

가중치가 8인 간선이 없으면 정점 A와 D가 연결되지 않으므로 삭제하지 않는다. 알고리즘 1과 마찬가지로 최소 비용 신장 트리의 조건인 (간선의 수 + 1 = 정점의 수)를 만족하면 이것으로 최소 비용 신창 트리 형성 완료!

## 4. 구현
---
크루스칼 알고리즘 2를 구현해보자.  
이전에 구현한 연결 리스트, 배열 기반 스택, 우선순위 큐, 우선순위 큐의 기반이 되는 힙을 활용하여 구현하자.  

__ 




---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__