---
layout: post
title: (Python) 백준 1504번 특정한 최단 경로 - class 4
subtitle:   (Python) 백준 1504번 특정한 최단 경로 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1504){:target="_blank"}]


## 1504번 특정한 최단 경로
---
다익스트라 알고리즘을 사용했고 입력 횟수가 많으므로 sys를 사용했다.
```python
import sys
import heapq

input = sys.stdin.readline


n, e = map(int, input().split()) # 정점과 간선의 개수
graph = [[] for _ in range(n + 1)] # 인접 리스트
INF = int(1e9)

# 인접리스트 만들기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

# v1,v2 입력
v1, v2 = map(int, input().split())

# 다익스트라 로직
def dijkstra(start):
    dis = [INF] * (n + 1)
    dis[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, way = heapq.heappop(q)
        if cost > dis[way]:
            continue
        for new_cost, new_way in graph[way]:
            if dis[new_way] > cost + new_cost:
                dis[new_way] = cost + new_cost
                heapq.heappush(q, (dis[new_way], new_way))
    return dis


table_1 = dijkstra(1) # 1에서 다른 정점까지의 최소 거리 테이블
table_v1 = dijkstra(v1) # v1에서 다른 정점까지 최소 거리 테이블
table_v2 = dijkstra(v2) # v2에서 다른 정점까지 최소 거리 테이블

# 최소값 도출
ans = min(table_1[v1] + table_v1[v2] + table_v2[n],
          table_1[v2] + table_v2[v1] + table_v1[n])

# 출력
if ans>=INF:
    print(-1)
else:
    print(ans)
```