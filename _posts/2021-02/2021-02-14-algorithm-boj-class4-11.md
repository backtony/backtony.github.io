---
layout: post
title: (Python) 백준 1916번 최소비용 구하기 - class 4
subtitle:   (Python) 백준 1916번 최소비용 구하기 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1916){:target="_blank"}]


## 1916번 최소비용 구하기
---
다익스트라 알고리즘을 사용했다.

```python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dis =[INF]*(n+1)
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    # 메인 로직
    while q:
        cost,way = heapq.heappop(q)
        # 갱신이 필요 없는 경우
        if cost>dis[way]:
            continue

        # 갱신이 필요한 경우
        for new_cost,new_way in graph[way]:
            if new_cost+cost<dis[new_way]:
                dis[new_way] =new_cost+cost
                heapq.heappush(q,(dis[new_way],new_way))

    return dis[end]



n = int(input())
m = int(input())

# 그래프
graph =[[] for _ in range(n+1)]

# 그래프 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

start,end = map(int,input().split())

print(dijkstra(start))
```