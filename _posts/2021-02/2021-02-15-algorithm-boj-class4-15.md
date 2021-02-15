---
layout: post
title: (Python) 백준 2096번 내려가기 - class 4
subtitle:   (Python) 백준 2096번 내려가기 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/2096){:target="_blank"}]


## 2096번 내려가기
---
처음에는 일반적인 다이나믹 프로그래밍으로 설계했었는데 메모리 초과가 메모리 부분만 수정했다. 보통의 다이나믹 프로그래밍 설계에서는 입력정보와 같은 크기로 dp테이블을 만들어 놓고 진행하는데 주어진 메모리 한계가 매우 작다보니 데이터를 받고서 계속 저장해두지 않고 바로 처리하는 형식으로 설계했다.

```python
import copy
import sys

input = sys.stdin.readline

n = int(input())

# 그래프 정보 입력
for i in range(n):
    # 첫 입력
    if i == 0:
        dp_max = list(map(int, input().split()))
        dp_max = copy.deepcopy(dp_max)
        dp_min = copy.deepcopy(dp_max)
    else:
        new = list(map(int, input().split()))
        a, b, c = dp_max[0], dp_max[1], dp_max[2]  # 이전 dp저장
        dp_max[0] = new[0] + max(a, b)
        dp_max[1] = new[1] + max(a, b, c)
        dp_max[2] = new[2] + max(b, c)

        a, b, c = dp_min[0], dp_min[1], dp_min[2]  # 이전 dp저장
        dp_min[0] = new[0] + min(a, b)
        dp_min[1] = new[1] + min(a, b, c)
        dp_min[2] = new[2] + min(b, c)

print(max(dp_max), min(dp_min))
```