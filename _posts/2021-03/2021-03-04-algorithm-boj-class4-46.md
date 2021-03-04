---
layout: post
title: (Python) 백준 18119번 단어 암기 - class 4
subtitle:   (Python) 백준 18119번 단어 암기 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/18119){:target="_blank"}]


## 18119번 단어 암기
---
__접근 방법__  
일단 범위가 매우 크다. 따라서 일일이 문자를 확인하는 것은 불가능하다. 소문자만 입력받으므로 26개의 알파벳 배열을 만들고 입력받는 문자열을 알파벳 단위로 쪼갠 뒤, 해당 알파벳 배열에 현재 문자열의 인덱스를 추가한다. 이러면 알파벳 배열을 확인하면 어떤 문자열이 해당 알파벳을 포함하고 있는지 확인할 수 있다. 또한 문자열이 현재 몇 개의 문자를 잊어버렸는지 확인하는 테이블도 만들어서 잊어버린 문자가 0개일 때와 아닐 때를 구분하는 용도로 사용한다.

<br>

__Pypy3 해결__  
1. 26개의 알파벳 배열 생성
2. 문자열을 입력받아 알파벳 단위로 쪼개고 알파벳 배열에 해당 문자열의 인덱스를 추가
3. o가 1일 경우, 알파벳 x의 배열을 확인하여 해당 문자열이 문자를 처음 잊어버린 경우라면 전체 단어 개수에서 -1, 아니라면 잊어버린 문자 개수만 수정
4. o가 0일 경우, 알파벳 x의 배열을 확인하여 잊어버린 문자 개수를 수정해주고 모두 되찾았다면 전체 단어 개수 +1
5. 전체 단어 개수 출력

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
str = [[] for _ in range(26)]  # 알파벳 배열
forgot = [0] * n  # 잊어버린 문자 개수

# 문자열 입력받아 문자열의 알파벳마다 알파벳 배열에 인덱스 추가
for i in range(n):
    temp = set(input().rstrip())
    for j in temp:
        # i번째 문자열은 해당 알파벳을 포함하고 있다는 표시
        str[ord(j) - ord('a')].append(i)

cnt = n
for _ in range(m):
    o, x = input().split()
    o = int(o)

    # 망각
    if o == 1:
        # 알파벳 x가 들어있는 문자열을 순회
        for i in str[ord(x) - ord('a')]:
            # 잊어버린 문자가 없다면 cnt 수정
            if forgot[i] == 0:
                cnt -= 1
            # 잊어버린 문자 수정
            forgot[i] += 1
    # 되찾음
    else:
        for i in str[ord(x) - ord('a')]:
            forgot[i] -= 1  # 기억 되찾음
            if forgot[i] == 0:  # 모두 되찾으면
                cnt += 1

    print(cnt)
```