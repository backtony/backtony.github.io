---
layout: post
title: (Python) 백준 1238번 파티 - class 4
subtitle:   (Python) 백준 1238번 파티 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1238){:target="_blank"}]


## 1238번 파티
---
문제는 그래프 문제고 플로이드 워셜 알고리즘을 사용하면 쉽게 풀 수 있을 거라 생각했지만 주어진 학생이 500명 이상이기 때문에 복잡도를 고려하면 플로이드 워셜 알고리즘은 사용할 수 없다. (참고로 500명 이하의 경우에도 인접 행렬로 주어지면 사용할 수 없다.) 따라서 다익스트라 알고리즘__ 을 생각해냈다. import sys의 경우 10만단위로 넘어가면 사용해야 좋은 것을 알고 있는데 입력 단위가 적을 때 사용하면 오히려 더 오래 걸린다고 알고 있다. 10,000단위의 입력은 판단하기 어려워 사용해서 돌려보고 사용하지 않고 돌려보았는데 __결론적으로는 10,000단위의 입력부터는 sys를 사용하는 것이 더 빠르다.__  
원래 다익스트라 알고리즘을 설계할 때 보통 저장된 최소거리 테이블을(아래 코드에서는 dis)를 반환해서 사용한다. 선택한 시작점에서 도착이 불가능한 지점이 있는 경우 아래와 같이 spot==target에서 return을 해버리면 target에 도달이 불가능한 경우는 while문이 끝나고 none이 리턴되기 때문이다. 하지만 이 문제에서는 조건으로 갈 수 있고 올 수 있는 데이터만 입력된다고 했으므로 굳이 dis에서 모든 지점의 최소거리를 확인할 필요가 없다. 따라서 다익스트라 로직에 우선순위 큐에서 pop으로 꺼내진 위치는 최소거리가 결정된 지점이므로 꺼낸 위치가 target과 일치하면 바로 return 하도록 하여 시간을 단축시켰다.

```python
import sys
import heapq

input = sys.stdin.readline

def dijkstra(start,target):
    dis=[int(1e9)]*(n+1)
    dis[start]=0
    q=[]

    heapq.heappush(q,(0,start))

    # 다익스트라 메인 로직
    while q:
        cost,spot =heapq.heappop(q) # 우선순위 큐에서 뽑히면 이미 최소거리를 저장한 상태
        if spot==target: # 따라서 원하는 곳에 도착시 값을 return
            return cost
        if cost>dis[spot]:
            continue

        for new_cost,new_way in graph[spot]:
            if cost+new_cost<dis[new_way]:
                dis[new_way]=cost+new_cost
                heapq.heappush(q,(dis[new_way],new_way))


# 마을수(학생수), 단방향도로수, 파티 여는 마을
n,m,x = map(int,input().split())
ans=0 # 결과값 저장소
graph=[[] for _ in range(n+1)]

# 그래프 정보
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

# 1부터 n번째 집까지 돌리면서 최대값 구하기
for i in range(1,n+1):
    ans = max(dijkstra(i,x) + dijkstra(x,i),ans)

print(ans)
```