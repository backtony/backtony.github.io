---
layout: post
title: (Python) 백준 11725번 트리의 부모 찾기 - class 4
subtitle:   (Python) 백준 11725번 트리의 부모 찾기 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/11725){:target="_blank"}]


## 11725번 트리의 부모 찾기
---
__접근 방법__  
트리 문제이므로 당연히 재귀로 풀어내야 할 것이라고 생각했다.
<br>

__해결__  
1. 1번 노드를 루트로 하므로 루트에서 연결된 자식 노드를 찾는다.
2. 찾은 자식노드를 부모로 하는 자식노드를 찾는다.
3. 위 과정을 반복한다.

```python
import sys

# 재귀를 통해 풀이하므로 재귀 깊이 늘리기
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# root을 부모로하는 자식 노드 찾기
def find(root):
    # 부모 노드에 연결된 자식 노드 찾기
    for idx in graph[root]:
        parent[idx] = root # 찾은 자식노드의 부모를 root로 수정
        graph[idx].remove(root) # 자식 노드의 연결정보에서 부모노드 삭제
        if graph[idx]: # 부모를 삭제하고도 연결정보가 남아있으면 현재 노드를 부모로 하는 자식 노드 찾기
            find(idx)


n = int(input())
parent = [0] * (n + 1)  # 부모 노드 저장
graph = [[] for _ in range(n + 1)] # 연결 정보 저장

# 그래프 정보 입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 루트에 연결된 노드 찾기
for i in graph[1]:
    parent[i] = 1 # 해당 노드의 부모노드를 1로 수정
    graph[i].remove(1) # 해당 노드에 연결정보로 저장된 1번 노드 삭제
    find(i) # 해당 노드를 부모노드로 하는 자식 노드 찾기

for i in parent[2:]:
    print(i)
```