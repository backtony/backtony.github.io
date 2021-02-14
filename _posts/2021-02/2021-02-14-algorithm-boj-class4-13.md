---
layout: post
title: (Python) 백준 1967번 트리의 지름 - class 4
subtitle:   (Python) 백준 1967번 트리의 지름 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1967){:target="_blank"}]


## 1967번 트리의 지름
---
1. 다익스트라 알고리즘을 사용해서 무작위 한 지점에서 가장 먼 지점(트리의 끝)을 찾는다.
2. 찾은 지점에서 다시 다익스트라 알고리즘을 사용해서 가장 먼 지점(트리의 반대편 끝)을 찾는다.

다익스트라 알고리즘 로직의 우선순위 큐에서 pop하는 시점에 뽑히는 지점은 최소거리 계산이 완료된 지점이다. 우선순위 큐는 거리 비용이 작은 순으로 뽑아내기에 pop으로 뽑힌다는 의미는 자신보다 거리 비용이 작은 것들은 다 뽑히고 자신의 차례가 왔다는 뜻으로 시작지점으로부터 자기까지의 최소거리는 결정되었음을 의미한다. 따라서 제일 마지막에 if cost>dis[way]문을 무시하고 들어온 지점은 시작지점에서의 최대 거리 지점을 의미한다. 이 값을 리턴해서 사용하면 된다.

```python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


# 다익스트라 알고리즘
def dijkstra(start):
    dis =[INF]*(n+1)
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    
    # 메인 로직
    while q:
        cost,way = heapq.heappop(q)
        if cost>dis[way]:
            continue
        last_way = way # 시작 지점에서 최대 거리 지점
        last_cost = cost # 시작 지점에서 최대 거리 비용
        for new_cost,new_way in graph[way]:
            if new_cost+cost<dis[new_way]:
                dis[new_way] =new_cost+cost
                heapq.heappush(q,(dis[new_way],new_way))


    return last_cost,last_way


n = int(input())
graph =[[]for _ in range(n+1)]

# 그래프 정보 입력
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

# 무작위 지점 넣어서 제일 멀리있는 지점 찾기 -> 트리의 제일 끝점
temp_cost,temp_way = dijkstra(1)

# 트리의 제일 끝점에서 제일 먼 지점 찾기
ans_cost,ans_way = dijkstra(temp_way)
print(ans_cost)
```