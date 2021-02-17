---
layout: post
title: (Python) 백준 2263번 트리의 순회 - class 4
subtitle:   (Python) 백준 2263번 트리의 순회 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/2263){:target="_blank"}]


## 2263번 트리의 순회
---
+ pre-order : 전위 순회, 루트 -> 왼쪽 -> 오른쪽
+ in-order : 중위 순회, 왼쪽 -> 루트 -> 오른쪽
+ post-order : 후위 순회, 왼쪽 -> 오른쪽 -> 루트

1. 트리 전체에서 보면 후위 순회의 제일 마지막 값은 루트 노드에 해당한다.
2. 중위 순회에서 루트노드에 해당하는 값의 인덱스를 기준으로 보면 왼쪽은 루트노드 기준 왼쪽 서브트리, 오른쪽은 오른쪽 서브 트리에 해당한다.
3. 전위 순회 출력이 목적이므로 현재의 루트를 찍고 왼쪽부터 재귀 반복, 오른쪽 재귀 반복한다.
    - 각각의 서브트리의 루트를 구하는 방식이므로 각각의 서브트리에서 루트를 구해야하므로 인자로 후위순회가 필요하다.
    - 전체 트리를 기준으로 보면 후위 순회에서 맨 마지막 값(루트)을 제외하면 왼쪽서브트리 -> 오른쪽 서브트리 순이다. 따라서 중위 순회를 통해 왼쪽서브트리 노드의 개수를 구하면 후위순회도 왼쪽서브트리, 오른쪽서브트리를 나눌 수 있다.

cf) 노드 개수만큼 재귀를 반복하므로 sys.setrecursionlimit로 재귀 깊이를 늘려줘야 한다.


```python
import sys

# 정점 개수만큼 재귀 깊이 증가
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def pre_order(in_l,in_r,post_l,post_r):
    # 역전되면 구분할 노드가 없는 것
    if in_l>in_r or post_l>post_r:
        return

    root=post_order[post_r]
    print(root, end=" ")

    left = idx[root] - in_l # 왼쪽 개수
    right = in_r - idx[root] # 오른쪽 개수

    # 전위이므로 루트찍고 왼쪽부터
    pre_order(in_l,in_l+left-1,post_l,post_l+left-1)
    # 오른쪽
    pre_order(in_r-right+1,in_r,post_r-right,post_r-1)


n = int(input())
in_order = list(map(int,input().split())) # 중위 순회
post_order = list(map(int,input().split())) # 후위 순회

idx=[0]*(n+1)
# 후위순회의 끝값이 중위순회의 어디 인덱스에 위치한지 확인을 위해
# 중위순회의 값들의 인덱스값을 저장
for i in range(n):
    idx[in_order[i]]=i

pre_order(0,n-1,0,n-1)
```