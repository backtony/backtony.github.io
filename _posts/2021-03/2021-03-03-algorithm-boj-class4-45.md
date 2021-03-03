---
layout: post
title: (Python) 백준 17144번 미세먼지 안녕! - class 4
subtitle:   (Python) 백준 17144번 미세먼지 안녕! - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/17144){:target="_blank"}]


## 17144번 미세먼지 안녕!
---
__접근 방법__  
문제에 주어진 조건대로 진행하는 시뮬레이션 문제이다. 그냥 문제에서 주어진 조건대로 코딩해나가면 해결할 수 있다. 이 문제를 보면서 든 생각은 Python으로 제출하면 시간초과가 될 것 같다는 느낌이 들었다. 
<br>

__Pypy3 해결__  
1. 그래프 정보 입력 받기
2. 그래프 정보를 기반으로 청정기 위치 찾기
3. deepcopy로 복사하여 1초 동안 이동한 것을 저장할 temp 배열 만들기
    + 먼지는 모두 동시에 확산된다. 그런데 코딩 과정에서는 하나 하나씩 방문하면서 확산시키므로 graph 배열에서 바로 수정해버리면 1초 동안 원래 확산할 수 없는 먼지양이었는데 수정으로 인해 확산 가능한 먼지 양이 되버릴 수도 있기 때문에 따로 배열을 만들어 처리하고 모든 이동 후에 수정하도록 한다.
4. 1초 동안 이동을 마친 후 temp배열을 다시 graph로 복사하기
5. 위 과정을 t초만큼 반복하고 출력


```python
import copy

# 청정기 위치 찾기
def find_machine():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                return i  # 청정기 위쪽 x좌표 반환


# 미세먼지 확산
def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        # 범위 내
        if 0 <= px and px < r and 0 <= py and py < c:
            # 청정기 위치 제외
            if graph[px][py] != -1:
                temp[px][py] += graph[x][y] // 5  # 확산
                temp[x][y] -= graph[x][y] // 5  # 원위치 값 수정


# 공기청정기에 의한 이동
def machine():
    # 위쪽
    for i in range(machine_x - 1, 0, -1):
        temp[i][0] = temp[i - 1][0]
    for i in range(c - 1):
        temp[0][i] = temp[0][i + 1]
    for i in range(0, machine_x):
        temp[i][c - 1] = temp[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
        temp[machine_x][i] = temp[machine_x][i - 1]
    temp[machine_x][1] = 0

    # 아래쪽
    for i in range(machine_x + 2, r - 1):
        temp[i][0] = temp[i + 1][0]
    for i in range(c - 1):
        temp[r - 1][i] = temp[r - 1][i + 1]
    for i in range(r - 1, machine_x + 1, -1):
        temp[i][c - 1] = temp[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        temp[machine_x + 1][i] = temp[machine_x + 1][i - 1]
    temp[machine_x + 1][1] = 0


# 격자 r*c , t초후
r, c, t = map(int, input().split())

graph = []

# 그래프 정보 입력
for i in range(r):
    graph.append(list(map(int, input().split())))

machine_x = find_machine()  # 공기청정기 위쪽 위치

# t초 동안 반복
for _ in range(t):
    temp = copy.deepcopy(graph)  # 1초 동안의 이동을 담을 배열
    # 배열 순회
    for i in range(r):
        for j in range(c):
            # 5보다 크면 확산
            if graph[i][j] >= 5:
                dfs(i, j)

    machine()  # 공기청정기에 의한 이동
    graph = copy.deepcopy(temp)  # 1초 동안 이동한 배열을 graph에 씌우기

ans = 2
for i in range(r):
    ans += sum(graph[i])

print(ans)
```