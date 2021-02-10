---
layout: post
title: (Python) 백준 1016번 제곱 ㄴㄴ 수 - class 4
subtitle:   (Python) 백준 1016번 제곱 ㄴㄴ 수 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1016){:target="_blank"}]

## 1016번 - 제곱 ㄴㄴ 수
---
접근방식은 매우 간단하다. 주어진 min과 max 범위 안에서 제곱수들의 배수를 제외시켜주고 갯수를 구하면 된다. 하지만 min의 범위가 매우 크기때문에 최적화가 필요하다. 
1. 제곱 ㄴㄴ수를 구하기 위해서는 당연히 제곱수를 먼저 구해야하므로 반복문으로 제곱수를 구한다.  
2. 제곱수의 배수를 곱하기 1부터 구하면 min의 범위가 매우 크기때문에 분명 시간초과가 걸릴 것이다. 따라서 제곱수 * 상수가 min보다 최소한으로 큰 지점으로 바로 접근하는 방법을 찾아야한다.
3. min을 제곱수로 나눈 값을 올림한 뒤 그것을 제곱수에 곱하면 해당 제곱수의 배수 중 min과 max 사이의 값중 최소로 접근할 수 있는 수를 구할 수 있다.
4. 최소로 접근할 수 있는 수부터 배수를 진행해 범위 내 제곱수의 배수들의 값을 0으로 수정한다.
5. 배열에서 1을 카운트한다.

```python
import math
min,max = map(int,input().split())

# min을 0번째 인덱스로
# 초기값은 1로 , 1은 제곱ㄴㄴ수, 0은 제곱수 ㄴㄴ 아닌수
ans = [1]*(max-min+1)
zocopsu=[]

i=2
while i**2<=max:
    zocopsu.append(i**2)
    i+=1

# 제곱수의 배수를 돌리면서 min,max 안에 있는 값들 중 배수인 것 제외시키기
for num in zocopsu:
    # 단순 1부터의 곱으로 진행시 min값이 너무 크므로 시간 초과 발생
    # 한 번에 min과 max 안에 있는 값을 찾는 방법 사용해야함
    # min을 해당 제곱수로 나눠서 올림한 값을 곱한것부터 시작
    j = math.ceil(min/num)
    while num*j<=max:
        ans[num*j-min]=0
        j+=1

print(ans.count(1))
```
