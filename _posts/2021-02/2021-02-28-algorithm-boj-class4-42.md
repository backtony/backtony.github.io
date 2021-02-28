---
layout: post
title: (Python) 백준 15666번 N과 M(12) - class 4
subtitle:   (Python) 백준 15666번 N과 M(12) - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/15666){:target="_blank"}]


## 15666번 N과 M(12)
---
__접근 방법__  
주어진 수를 중복선택해도 되지만 중복된 순열은 제거한다. 오름차순으로 출력한다고 했으므로 순서에 관계없다고 봐야한다. 따라서 조합이고 중복선택이므로 combinatiocombinations_with_replacementns을 생각해냈고 중복된 순열은 set으로 제거해야겠다고 생각했다.
<br>

__해결__  
1. num 리스트에 숫자를 받고 정렬한다.
    - combinations_with_replacement는 첫 파라미터의 첫 인덱스부터 뽑아내므로 오름차순으로 뽑아내기 위해 정렬
2. combinatiocombinations_with_replacementns로 num에서 m개를 뽑는다.
3. set으로 중복을 제거하고 set은 순서에 관계없이 동작하므로 리스트로 만들고 재정렬
4. 출력

```python
from itertools import combinations_with_replacement

n, m = map(int, input().split())

num = list(map(int, input().split()))
# combinations_with_replacement는 첫 파라미터의 첫 인덱스부터 뽑아내므로
# 오름차순으로 뽑아내기 위한 정렬
num.sort()  

num = list(set(combinations_with_replacement(num, m)))  # set으로 중복 제거
num.sort()  # set은 순서에 관계없이 작동하므로 다시 정렬

for ans in num:
    print(*ans)
```