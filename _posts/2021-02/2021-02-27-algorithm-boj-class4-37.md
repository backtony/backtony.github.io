---
layout: post
title: (Python) 백준 15650번 N과 M(2) - class 4
subtitle:   (Python) 백준 15650번 N과 M(2) - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/15650){:target="_blank"}]


## 15650번 N과 M(2)
---
__접근 방법__  
주어진 수 중에서 중복없이 m개만큼 뽑는 문제다. itertools 라이브러리에 combinations 을 생각해 냈다.
<br>

__해결__  
1. num 리스트에 1부터 n까지의 자연수를 만들어 놓는다.
2. combinations로 num에서 m개를 뽑는다.
3. combinations 자체적으로 오름차순으로 뽑아내므로 바로 출력하면 된다.


```python
from itertools import combinations

n, m = map(int, input().split())
num = [x for x in range(1, n + 1)]

for i in list(combinations(num, m)):
    for j in i:
        print(j, end=" ")
    print()
```