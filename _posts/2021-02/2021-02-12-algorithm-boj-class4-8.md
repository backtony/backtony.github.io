---
layout: post
title: (Python) 백준 1753번 최단경로 - class 4
subtitle:   (Python) 백준 1753번 최단경로 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1753){:target="_blank"}]


## 1753번 최단경로
---
다이젝스트라 알고리즘을 사용해서 최단거리 테이블을 반환하여 출력했다. 입력횟수가 최대 30만 번 이상이므로 sys를 사용했다.
```python
import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 비용, 시작위치
    dist = [int(1e9)] * (v + 1)  # 최단거리 테이블
    dist[start] = 0  # 시작지점 처리

    # 메인 로직
    while q:
        prev_cost, prev_pos = heapq.heappop(q)
        if prev_cost > dist[prev_pos]:  # 갱신의 필요가 없는 경우
            continue
        # 간선으로 연결된 지점 확인후 최단거리 갱신
        for new_cost, new_pos in graph[prev_pos]:
            if new_cost + prev_cost < dist[new_pos]:
                dist[new_pos] = new_cost + prev_cost
                heapq.heappush(q, (dist[new_pos], new_pos))

    return dist


v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]

# 그래프 정보
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

ans = dijkstra(start)

# 출력
for i in ans[1:]:
    if i == int(1e9):
        print("INF")
    else:
        print(i)
```