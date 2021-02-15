---
layout: post
title: (Python) 백준 1991번 트리 순회 - class 4
subtitle:   (Python) 백준 1991번 트리 순회 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1991){:target="_blank"}]


## 1991번 트리 순회
---
ord와 chr 내장함수를 사용하여 A부터 0으로 테이블을 만들었다. 나머지는 재귀로 구현했다.
```python
BLANK = ord('.') - ord('A')  # 자식노드가 없는 경우


# 전위 순회
def front(root):
    global ans_front
    ans_front += chr(root + ord('A'))

    # 왼쪽에 자식 노드가 있다면
    if graph[root][0] != BLANK:
        front(graph[root][0])

    # 오른쪽 자식 노드가 있다면
    if graph[root][1] != BLANK:
        front(graph[root][1])


# 중위 순회
def mid(root):
    global ans_mid
    # 왼쪽에 자식 노드가 있다면
    if graph[root][0] != BLANK:
        mid(graph[root][0])

    ans_mid += chr(root + ord('A'))

    # 오른쪽 자식 노드가 있다면
    if graph[root][1] != BLANK:
        mid(graph[root][1])


# 후위 순회
def back(root):
    global ans_back
    # 왼쪽에 자식 노드가 있다면
    if graph[root][0] != BLANK:
        back(graph[root][0])

    # 오른쪽 자식 노드가 있다면
    if graph[root][1] != BLANK:
        back(graph[root][1])

    ans_back += chr(root + ord('A'))


n = int(input())

graph = [[] for _ in range(26)]
ans_front = ""
ans_mid = ""
ans_back = ""

# 그래프 정보 입력
for _ in range(n):
    a, b, c = input().split()
    graph[ord(a) - ord('A')] = [ord(b) - ord('A'), ord(c) - ord('A')]

front(0)
mid(0)
back(0)
print(ans_front)
print(ans_mid)
print(ans_back)
```