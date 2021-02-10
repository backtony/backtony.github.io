---
layout: post
title: (Python) 백준 1167번 트리의 지름 - class 4
subtitle:   (Python) 백준 1167번 트리의 지름 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1167){:target="_blank"}]


## 1167번 - 트리의 지름
---
트리의 지름에 관한 내용을 처음 공부해서 시간이 좀 걸렸지만, 방법만 알면 매우 쉬운 문제다.  
1. 아무 노드를 하나 잡아서 그 노드에서의 최대 거리에 있는 노드를 찾는다. 그 노드를 v라고 하자.
2. v에서 최대 거리에 있는 노드를 찾는다. 그 노드를 u라고 하자.
3. u와 v사이의 거리가 트리의 지름이다.  

__코드레벨에서 sys를 반드시 사용해야 한다.__ 최대 10만개의 노드가 주어지고 그에 따른 간선도 엄청나게 많이 주어지기 때문에 입력횟수가 매우 많다. 이럴 때 파이썬의 경우 import sys를 사용해서 입력받지 않으면 시간차이가 엄청 크게 발생한다.  
처음에는 무슨 소리인지 이해가 안됬으나 문제에서 주어진 예시를 그래프로 그려보니 쉽게 이해가 됬다.
```python
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

# 인접 리스트 만들기
for i in range(1, n + 1):
    temp = list(map(int, input().rstrip().split()))
    start = temp[0]
    k = 1
    while 1:
        to = temp[k]
        if to == -1:
            break
        cost = temp[k + 1]
        graph[start].append((cost, to))
        k += 2


def bfs(start):
    q = deque()
    q.append((0, start))
    dis = [-1] * (n + 1) # -1은 아직 방문하지 않은 곳
    dis[start] = 0
    while q:
        now_cost, v = q.popleft()
        for new_cost, to in graph[v]:
            if dis[to] == -1:  # 방문하지 않은 곳 거리값으로 수정
                dis[to] = now_cost + new_cost
                q.append((dis[to], to))
    ans = max(dis) # start로부터 최대 거리에 있는 노드와의 거리
    idx = dis.index(ans) # start로부터 최대 거리에 있는 노드 번호
    return ans, idx


ans = bfs(1)[1] # 임의의 노드에서 최대 거리에 있는 노드 v 찾기
ans = bfs(ans)[0] # v와 u사이의 거리

print(ans)
```