---
layout: post
title: (Python) 백준 10830번 행렬 제곱 - class 4
subtitle:   (Python) 백준 10830번 행렬 제곱 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/10830){:target="_blank"}]


## 10830번 행렬 제곱
---
__접근 방법__  
주어진 곱이 행렬이라서 그렇지 일반적인 수의 b제곱승을 1000으로 나눈 값으로 생각해보면 분할 정복이 떠오른다. 예를 들면 2^10은 2를 10번 곱할게 아니라 2^5를 두 번 곱하면 연산을 거의 절반 가까이 줄이는 것이 분할 정복이다. 이 문제는 단지 수가 행렬로 주어졌을 뿐이다. 정리하면, 무언가에 무수히 많은 제곱승을 한다면 그것은 분할 정복으로 해결할 수 있다.
<br>

__해결__  
분할 정복의 정석적인 풀이는 재귀이다. 앞선 문제에서도 재귀함수에 대해서 설명했었는데 __재귀함수는 함수의 목적을 정하고 그에 따라 값을 반환하도록 설계만 하고 일일이 동작과정을 파고들지 않아야 한다.__ 일일이 재귀를 따라가면 머리만 복잡해질 뿐이다. 예를 들면, 함수의 목적이 a의 반환이라고 한다면 return a 로 만들어 놓고 '이 함수는 a를 반환할거야' 라고 생각하고 더이상 파고들지 않아야 한다.
1. 분할 정복 문제 판단
2. 재귀함수 설계 -> 목적 : a^b 행렬의 각 원소 %1000한 행렬 반환
3. 함수 로직 -> 제곱승의 짝수와 홀수 구분
    - 짝수 : a^(b//2) 제곱
    - 홀수 : a^(b//2) 제곱 * a
    - 각 원소 %1000
4. 결과값을 함수의 목적대로 반환

```python
# 두 행렬의 곱 + 각 원소 %1000 하는 함수
def time(a, b):
    temp = [[0] * n for _ in range(n)]

    # 행렬 * 행렬
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += a[i][k] * b[k][j]
            
            # 각 원소 %1000
            temp[i][j] %= 1000

    return temp


# a^b 행렬의 각 원소 %1000 하는 함수
def solution(a, b):
    # b==1 이면 a의 각 원소에 %1000 한 행렬 반환
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a

    # b가 1이 아니라면 아래 로직을 수행

    # solution 함수는 함수의 설계 목적대로 a^b 행렬의 각 원소 %1000한 뒤 반환해줄 것이다     
    temp = solution(a, b // 2) # a^(b//2) 의 각 원소 %1000 한 행렬 가져오기

    # 짝수라면 a^(b//2) 행렬의 제곱, 각 원소 %1000 행렬 반환
    if b % 2 == 0:        
        return time(temp, temp)
    # 홀수라면 a^(b//2) 행렬의 제곱  X a, 각 원소 %1000 행렬 반환
    else:
        return time(time(temp, temp), a)


n, b = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

answer = solution(matrix, b)
for ans in answer:
    print(*ans)
```