---
layout: post
title: (Python) 백준 11660번 구간 합 구하기 5 - class 4
subtitle:   (Python) 백준 11660번 구간 합 구하기 5 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/11660){:target="_blank"}]


## 11660번 구간 합 구하기 5
---
최대 10만번의 합을 구해야 하고 그 과정에서 연산과정이 무수히 많기 때문에 다이나믹 프로그래밍으로 풀어야 한다. 구하고자 하는 것이 (x1, y1)부터 (x2, y2)까지 합이므로 dp 테이블을 (0,0)부터 (x2,y2)까지의 합으로 정하고 설계한다.  
<br>

__해결__  
다이나믹 프로그래밍 문제라고 해서 dp테이블을 항상 누적 덧셈으로 설계하는게 아니다. 문제에서 요구하는 값을 dp 테이블의 목적으로 설계해야 한다. 따라서 dp 테이블은 (0,0)부터 (x2,y2)까지의 합으로 설계해야 한다. 각 행을 누적으로 덧셈한 뒤에 각 열을 누적으로 더하면 dp테이블을 목적에 맞게 채울 수 있다. 문제에서 출력하고자 하는 값은 0,0부터가 아니라 x1,y1부터이므로 이에 맞게 dp에서 찾아서 빼주고, 중복이 있는 경우는 빼고 더해주고 하면 된다.
```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = []
# 행렬 정보 입력
for _ in range(n):
    dp.append(list(map(int, input().split())))

# 각 행의 누적 합
for i in range(n):
    for j in range(1, n):
        dp[i][j] += dp[i][j - 1]

# 각 열의 누적 합
for i in range(1, n):
    for j in range(n):
        dp[i][j] += dp[i - 1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 인덱스 조정
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    # 첫 행, 첫 열
    if y1 == 0 and x1 == 0:
        ans = dp[x2][y2]
    # 첫 행
    elif x1 == 0:
        ans = dp[x2][y2] - dp[x2][y1 - 1]
    # 첫 열
    elif y1 == 0:
        ans = dp[x2][y2] - dp[x1 - 1][y2]
    # 나머지 경우
    else:
        ans = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]

    print(ans)
```
