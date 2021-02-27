---
layout: post
title: (Python) 백준 15654번 N과 M(5) - class 4
subtitle:   (Python) 백준 15654번 N과 M(5) - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/15654){:target="_blank"}]


## 15654번 N과 M(5)
---
__접근 방법__  
주어진 수 중에서 순열을 구하는 문제다. itertools 라이브러리에 permutations 순열을 생각해 냈다.
<br>

__해결__  
1. num 리스트에 n개의 수를 입력받는다.
2. permutations로 num에서 m개를 뽑는다.
3. 오름차순 출력을 위해 리스트로 만들고 sort 정렬한다.
4. 츨력한다.


```python
from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

per = list(permutations(num, m))
per.sort()

for i in per:
    for j in i:
        print(j, end=" ")
    print()
```