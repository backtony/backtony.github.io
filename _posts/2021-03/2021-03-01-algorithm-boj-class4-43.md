---
layout: post
title: (Python) 백준 16953번 A -> B - class 4
subtitle:   (Python) 백준 16953번 A -> B - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/16953){:target="_blank"}]


## 16953번 A -> B
---
__접근 방법__  
문제를 보고 일반적인 다이나믹프로그래밍 문제라고 생각했으나 범위를 보고 다른 풀이를 생각해야 했다. 범위가 매우 넓다보니 다이나믹 프로그래밍으로 하기에는 시간초과가 나올 것이 분명했기 때문이다. 따라서 큐에 시작 위치를 넣고 빼내면서 b보다 큰 경우 더이상 삽입하지 않고 b보다 작은 경우 가능한 연산 2가지를 하고 다시 큐에 넣는 방식으로 설계했다.
<br>

__해결__  
1. 첫 위치와 비용을 큐에 삽입
2. 큐에서 꺼낸 값이 b보다 큰 경우 무시
3. 큐에서 꺼낸 값이 b와 같은 경우 이전 정답과 비교 min 사용
4. 큐에서 꺼낸 값이 b보다 작은 경우 가능한 2가지 연산 후 다시 큐에 삽입
5. 큐가 빌 때까지 반복하고 정답 출력

```python
from collections import deque

INF = int(1e9)

a, b = map(int, input().split())

ans = INF  # 정답
q = deque()
q.append((a, 0))  # 첫 위치 삽입

while q:
    dp, cnt = q.popleft()
    # dp가 b일 경우 정답 수정
    if dp == b:
        ans = min(ans, cnt)
        continue

    # dp가 b보다 작으면 2배와 1추가 과정후 삽입
    if dp < b:
        q.append((dp * 10 + 1, cnt + 1))
        q.append((dp * 2, cnt + 1))

# 도달 불가능
if ans == INF:
    print(-1)
# 도달 가능
else:
    print(ans + 1)

```