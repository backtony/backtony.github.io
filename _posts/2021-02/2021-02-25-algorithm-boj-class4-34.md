---
layout: post
title: (Python) 백준 13549번 숨바꼭질 3 - class 4
subtitle:   (Python) 백준 13549번 숨바꼭질 3 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/13549){:target="_blank"}]


## 13549번 숨바꼭질 3
---
__접근 방법__  
가중치가 있는 그래프 문제와 같다. 보통 가중치가 일치하는 경우 BFS를 사용하는데, 이 문제는 가중치가 다른 부분이 존재하므로 다익스트라 알고리즘을 이용해서 풀이 했다.
<br>

__해결__  
1. 최소 시간 저장소 dp 테이블 만들기
2. 동생이 수빈이 왼쪽에 있는 경우는 뺄셈으로 처리
3. 동생이 수빈이 오른쪽에 있는 경우    
    + 2배 이동과 -1,1 이동은 가중치가 다르므로 구분해서 우선순위 큐에 삽입
    + 우선순위 큐에 의해 뽑힌 위치가 처음 뽑힌 위치라면 현재 뽑은 시간이 해당 위치에 도달하는데 최소 시간으로 판단하여 값 수정하고 큐에 다시 삽입
4. 결과 출력

```python
import heapq

INF = int(1e9)


def solution(n, k):
    # 동생이 수빈이 왼쪽에 있는 경우
    if k <= n:
        print(n - k)
        return

    # 동생이 수빈이 오른쪽에 있는 경우
    dp = [INF] * (100001)
    q = []

    heapq.heappush(q, (0, n))  # 시작 위치 삽입

    # 메인 로직
    while q:
        cost, pos = heapq.heappop(q)
        for i in [pos * 2, pos - 1, pos + 1]:
            # 범위 내
            if 0 <= i and i <= 100000:
                # 2배 이동, 첫 방문
                if i == pos * 2 and dp[i] == INF:
                    heapq.heappush(q, (cost, i))
                    dp[i] = cost
                # -1,+1 이동, 첫 방문
                elif dp[i] == INF:
                    heapq.heappush(q, (cost + 1, i))
                    dp[i] = cost + 1

    print(dp[k])


n, k = map(int, input().split())

solution(n, k)
```