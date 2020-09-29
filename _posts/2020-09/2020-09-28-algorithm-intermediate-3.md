---
layout: post
title:  DFS/BFS 기출문제
subtitle:   DFS/BFS 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 간단 정리](#1-간단-정리)
  - [2. 특정한 거리의 도시 찾기](#2-특정한-거리의-도시-찾기)
  - [3. 연구소](#3-연구소) 
  - [4. 경쟁적 전염](#4-경쟁적-전염)
  - [5. 괄호 변환](#5-괄호-변환)
  - [6. 연산자 끼워 넣기](#6-연산자-끼워-넣기)
  - [7. 감시 피하기](#7-감시-피하기)
  - [8. 인구 이동](#8-인구-이동)
  - [9. 블록 이동하기](#9-블록-이동하기)


## 1. 간단 정리
---
+ 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
+ 자료구조 : 데이터를 표현하고 처리하는 방법
+ 스택 : 선입후출, 후입선출구조이며 박스 쌓기에 비유 가능
+ 큐 : 선입선출구조로 공정한 자료구조라고도 한다. 대기 줄에 비유 가능
+ DFS : Depth-First Search, 깊이 우선 탐색 알고리즘이며 그래프를 탐색하는 알고리즘이다. 최대한 얼리 있는 노드를 우선으로 탐색하는 방식으로 동작하며 스택자료구조를 이용
+ BFS : 너비우선 탐색으로 가까운 노드부터 탐색하는 알고리즘이다. 큐를 이용하면 효과적으로 구현 가능

<br>

## 2. 특정한 거리의 도시 찾기
---
[문제 클릭](https://www.acmicpc.net/problem/18352){: target="_blank"}

### 내가 작성한 코드
```python
import sys
import heapq
input = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
INF = int(1e9) # 무한

shortcut = [INF]*(n+1) # 각 도시의 최단 경로
graph =[[] for _ in range(n+1)] # 도시별 연결 정보
q=[] # 우선순위 큐

# 도로 정보 입력
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

# 출발지점 정보 수정 및 우선순위 큐
shortcut[x] = 0
heapq.heappush(q,(0,x))

# 최소 거리 구하기
while q:
    distance, now = heapq.heappop(q)
    # 이미 처리된 경우는 무시 , 첫 시작의 경우가 등호에 해당하므로 등호는 뺀다
    if distance > shortcut[now]:
        continue
    for way in graph[now]: # now에 연결된 도시들
            # 갱신이 필요한 경우
            if distance + 1 < shortcut[way]:
                shortcut[way] = distance+1
                heapq.heappush(q,(shortcut[way],way))

cnt=0
for i in range(1,n+1):
    if shortcut[i] == k:
        print(i)
        cnt+=1
if cnt == 0:
    print(-1)
```
한 가지 출발지점이 정해진 경우에 대해서 각 지점에 대해 최소 거리를 구하는 다익스트라 알고리즘을 사용했다. 다익스트라 알고리즘의 복잡도는 선형로그시간 O(ElogV)이므로 주어진 큰 범위에 적합한 알고리즘이다. (V는 노드, E는 간선, 우선순위 큐로 인해 logV)
<br>

## 3. 연구소
---
[문제 클릭](https://www.acmicpc.net/problem/14502){: target="_blank"}  

<br>

## 4. 경쟁적 전염
---
[문제 클릭](https://www.acmicpc.net/problem/18405){: target="_blank"}  

### 내가 작성한 코드
```python
import sys
from collections import deque
input = sys.stdin.readline

# 시험관 크기 n, 바이러스 종류 k
n, k = map(int, input().split())
graph = [[] for _ in range(n)]
cnt = 0  # 시간초

# U R D L 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시험관 정보
for i in range(n):
    graph[i] = list(map(int, input().rstrip().split()))

# s초후 x,y 위치의 값
s, x, y = map(int, input().split())

next =[]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            next.append((graph[i][j], i, j))  # (바이러스 종류, 좌표)
next.sort()  # 바이러스 번호순 정렬

# 입력된 시간 까지
while cnt < s:
    if not next : # 전염 시작 위치가 없는 경우
        break
    q = deque(next)  # 큐에 삽입
    next.clear()  # 이후 사용을 위해 비우기
    # 큐가 빌때까지 반복
    while q:
        num, i, j = q.popleft()
        # 4방향
        for z in range(4):
            pi = i + dx[z]
            pj = j + dy[z]
            # 범위 내에 있으면서 빈칸인 경우만
            if 0 <= pi < n and 0 <= pj < n and graph[pi][pj] == 0:
                graph[pi][pj] = num  # 바이러스 전염
                next.append((num, pi, pj))  # 다음 전염 시작의 기준 위치
    cnt +=1 # 큐가 다 비게 되면 1초 카운트


print(graph[x-1][y-1])
```
하나씩 옆에 있는 것부터 처리하는 과정을 통해 BFS를 생각해냈다. 바이러스 번호가 작은 것부터 전염을 시작해야 하기 때문에 큐를 바로 사용하기 전에 먼저 전염 번호 순으로 정렬시키고 큐에 대입하는 방법으로 설계했다.

### 모범 답안
```python

```
<br>

## 5. 괄호 변환
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60058){: target="_blank"}  

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
