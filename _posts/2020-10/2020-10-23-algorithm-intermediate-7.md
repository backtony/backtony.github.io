---
layout: post
title:  다이나믹 프로그래밍 기출문제
subtitle:   다이나믹 프로그래밍 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 간단 정리](#1-간단-정리)
  - [2. 플로이드](#2-플로이드)
  - [3. 정확한 순위](#3-정확한-순위) 
  - [4. 화성 탐사](#4-화성-탐사)
  - [5. 숨바꼭질](#5-숨바꼭질)
 

## 1. 간단 정리
---
### 최단 경로 알고리즘
그래프상에서 가장 짧은 결로를 찾는 알고리즘이다. 다익스트라 알고리즘과 플로이드 워셜 알고리즘을 성능, 구현 난이도, 역할에 대하여 비교해보자.

알고리즘 종류|시간복잡도|구현 난이도|역할
---|---|---|---
다익스트라|O(ElogV)|어려운 편|한 지점에서 다른 모든 지점까지의 최단 경로를 계산
플로이드 워셜|O(V)|쉬운 편|모든 지점에서 다른 모든 지점까지의 최단 경로를 계산

### 다익스트라 알고리즘
다익스트라 알고리즘은 단계마다 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택한 뒤에 그 노드를 거쳐 가는 경우를 확인하여 최단 거리를 갱신하는 방법이다. 우선순위 큐를 이용하여 소스코드를 작성할 수 있다는 점을 기억하자.

### 플로이드 워셜 알고리즘
플로이드 워셜 알고리즘은 다이나믹 프로그래밍을 이용하여 단계마다 거쳐 가는 노드를 기준으로 최단 거리 테이블을 갱신하는 방식으로 동작한다. 다음 점화식만 제대로 기억해 놓는다면 큰 어려움 없이 구현 가능하다. D(ab) = min(D(ab), D(a(ak)+a(kb)))
<Br>

## 2. 플로이드
---
[문제 클릭](https://www.acmicpc.net/problem/11404){: target="_blank"}  

### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

# 도로 정보 입력
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

# 자기 자신으로 가는 길은 0
for i in range(n):
    graph[i][i] = 0

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 불가능한 곳 0으로 수정
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

# 출력
for i in range(n):
    print(*graph[i])
```
플로이드 워셜 알고리즘 작성하면서 자기 자신으로 가는 경우는 0으로 초기화해줘야 하는 부분을 자꾸 생략하고 넘어가는데 잘 기억해두자. 마지막 출력할 때 *쓰는 방법 말고 다른 방법은 없을까?

### 모범 답안
```python

```

<br>

## 3. 정확한 순위
---
### 내가 작성한 코드
```python

```

### 모범 답안
```python

```

<br>

## 4. 화성 탐사
---
### 내가 작성한 코드
```python

```

### 모범 답안
```python

```

<br>

## 5. 숨바꼭질
---
### 내가 작성한 코드
```python

```

### 모범 답안
```python

```

<br>


<br>

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
