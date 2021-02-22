---
layout: post
title: (Python) 백준 11779번 최소비용 구하기 2 - class 4
subtitle:   (Python) 백준 11779번 최소비용 구하기 2 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/11779){:target="_blank"}]


## 11779번 최소비용 구하기 2
---
__접근 방법__  
그래프의 최소 비용을 구하는 문제에서 음의 간선이 없고, 하나의 특정 지점에서 하나의 특정 지점까지의 최소비용이므로 다익스트라 알고리즘을 생각했다. 최소비용만 구하는 것이면 다익스트라 알고리즘만으로 해결할 수 있는데 최소비용의 경로까지 구해야 한다. 따라서 단순히 다익스트라 알고리즘만이 아니라 경로를 저장하는 리스트를 따로 생성해야 한다.
<br>

__해결__  
1. 다익스트라 알고리즘을 사용
2. 다익스트라 메인 로직에서 최단 거리가 수정되는 경우 먼저 최단 경로 테이블에 자기 자신을 추가한다.
    - 자신의 최단 거리가 수정되었다면 자신을 통해서 도달하는 지점들도 최단 거리가 수정될 수 있다. 그 지점들의 최단 거리가 수정된다면 경로도 수정해줘야 한다. 그 경로는 현재 자신까지 도달한 최단 경로에서 자기 자신을 추가한 것이 수정되는 지점의 최단 경로가 된다.
3. 자기 자신을 통해 최단 거리가 수정되는 경우가 있다면 앞서 자신의 최단 경로에 자기 자신을 추가한 경로로 수정한다.
4. 다익스트라 알고리즘의 우선순위 큐에서 뽑힌 지점이 처음 뽑힌 지점인 경우, 이미 해당 지점에 대한 최단 거리는 정해진 상태이므로 그 지점이 도착지점과 일치하면 return

cf) 최단 경로 저장할 때 이전의 경로를 =으로 대입해버리면 참조값이 대입된다. 만약 이렇게 한 상태에서 append하면 참조값이 엮인 경로 전체에 영향을 주기 때문에 deepcopy로 따로 만들어주거나, for문을 돌리면서 하나씩 append해줘야 한다.


```python
import sys
import heapq
import copy

input = sys.stdin.readline
INF = int(1e9)


# 다익스트라 함수
def dijkstra(start):
    dis = [INF] * (n + 1) # 최소 비용 테이블
    dis[start] = 0 # 시작 지점 0 처리
    q = []
    heapq.heappush(q, (0, start)) 

    # 메인 로직
    while q:
        now_cost, now_way = heapq.heappop(q)

        if dis[now_way] < now_cost:
            continue

        # 최단 거리가 갱신되는 경우라면 
        # 자기 자신을 통해 다른 곳으로 가는 지점의 경로 처리를 위해
        # 자기 자신 경로 테이블에 자기 자신 추가
        path[now_way].append(now_way)

        # 우선순위 큐에서 뽑은 것이 end와 일치하면 return
        if now_way == end:
            return dis[end]

        # 최단 거리 수정
        for new_cost, new_way in graph[now_way]:
            if dis[new_way] > new_cost + now_cost:
                dis[new_way] = new_cost + now_cost
                heapq.heappush(q, (dis[new_way], new_way))
                # 최단 거리 수정으로 인해 최단 경로 수정                
                path[new_way] = copy.deepcopy(path[now_way])
               


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)] # 인접 리스트
path = [[] for _ in range(n + 1)] # 경로 저장

# 그래프 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

# 시작점 도착점
start, end = map(int, input().split())
print(dijkstra(start)) # 최소 비용 출력
print(len(path[end])) # 경로 길이
print(*path[end]) # 경로 출력
```