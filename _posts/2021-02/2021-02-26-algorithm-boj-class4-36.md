---
layout: post
title: (Python) 백준 14938번 서강그라운드 - class 4
subtitle:   (Python) 백준 14938번 서강그라운드 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/14938){:target="_blank"}]


## 14938번 서강그라운드
---
__접근 방법__  
각각의 지점들에서 모든 지점에 대한 최단 거리를 알아야 수색 범위 내에 있는지 확인할 수 있다. 따라서 모든 지점에서 모든 지점까지의 최단 거리를 구하는 플로이드 워셜 알고리즘을 생각해냈다.
<br>

__해결__  
1. 플로이드 워셜 알고리즘 만들기
2. 시작지점에서 도달지점까지의 거리가 수색 범위 내이면 아이템 회수하기
3. 2번을 반복하여 최대 개수를 구하고 출력한다.

```python
INF = int(1e9)

# 지역, 수색범위, 길의 개수
n, m, r = map(int, input().split())
# 아이템 개수
items = list(map(int, input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]
ans = 0

# 같은 지점 0처리
for i in range(1, n + 1):
    graph[i][i] = 0

# 그래프 정보
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 시작 지점
for i in range(1, n + 1):
    temp = 0
    # 방문 지점
    for j in range(1, n + 1):
        # 수색 범위 내
        if graph[i][j] <= m:
            # 아이템 회수
            temp += items[j - 1]

    # 이전 시작 지점들과 비교
    ans = max(ans, temp)

print(ans)
```