---
layout: post
title: (Python) 백준 12865번 평범한 배낭 - class 4
subtitle:   (Python) 백준 12865번 평범한 배낭 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/12865){:target="_blank"}]


## 12865번 평범한 배낭
---
__접근 방법__  
처음에는 백트래킹으로 풀었는데 시간초과가 발생했다. 그래서 인터넷으로 검색해보니 [냅색 알고리즘](https://ko.wikipedia.org/wiki/%EB%B0%B0%EB%82%AD_%EB%AC%B8%EC%A0%9C) 을 사용해야 했는데 이 알고리즘을 처음 보는 것이라 혼자 풀지 못했다. 공부하고 보니 그냥 다이나믹프로그래밍 문제로 점화식만 잘 세우면 되는 문제였다.
<br>

__해결__  
1. 무게별 최대 가치를 저장할 2차원 dp테이블을 만든다.
    + 첫 줄은 0으로 1부터 k까지 배낭을 채운다.
2. 모든 물건에 대해 허용 무게가 1부터 K까지 배낭에 넣어보면서 dp 테이블을 수정한다.
    + 현재 물건의 무게가 배낭의 허용무게보다 작은 경우, 전에 물건의 결과값을 가져온다.
    + 현재 물건의 무게가 배낭의 허용무게보다 작은 경우, max(현재 물건의 가치 + 이전 물건의 (허용무게-현재물건무게)의 최대 가치, 이전 물건의 허용무게 최대 가치)
        

```python
import sys

input = sys.stdin.readline

# 물건 개수, 버틸 수 있는 무게
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)] # 무게별 최대 가치 저장소

# 모든 물건에 대해서 확인
for i in range(1, n + 1):
    # 무게, 가치
    w, v = map(int, input().split())
    # 무게별 확인
    for j in range(1, k + 1):
        # 현재 물건의 무게가 가방 무게 j보다 무거운 경우
        if w > j:
            dp[i][j] = dp[i - 1][j]  # 전에 물건 결과값 가져오기
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])

print(dp[n][k])
```