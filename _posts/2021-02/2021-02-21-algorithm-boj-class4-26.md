---
layout: post
title: (Python) 백준 11053번 가장 긴 증가하는 부분 수열 - class 4
subtitle:   (Python) 백준 11053번 가장 긴 증가하는 부분 수열 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/11053){:target="_blank"}]


## 11053번 가장 긴 증가하는 부분 수열
---
무난한 다이나믹 프로그래밍 문제다. 주어진 배열에서 해당 인덱스의 값까지를 수열의 최대값으로 정하여 그 값을 최대값으로 하는 수열의 길이를 dp테이블에 저장하는 방식으로 설계했다. 입력횟수가 최대 2000번이라 sys를 써야하는지 잘 모르겠어서 둘 다 제출해봤는데 쓰지 않는게 더 빠른 속도를 보여줬다. 5000번 이상 정도부터 sys.stdin.readline을 사용하는게 좋을 것 같다.
```python
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n  # 수열에서 자기 자신을 포함

for i in range(n):
    for j in range(i):
        # i보다 앞선 인덱스 value 값보다
        # i인덱스의 value가 더 큰 경우 수열의 길이 수정
        if a[j] < a[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
```