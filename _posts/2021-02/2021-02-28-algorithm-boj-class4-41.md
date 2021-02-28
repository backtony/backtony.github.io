---
layout: post
title: (Python) 백준 15663번 N과 M(9) - class 4
subtitle:   (Python) 백준 15663번 N과 M(9) - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/15663){:target="_blank"}]


## 15663번 N과 M(9)
---
__접근 방법__  
n 개중 m개를 고르고 중복을 제외한 순열을 구하는 문제다.
<br>

__해결__  
1. num 에 숫자를 입력 받는다.
2. permutations로 순열을 받고 set으로 중복을 제거한다.
    - {(),()} 형태로 set은 ()안의 내용물의 순서까지 같은 경우 중복으로 판단하여 제거한다.
3. 리스트로 변환하여 정렬하고 출력한다.


```python
from itertools import permutations

n, m = map(int, input().split())

num = map(int, input().split())
num = set(permutations(num, m))  # 중복 제거
num = list(num)  # 리스트로 만들고
num.sort()

for per in num:
    print(*per)
```