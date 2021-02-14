---
layout: post
title: (Python) 백준 1786번 찾기 - class 4
subtitle:   (Python) 백준 1786번 찾기 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1786){:target="_blank"}]


## 1786번 찾기
---
kmp 알고리즘을 사용했다. kmp 알고리즘은 찾고자 하는 패턴 문자열 p 안에 접두사와 접미사의 중복이 있는 때 대상과 비교하는 도중에 틀린 경우, 대상 문자열의 인덱스를 하나 증가시키고 패턴 문자열의 인덱스를 처음부터 다시 비교하는게 아니라 패턴 문자열의 중복지점 이후부터 검색을 시작하기 때문에 검색 시간을 단축시킬 수 있다. 일일이 비교하면 문자열의 길이가 n(찾을 대상의 전체 길이), m(패턴 길이)이라면 복잡도가 O(mn)이지만, kmp알고리즘을 사용하면 최악의 경우가 O(n)이다.
```python
# 패턴 문자열의 접두사 접미사 중복 테이블 만들기
def duptable(p):
    n = len(p)
    # 해당 인덱스까지의 문자열에서 중복된 접두,접미사의 개수 저장
    table = [0] * n  

    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
            # 이전까지는 일치했다가 현재 불일치가 발생
            # 방금 전까지는 접미사와 접두사가 일치했음
            # 방금 전까지의 일치개수를 가져오면 다음 비교 시작 위치를 알수있음
            # 예를들면 방금 전까지 일치 개수가 3개였다면
            # table[j-1] 은 3이었을것이고 j=3으로 수정하면            
            # 인덱스가 3이면 사실상 4번째 문자열을 의미함
            # 따라서 패턴 접미사 3개를 띄어넘고 4번째 문자열과 i번째 문자열을 비교하게 됨
            # 즉 j=table[j-1]로 수정하면 
            # j는 중복 이후의 비교할 시작 문자열의 위치를 가리키게 된다.            
            

        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table


def kmp(s, p):
    j = 0  # 패턴 인덱스
    cnt = 0
    pos = []
    for i in range(len(s)):
        # 비교 중간에 틀린 경우
        # j==0이거나 다음 시작점이 같은 문자를 가리킬때까지 반복
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]

        if s[i] == p[j]:
            j += 1
            if j == len(p):  # 일치 패턴을 찾음
                cnt += 1
                pos.append(i - len(p) + 2)
                j = table[j - 1]  # j를 끝값으로 했을 때 접두,접미 중복 개수 -> 비교시작위치

    return cnt, pos


s = input()
p = input()
table = duptable(p)

answer, positions = kmp(s, p)
print(answer)
print(*positions)
```