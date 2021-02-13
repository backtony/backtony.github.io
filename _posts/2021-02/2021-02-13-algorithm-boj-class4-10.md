---
layout: post
title: (Python) 백준 1865번 웜홀 - class 4
subtitle:   (Python) 백준 1865번 웜홀 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1865){:target="_blank"}]


## 1865번 웜홀
---
최단 거리 알고리즘에 관해서 다익스트라, 플로이드워셜, 벨만 포드 알고리즘을 알고 있다. 
+ 다익스트라 알고리즘은 간선의 비용이 음의 경우에는 사용할 수 없다. 
+ 플로이드 워셜의 경우 로직을 수행하고 graph[i][i]가 음수일 경우 음수 사이클이 존재한다는 점을 알 수 있지만, 문제에서 주어진 지점의 수가 500이고 인접 리스트로 주어지는 것 까지는 좋으나 테스트 케이수가 최대 5회이므로 플로이드 워셜 알고리즘으로 설계하면 시간초과가 발생한다. 
+ 결론적으로 벨만 포드 알고리즘을 사용해야한다.

음의 사이클의 경우 플로이드 워셜 알고리즘을 사용할 수 있지만 벨만 포드 알고리즘도 음의 사이클을 확인할 수 있고 복잡도가 벨만 포드가 더 작기 때문에 음의 간선이 존재한다면 벨만 포드 알고리즘을 사용하는 것이 좋다. 벨만 포드 알고리즘에 관한 설명은 [[링크](https://backtony.github.io/algorithm/2020/09/07/algorithm-basics-coding-10/#4-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9C){:target="_blank"}]를 참고하자.
### 틀렸던 풀이(시간 초과)와 이유
정석적인 벨만 포드 알고리즘을 사용했는데 문제에서 시작지점이 주어져있지 않다. 그래서 모든 지점을 시작지점으로 지정해서 돌리면 다른 언어에서는 시간이 적당할지 몰라도 파이썬의 경우는 시간초과가 뜬다. 사실상 이 문제는 시작 지점에 관계없이 음의 사이클이 존재하는지만 판단하면 되는 문제다. 따라서 __모든 지점을 시작 지점으로 둘 필요가 없다.__ 시작지점은 아무곳이나 두고 __dis[cur] != INF 조건을 삭제해주면 된다.__ dis[cur] != INF 조건이 들어간 이유는 bf 함수에 주어진 인자를 시작지점으로 했을 때 이 시작지점으로부터 이어진 노드의 최소 거리를 구하기 위함이었다.(dis[start]=0 초기화 후 dis[cur] != INF조건이 있어야 시작지점부터 연결된 노드를 찾을 수 있기 때문) dis[cur] != INF 조건을 빼주게 되면 시작 지점과 관계없이 알고리즘이 진행되게 되는데 이때 최단 거리 테이블인 dis는 시작지점으로부터의 최단 거리 테이블이라는 원래 의미를 갖지 않게 된다. 그저 음수 싸이클의 존재 유무를 판단하는 테이블이 된다. 따라서 n번째 루프를 돌 때 dis의 테이블의 변화 유무를 통해 음의 싸이클이 있는지만 판단할 수 있는 알고리즘이 되게 되는 것이다.
```python
import sys

input = sys.stdin.readline
INF = int(1e9)


# 벨만 포드 알고리즘
def bf(start):
    dis = [INF] * (n+1)  # 최단거리 초기화
    dis[start]=0
    # 메인 로직
    # 음의 사이클 판별을 위해 n-1번이 아닌 n번 반복
    for i in range(n):
        # 반복마다 모든 간선 확인
        for edge in edges:
            cur = edge[0] # 출발
            next_node = edge[1] # 도착
            cost = edge[2] # 비용

            # 현재 노드에 도달이 가능하면서
            # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if dis[cur] != INF and dis[next_node] > cost + dis[cur]:
                dis[next_node] = cost + dis[cur]
                # i==n-1이면 n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클 존재
                if i == n - 1:
                    return True

    return False


t = int(input())

for _ in range(t):
    # 지점수, 도로수, 웜홀수
    n, m, w = map(int, input().split())
    edges = []

    # 도로 정보
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    # 웜홀 정보
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    key=0
    for i in range(1,n+1):
        if bf(i):
            key=1
            break
    if key:
        print("YES")
    else:
        print("NO")
```
<br>

### 수정한 풀이
```python
import sys

input = sys.stdin.readline
INF = int(1e9)


# 벨만 포드 알고리즘 응용 -> 그래프상 음의 싸이클 존재 판단 함수
def bf(start):
    dis = [INF] * (n+1)  # 최단거리 초기화
    dis[start]=0
    # 메인 로직
    # 음의 사이클 판별을 위해 n번 반복
    for i in range(n):
        # 반복마다 모든 간선 확인
        for edge in edges:
            cur = edge[0] # 출발
            next_node = edge[1] # 도착
            cost = edge[2] # 비용

            
            # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if dis[next_node] > cost + dis[cur]:
                dis[next_node] = cost + dis[cur]
                # i==n-1이면 n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클 존재
                if i == n - 1:
                    return True

    return False


t = int(input())

for _ in range(t):
    # 지점수, 도로수, 웜홀수
    n, m, w = map(int, input().split())
    edges = []

    # 도로 정보
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    # 웜홀 정보
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # bf알고리즘 조건에 dis[cur]!=INF 조건이 없으므로
    # 시작 위치는 아무거나 무관
    # bf는 최단거리 알고리즘이 아닌 음의 싸이클의 판별 유무 판단 알고리즘
    key = bf(1)
    if key:
        print("YES")
    else:
        print("NO")
```