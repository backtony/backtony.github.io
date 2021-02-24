---
layout: post
title: (Python) 백준 12851번 숨바꼭질 2 - class 4
subtitle:   (Python) 백준 12851번 숨바꼭질 2 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/12851){:target="_blank"}]


## 12851번 숨바꼭질 2
---
### 방법 1

__접근 방법__  
모든 경우를 누적해야하므로 다이나믹 프로그래밍으로 접근했다.  
<br>

__해결__  
+ 동생이 수빈이 왼쪽에 있는 경우
    - 왼쪽으로 이동 방법은 -1뿐이므로 뺄쎔으로 한 번에 처리
+ 동생이 수빈이 오른쪽에 있는 경우
    - 가장 빠른 시간 저장소 dp 테이블, 최소시간 경우의 수 count 테이블 사용
    - 먼저 -1, +1로 이동하는 방법으로 dp와 count 테이블 채우기
    - 2배로 이동하는 방법으로 dp, count 테이블 수정

```python
def solution(n,k):
    # 동생이 수빈이 왼쪽에 있는 경우
    if k<n:
        print(n-k)
        print(1)
        return
    # 동생이 수빈이 오른쪽에 있는 경우

    dp = [0] * (100001)  # 가장 빠른 시간 저장소
    count = [0] * (100001)  # 해당 인덱스로 오는 최소시간 경우의 수
    count[n] = 1 # 경우의 수 누적을 위한 시작점 처리

    # 수빈이 기준 왼쪽으로 -1씩 가는 경우 처리
    start = n - 1
    while start >= 0:
        count[start] = 1 # 왼쪽으로 가는 경우의 수는 단 한 번뿐
        dp[start] = dp[start + 1] + 1
        start -= 1

    # 수빈이 기준 오른쪽으로 +1씩 가는 경우 처리
    start = n + 1
    while start <= k:
        dp[start] = dp[start - 1] + 1
        start += 1

    # 오른쪽으로 2배씩 이동하는 경우 처리
    for i in range(n + 1, k + 1):
        if i % 2 == 0:  # 짝수
            # 2배로 오는 경우와, +1로 오는 경우 중 작은 것 선택
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)

            # 해당 인덱스로 오는 경우의 수 누적
            if dp[i] == dp[i // 2] + 1:
                count[i] += count[i // 2]
            if dp[i] == dp[i - 1] + 1:
                count[i] += count[i - 1]


        else: # 홀수
            # 홀수의 경우 i//2 와 i//2+1 인덱스의 두 배 이동 후 +1, -1 로 i 도착
            dp[i] = min(dp[i // 2 + 1] + 2, dp[i - 1] + 1)

            # 해당 인덱스로 오는 경우의 수 누적
            if dp[i] == dp[i // 2 + 1] + 2:
                count[i] += count[i // 2 + 1]
            if dp[i] == dp[i - 1] + 1:
                count[i] += count[i - 1]

    # 결과 출력
    print(dp[k])
    print(count[k])


n, k = map(int, input().split())
solution(n,k)
```
<br>

### 방법 2
__접근 방법__  
거리 이동 비용이 1인 경우, 특정 위치에서 특정 위치까지 가장 빠른 시간을 구하는 것은 가장 빠른 거리를 구하는 것과 같다. 비용이 1인 그래프 최소 거리는 BFS로 풀이할 수 있으므로 BFS로 접근했다.  
cf) 앞으로 문제가 그래프이론처럼 보이지 않아도 이동하는 문제에서 이동 비용이 1이면 그래프 그래프 이론을 고려해보자.
<br>

__해결__  
BFS는 로직상 꺼내는 순간 첫 방문일 경우 그 값이 최소 값으로 정해진다는 점을 이용한다.
1. 시작점을 처리하고 큐에 시작점 삽입
2. 큐에서 지점을 꺼내서 현재 위치에서 이동가능한 위치 for문 돌리기
    + 첫 방문인 경우 최소 시간 수정, 방문 누적 횟수 수정, 큐에 삽입
    + 최소 시간이 일치하는 경우, 방문 누적 횟수 수정
3. 결과 출력

```python
from collections import deque


def bfs(n):
    # 시작 위치 처리
    dp[n][0] = 0  # 최단 시간
    dp[n][1] = 1  # 최단 시간 방문 횟수

    q = deque()
    q.append(n)

    while q:
        pos = q.popleft()
        for i in [pos + 1, pos - 1, 2 * pos]:
            # 범위 내
            if 0 <= i and i <= 100000:
                if dp[i][0] == -1:  # 첫 방문
                    dp[i][0] = dp[pos][0] + 1  # 최단 시간 수정
                    dp[i][1] = dp[pos][1]  # 방문 횟수 누적
                    q.append(i)  # 탐색 위치 추가

                # 최단 시간 일치
                elif dp[i][0] == dp[pos][0] + 1:
                    dp[i][1] += dp[pos][1]  # 방문 횟수 누적


n, k = map(int, input().split())

# 최단시간, 최단시간으로 방문 횟수
dp = [[-1, 0] for _ in range(100001)]

bfs(n)
print(dp[k][0])
print(dp[k][1])
```