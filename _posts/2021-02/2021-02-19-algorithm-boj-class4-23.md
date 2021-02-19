---
layout: post
title: (Python) 백준 9663번 N-Queen - class 4
subtitle:   (Python) 백준 9663번 N-Queen - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/9663){:target="_blank"}]


## 9663번 N-Queen
---
백트래킹 문제인데 대각선과 위아래가 겹치지 않는지 한 번에 처리하는 것이 중요하다. 따라서 정사각 보드판의 특성을 알고 있어야 한다.
+ 오른쪽 대각선 : x - y + n - 1 결과값이 같다면 같은 오른쪽 대각선 상
+ 왼쪽 대각선 : x + y 결과값이 같다면 같은 왼쪽 대각선 상
+ 같은 행 : 같은 x값
+ 같은 열 : 같은 y값

문제 조건에서 N * N 보드판에 N개의 퀸을 놓는다고 했다. 퀸은 같은 행에 존재할 수 없기 때문에 모든 행에 1개씩 퀸을 놓아야 한다. 따라서 행을 인자로 넘기면서 설계하면 된다.


cf) 백트래킹 문제는 타 언어보다 느리다는 파이썬의 특성상 __PyPy3를 사용__ 해야 한다.


```python
def solution(i):
    global ans
    if i == n: # 마지막 행까지 도달하면 
        ans += 1
        return

    for j in range(n):
        # 모두 False 여야 조건문 실행
        if not (column[j] or dekak_r[i + j] or dekak_l[i - j + n - 1]):
            # 현재 행에서 퀸 위치 선택
            column[j] = dekak_r[i + j] = dekak_l[i - j + n - 1] = True

            solution(i + 1) # 다음 행으로 이동

            # 현재 행 퀸 위치 제거
            column[j] = dekak_r[i + j] = dekak_l[i - j + n - 1] = False


n = int(input())
ans = 0
dekak_r = [False] * (2 * n - 1) # 오른쪽 대각선 
dekak_l = [False] * (2 * n - 1) # 왼쪽 대각선
column = [False] * n # 열

solution(0) # 행을 인자로 넣기
print(ans)
```