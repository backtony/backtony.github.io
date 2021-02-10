---
layout: post
title: (Python) 백준 1149번 RGB거리 - class 4
subtitle:   (Python) 백준 1149번 RGB거리 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1149){:target="_blank"}]


## 1149번 - RGB거리
---
문제에서 주어진 조건을 보면 점화식을 알려주있기에 비로 다이나믹 프로그래밍을 생각해냈다.  
다이나믹 프로그래밍 문제에서 끝이 정해져있는 경우라면 dp 테이블에 마지막 인덱스에 원하는 값을 가지도록 설계하면 된다. 이 문제의 경우 비용의 최소값을 구해야하므로 각 인덱스 안에는 해당 집까지의 최소비용을 값으로 담고 마지막 인덱스에 담은 값을 출력하면 된다.  
참고로 끝이 정해져있지 않은 다이나믹 프로그래밍 문제는 dp테이블의 첫 인덱스에 구하는 값을 담도록 설계하면 된다.
```python
n = int(input())

dp_red = [0] * n
dp_green = [0] * n
dp_blue = [0] * n

for i in range(n):
    # 빨 초 파 순
    cost = list(map(int, input().split()))
    if i == 0:  # 첫 시작
        dp_red[0] = cost[0]
        dp_green[0] = cost[1]
        dp_blue[0] = cost[2]
        continue

    dp_red[i] = min(dp_blue[i - 1], dp_green[i - 1]) + cost[0]
    dp_green[i] = min(dp_blue[i - 1], dp_red[i - 1]) + cost[1]
    dp_blue[i] = min(dp_red[i - 1], dp_green[i - 1]) + cost[2]

print(min(dp_red[n - 1], dp_blue[n - 1], dp_green[n - 1]))
```