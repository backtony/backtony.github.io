---
layout: post
title: (Python) 백준 2638번 치즈 - class 4
subtitle:   (Python) 백준 2638번 치즈 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/2638){:target="_blank"}]


## 2638번 치즈
---
문제의 핵심은 외부공기와 내부공기를 구분해내는 것이다. 문제 조건에서 치즈는 가장자리에 존재하지 않는다고 했다. 그러므로 어느 가장자리 지점에서 bfs 혹은 dfs를 통해 치즈가 아닌 경우 0이 아닌 다른 숫자로 바꾸면 외부공기와 내부 공기를 분리할 수 있다. 이 아이디어를 핵심으로 설계했다.

1. 모눈종이 정보를 입력받고 치즈의 지점은 큐에 저장한다.
2. (0,0)에서 bfs 혹은 dfs를 통해 외부공기와 내부공기를 분리한다.
3. q가 빌 때까지 반복하는 while문 내부에 q의 길이만큼만 반복하는 while문을 만들어 한 싸이클을 만든다.
4. 큐에서 치즈의 위치를 꺼내 2면 이상 외부공기와 닿으면 3으로 수정하고 changed 리스트에 따로 위치를 저장해둔다. 2면 미만이 닿는 경우는 다시 큐에 넣는다.
    - -1 이외의 수 3으로 수정하는 이유는 바로 -1로 수정해버리는 경우에는 다른 치즈의 지점에서 면을 고려하는데 문제가 발생하기 때문이다.
5. 큐의 길이만큼 반복을 완료하면 changed 리스트에서 지워야할 치즈 위치를 꺼내서 dfs 혹은 bfs를 통해 외부 공기와 내부공기를 다시 분리한다.
6. 큐가 빌 때까지 반복한다.

dfs 또는 bfs 둘 중 선택해서 사용하면 되는데 내가 작성한 코드는 dfs를 사용했으므로 재귀의 깊이를 sys.setrecursionlimit로 모눈종이의 개수만큼 늘려줬다.

```python
from collections import deque
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def dfs(x, y):
    graph[x][y] = -1  # 외부 공기 처리
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        # 모눈종이 내
        if 0 <= px and px < n and 0 <= py and py < m:
            # 외부 공기인 경우
            if graph[px][py] == 0:
                dfs(px, py)


n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
q = deque()
ans = 0  # 최종 걸리는 시간
# 모눈종이 정보 입력
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        # 치즈위치 저장
        if graph[i][j] == 1:
            q.append((i, j))

dfs(0, 0)  # 외부공기 -1로 처리

# 큐가 빌때까지 반복 -> 치즈가 남아있으면 반복
while q:
    length = len(q)
    loop = 0
    changed = []  # 녹는 지점
    ans += 1 # 소요시간
    # 큐의 길이만큼 반복
    while loop < length:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            # 4면 중 외부공기와 닿는 면 개수 확인
            if graph[px][py] == -1:
                cnt += 1

        # 2면 이상 닿으면
        if cnt >= 2:
            graph[x][y] = 3  # 녹음 처리
            changed.append((x, y))
        # 2면 미만 닿으면
        else:
            q.append((x, y))  # 다시 큐에 삽입

        loop += 1
    # 녹는 지점을 기준으로 4방향에 내부공기가 있다면 외부공기로 수정
    # 녹는 지점도 외부공기로 처리
    for x, y in changed:
        dfs(x, y)

print(ans)
```