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
__접근 방법__  
문제는 그래프 문제고 플로이드 워셜 알고리즘을 사용하면 쉽게 풀 수 있을 거라 생각했지만 주어진 학생이 500명 이상이기 때문에 복잡도를 고려하면 플로이드 워셜 알고리즘은 사용할 수 없다. (참고로 500명 이하의 경우에도 인접 행렬로 주어지면 사용할 수 없다.) 따라서 __다익스트라 알고리즘__ 을 생각해냈다. import sys의 경우 10만단위로 넘어가면 사용해야 좋은 것을 알고 있는데 입력 단위가 적을 때 사용하면 오히려 더 오래 걸린다고 알고 있다. 10,000단위의 입력은 판단하기 어려워 사용해서 돌려보고 사용하지 않고 돌려보았는데 __결론적으로는 10,000단위의 입력부터는 sys를 사용하는 것이 더 빠르다.__  
<br>

__해결__  
1. 1~n번 집부터 x집 까지의 최소 거리 + x집부터 자기집으로 되돌아가는 최소 거리 중 최대 값을 구하면 된다.
2. 다익스트라 함수를 시작값과 도착값 인자로 받고 도착값이 큐에서 나오면 해당 비용을 반환하도록 설계한다.
    - 문제 조건상 갈 수 있는 데이터만 입력된다고 했고, 다익스트라 알고리즘 로직상 큐에서 나온 순간 자신의 최소 거리 비용은 결정되있다.
3. 결론적으로 점화식은 ans = max(dijkstra(i,x) + dijkstra(x,i),ans) 이다.

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