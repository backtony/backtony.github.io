---
layout: post
title: (Python) 백준 15657번 N과 M(8) - class 4
subtitle:   (Python) 백준 15657번 N과 M(8) - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/15657){:target="_blank"}]


## 15657번 N과 M(8)
---
__접근 방법__  
주어진 수 중에서 중복을 포함해서 m개만큼 뽑는 문제다. 순열같아 보이지만 문제 조건이 오름차순이고 중복 출력이 안되기때문에 중복조합과 같다. itertools 라이브러리에 combinations_with_replacement 중복조합을 생각해 냈다.
<br>

__해결__  
1. num 리스트에 숫자를 받고 정렬한다.
2. combinatiocombinations_with_replacementns로 num에서 m개를 뽑는다.
3. combinations num의 앞에서부터 차례로 뽑아내는데 num이 현재 오름차순이므로 오름차순으로 뽑혀 나온다.
4. 출력

```python
from itertools import combinations_with_replacement

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

for i in combinations_with_replacement(num, m):
    for j in i:
        print(j, end=" ")
    print()
```