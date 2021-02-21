---
layout: post
title: (Python) 백준 11404번 플로이드 - class 4
subtitle:   (Python) 백준 11404번 플로이드 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/11404){:target="_blank"}]


## 11404번 플로이드
---
무난한 플로이드 워셜 알고리즘 문제다.

```python
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 0 처리
for i in range(n + 1):
    graph[i][i] = 0

# 간선 입력 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 플로이드워셜 로직
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# INF인 부분 0으로 바꿔서 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
```