---
layout: post
title: (Python) 백준 9251번 LCS - class 4
subtitle:   (Python) 백준 9251번 LCS - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/9251){:target="_blank"}]


## 9251번 LCS
---
[[LCS 알고리즘 참조](https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EA%B3%B5%ED%86%B5_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4)]  
문자열 중복 문제는 대부분 다이나믹 프로그래밍 문제이다. LCS 최장 공통 부분 수열의 특징은 다음과 같다.  
+ 두 문자열이 같은 문자로 끝나는 경우
    - 두 문자열의 마지막 원소를 제거하고 구한 LCS + 1 과 같다.
+ 두 문자열이 다른 문자로 끝나는 경우
    - MAX (첫 번째 문자열의 마지막 원소를 제거한 것과 두 번째 문자열의 LCS, 두 번째 문자열의 마지막 원소를 제거한 것과 첫 번째 문자열의 LCS)

위 특징을 가지고 LCS 테이블을 만든다.
![그림1](https://backtony.github.io/assets/img/post/algorithm/boj/21-1.PNG)

1. 첫 번째 행과 열은 빈 문자열로 두어서 빈 문자열과 문자열의 LCS를 작성한다. 
2. 두 번째 행부터는 문자열 G와 문자열이 A, AG, AGC, AGCA, AGCAT인 문자열과 LCS를 구한다.
3. 세 번째 행부터는 문자열 GA와 문자열이 A, AG, AGC, AGCA, AGCAT인 문자열과 LCS를 구한다.
    - 실질적으로 비교는 문자열 GA중 A와 각 문자열의 끝 문자만 비교하게 된다. 두 번째 행에서 문자열 끝이 G인 것으로 LCS를 구했으므로 이번에는 문자열 끝이 A인 것으로 LCS를 구하는 과정이다. LCS 특징에 따라 비교하는 과정에서 두 번째 행에서 수행한 문자열 G와 문자열 A, AG, AGC, AGCA, AGCAT의 LCS를 가져다가 사용한다.
    - 예를 들어, GA와 AGC를 비교하는 차례에서는 실질적으로 A와 C만을 비교한다. 이미 전에 G와 AG의 LCS를 구했으므로 추가된 A와 C만을 비교한다. LCS 특징에 따라 서로 다른 문자로 끝나기 때문에 max로 비교해서 전에 구한 결과를 가져와서 사용한다.
4. 과정을 반복하여 dp[n][m]을 출력한다.

```python
# 최대 2000글자로 sys을 사용하는 것이 100ms 더 빠르게 측정되었다.
import sys
input = sys.stdin.readline

a = input().rstrip() # 첫 번째 문자열 가로
b = input().rstrip() # 두 번째 문자열 세로
m = len(a)
n = len(b)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 끝이 같다면
        if b[i - 1] == a[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 끝이 다르다면
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
```