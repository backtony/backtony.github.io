---
layout: post
title: (Python) 백준 9465번 스티커 - class 4
subtitle:   (Python) 백준 9465번 스티커 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/9465){:target="_blank"}]


## 9465번 스티커
---
다이나믹 프로그래밍으로 풀이했다.

```python
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    tb = []
    dp = [[0] * n for _ in range(2)] # dp 테이블

    # 그림 정보
    for _ in range(2):
        tb.append(list(map(int, input().split())))

    # dp 테이블 첫 열 처리
    dp[0][0] = tb[0][0]
    dp[1][0] = tb[1][0]

    # 다이나믹 프로그래밍 
    for i in range(1, n):
        dp[0][i] = max(tb[0][i] + dp[1][i - 1], dp[0][i - 1])
        dp[1][i] = max(tb[1][i] + dp[0][i - 1], dp[1][i - 1])

    print(max(dp[0][n - 1], dp[1][n - 1]))
```