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
첫 시도에서는 일반적인 bfs에서 벽의 위치를 다 받아서 하나씩 벽을 선택해서 없애고 돌리는 것을 반복하는 과정으로 설계했더니 시간초과가 발생했다. bfs 복잡도가 O(V+E)인데 벽을 일일이 선택해서 돌리면 약 100만번을 돌리는 것이므로 당연히 시간초과가 발생한다.  
1차 복습 때 아래와 같이 코드를 설계했지만 3차원 리스트로 해결하면서 visited를 바로 수정하지 않고 cost를 큐에 넘기고 큐에서 꺼낼때 visited를 수정했더니 시간초과가 발생했다. 파이썬은 최적화가 가장 중요하다. __웬만하면 파라미터로 넘겨서 수정을 미루지 말고 가능하다면 바로바로 수정하는게 시간을 절약할 수 있는 것 같다.__
<br>

__해결__  
방문 리스트를 3차원 리스트로 만들어 bfs를 한 번만 수행하면서 벽을 뚫었을 때와 안뚫었을 때를 같이 처리하는 방식으로 설계했다.
```python
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    visited[0][x][y] = 1  # 시작위치 카운트
    q.append((0, x, y))  # 벽 뚫기전, 시작위치 삽입

    while q:
        block, x, y = q.popleft()
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            # 범위 내
            if 0 <= px and px < n and 0 <= py and py < m:
                # 벽이 아니고 방문한적이 없다면
                if graph[px][py] == 0 and visited[block][px][py] == INF:
                    visited[block][px][py] = visited[block][x][y] + 1
                    q.append((block, px, py))

                # 벽이고 한번도 뚫은적 없고 벽이 뚫린 기록이 없다면
                elif graph[px][py] == 1 and block == 0 and visited[1][px][py] == INF:
                    visited[1][px][py] = visited[block][x][y] + 1
                    q.append((1, px, py))

    return min(visited[0][n - 1][m - 1], visited[1][n - 1][m - 1])


n, m = map(int, input().split())
graph = []
# 방문 테이블 ,  0은 벽 안부숨, 1 벽 부숨
visited = [[[INF] * m for _ in range(n)] for _ in range(2)]

# 그래프 정보
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

ans = bfs(0, 0)
if ans == INF:
    print(-1)
else:
    print(ans)
```