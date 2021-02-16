---
layout: post
title: (Python) 백준 2206번 벽 부수고 이동하기 - class 4
subtitle:   (Python) 백준 2206번 벽 부수고 이동하기 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/2206){:target="_blank"}]


## 2206번 벽 부수고 이동하기
---
__시행 착오__  
첫 시도에서는 일반적인 bfs에서 벽의 위치를 다 받아서 하나씩 벽을 선택해서 반복하는 과정으로 설계했더니 시간초과가 발생했다. bfs 복잡도가 O(V+E)인데 벽을 일일이 선택해서 돌리면 약 100만번을 돌리는 것이므로 당연히 시간초과가 발생한다.  
<br>

__해결__  
방문 리스트를 3차원 리스트로 만들어 bfs를 한 번만 수행하면서 벽을 뚫었을 때와 안뚫었을 때를 같이 처리하는 방식으로 설계했다.
```python
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def bfs(x, y):
    visited[0][x][y] = 1  # 시작 지점 카운트
    q = deque()
    q.append((0, x, y))  # 벽뚫기전, 시작위치 삽입
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        block, x, y = q.popleft()
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            # 범위 내
            if 0 <= px and px < n and 0 <= py and py < m:
                # 벽이 아니고 방문한적 없는곳
                if graph[px][py] == 0 and visited[block][px][py] == -1:
                    visited[block][px][py] = visited[block][x][y] + 1
                    q.append((block, px, py))
                # 벽인데 아직 뚫은 적이 없으면서 해당 지점이 벽을 뚫고 방문한적이 없는 경우
                # bfs는 먼저 나온게 최소거리이므로 이미 방문한적이 있다면 다시 처리할 필요 없음
                elif graph[px][py] == 1 and block == 0 and visited[block + 1][px][py] == -1:
                    visited[block + 1][px][py] = visited[block][x][y] + 1
                    q.append((block + 1, px, py))


n, m = map(int, input().split())

graph = []
# 방문 3차원 리스트
# -1 은 미방문
# visited[][][0] -> 벽뚫기전, [][][1] -> 벽뚫은 후
visited = [[[-1] * m for _ in range(n)] for _ in range(2)]

# 그래프 정보
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

bfs(0, 0)

ans1, ans2 = visited[0][n - 1][m - 1], visited[1][n - 1][m - 1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
elif ans1 == -1 and ans2 == -1:
    print(-1)
else:
    print(min(ans1, ans2))
```