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
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
