---
layout: post
title: (Python) 백준 2407번 조합 - class 4
subtitle:   (Python) 백준 2407번 조합 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/2407){:target="_blank"}]


## 2407번 조합
---
다이나믹 프로그래밍으로 풀이했다. 팩토리얼마다 계산하면 시간이 오래 걸린다. nCm이라는 조합 자체가 n팩토리얼의 결과값 내에서 계산이 이루어지기 때문에 n까지의 팩토리얼을 계산해서 저장해두고 사용하면 된다. 이때 n까지의 팩토리얼을 구할 때 다이나믹 프로그래밍을 사용하여 이전의 계산 결과값을 가져와서 다시 재활용하는 방식으로 설계했다.
```python
def factorial(n):
    if dp[n] != 1:
        return dp[n]

    # 메인 로직
    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]


n, m = map(int, input().split())
dp = [1] * (n + 1)

print(factorial(n)//(factorial(m)*factorial(n-m)))
```