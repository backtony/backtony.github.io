---
layout: post
title: (Python) 백준 14502번 연구소 - class 4
subtitle:   (Python) 백준 14502번 연구소 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/14502){:target="_blank"}]


## 14502번 연구소
---
__접근 방법__  
무난한 완전 탐색 문제로 바이러스가 전염되는 것은 dfs로 방벽의 선택은 combination을 생각해냈다.
<br>

__해결__  
1. 그래프 입력 과정에서 바이러스, 빈칸의 위치는 따로 저장한다.
2. 방벽을 3개씩 선택하는 방법으로 itertools의 combinations 조합을 이용해서 3개씩 뽑아낸다.
3. 매번 뽑아내는 3개씩 마다 바이러스를 전파해야하니 copy로 graph 리스트를 복사해서 새로운 리스트 temp를 만들어 방벽 세우고 바이러스를 전파한 뒤 안전 영역 개수를 검사하고 temp를 버리는 형식을 사용한다. graph에다가 할 경우 바이러스를 전파하고 빼주는 작업까지 해야하기 때문이다.
3. 뽑아낸 위치에 방벽을 설치하고 dfs로 바이러스를 전파시킨다.
4. 안전 영역을 검사하고 max로 이전과 비교하여 저장한다.
5. 결과 출력

```python
from itertools import combinations
import copy


def dfs(x, y):
    temp[x][y] = 2
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        # 범위 내
        if 0 <= px and px < n and 0 <= py and py < m:
            # 바이러스 전파 가능
            if temp[px][py] == 0:
                dfs(px, py)


# 안전 영역 카운트
def check(temp):
    tot = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                tot += 1
    return tot


n, m = map(int, input().split())
ans = 0  # 안전 영역
graph = [[] for _ in range(n)]
blanks = []
virus = []

# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(m):
        # 빈칸 처리
        if graph[i][j] == 0:
            blanks.append((i, j))
        # 바이러스 위치 처리
        if graph[i][j] == 2:
            virus.append((i, j))

# 빈칸 3개 뽑기
for blank in combinations(blanks, 3):
    temp = copy.deepcopy(graph)
    # 방벽 설치
    for x, y in blank:
        temp[x][y] = 1
    # 바이러스 전파
    for x, y in virus:
        dfs(x, y)

    # 안전 영역 카운트
    ans = max(ans, check(temp))

print(ans)
```