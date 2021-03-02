---
layout: post
title: (Python) 백준 17070번 파이프 옮기기1 - class 4
subtitle:   (Python) 백준 17070번 파이프 옮기기1 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/17070){:target="_blank"}]


## 17070번 파이프 옮기기1
---
__접근 방법__  
이 문제는 완전탐색 문제다. 따라서 DFS, BFS 중 익숙한 BFS로 설계했는데 시간초과가 발생했다. Python에서 BFS를 구현할 때 보통 Queue를 이용해서 구현한다. BFS는 원래 같은 정점을 한 번 방문해야하는 알고리즘인데 Queue를 이용하면 사실상 같은 정점을 여러 번 방문하고 visited 리스트를 따로 만들어서 방문 여부를 확인하면서 진행한다. 따라서 DFS에 비해 시간이 더 많이 소요된다. Python은 다른 언어보다 느린 언어이다. 따라서 완전탐색의 문제에서 BFS와 DFS를 선택해야한다면 DFS를 선택하는 것이 옳은 선택이다. 하지만 이 문제에서는 DFS로 풀이해도 pypy3로 제출하지 않는 이상 시간초과가 발생한다. __정리하자면, Python으로 완전탐색을 풀어야 할 경우 범위가 매우 작으면 DFS로 풀이하되 범위가 크다면 다이나믹 프로그래밍으로 풀어야 한다.__
<br>

__Pypy3 DFS 해결__  
처음 풀이할 때는 주어진 보드판의 가장자리에 1을 붙여서 보드판을 나가는 범위를 1로 구분했는데 파이썬의 경우 최적화가 필요하므로 왠만하면 벽을 세우기 보다는 그대로 진행하는게 더 좋은 방법인것 같다.
```python
def dfs(pos):
    global cnt
    x, y, z = pos

    # n,n 도달
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    # 가로 세로 대각선의 경우 대각선 이동
    if x + 1 < n and y + 1 < n:
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs((x + 1, y + 1, 2))

    # 가로 대각선의 경우 가로 이동
    if z == 0 or z == 2:
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs((x, y + 1, 0))

    # 세로 대각선의 경우 세로 이동
    if z == 1 or z == 2:
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs((x + 1, y, 1))


n = int(input())
graph = [[] for _ in range(n)]
cnt = 0
# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

# x,y,현재방향
dfs((0, 1, 0))

print(cnt)
```
<br>

__Python dp해결__  
```python
n = int(input())
graph = [[] for _ in range(n)]

# 0은 가로, 1은 세로, 2는 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

dp[0][0][1] = 1  # 첫 시작 위치

# dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        # 현재위치가 대각선인 경우
        if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if graph[r][c] == 0:
            # 현재 위치가 가로인 경우
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            # 현재 위치가 세로인 경우
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))
```