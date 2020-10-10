---
layout: post
title:  DFS/BFS 기출문제
subtitle:   DFS/BFS 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 간단 정리](#1-간단-정리)
  - [2. 특정한 거리의 도시 찾기](#2-특정한-거리의-도시-찾기)
  - [3. 연구소](#3-연구소) 
  - [4. 경쟁적 전염](#4-경쟁적-전염)
  - [5. 괄호 변환](#5-괄호-변환)
  - [6. 연산자 끼워 넣기](#6-연산자-끼워-넣기)
  - [7. 감시 피하기](#7-감시-피하기)
  - [8. 인구 이동](#8-인구-이동)
  - [9. 블록 이동하기](#9-블록-이동하기)


## 1. 간단 정리
---
+ 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
+ 자료구조 : 데이터를 표현하고 처리하는 방법
+ 스택 : 선입후출, 후입선출구조이며 박스 쌓기에 비유 가능
+ 큐 : 선입선출구조로 공정한 자료구조라고도 한다. 대기 줄에 비유 가능
+ DFS : Depth-First Search, 깊이 우선 탐색 알고리즘이며 그래프를 탐색하는 알고리즘이다. 최대한 얼리 있는 노드를 우선으로 탐색하는 방식으로 동작하며 스택자료구조를 이용
+ BFS : 너비우선 탐색으로 가까운 노드부터 탐색하는 알고리즘이다. 큐를 이용하면 효과적으로 구현 가능

<br>

## 2. 특정한 거리의 도시 찾기
---
[문제 클릭](https://www.acmicpc.net/problem/18352){: target="_blank"}

### 내가 작성한 코드
```python
import sys
import heapq
input = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
INF = int(1e9) # 무한

shortcut = [INF]*(n+1) # 각 도시의 최단 경로
graph =[[] for _ in range(n+1)] # 도시별 연결 정보
q=[] # 우선순위 큐

# 도로 정보 입력
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

# 출발지점 정보 수정 및 우선순위 큐
shortcut[x] = 0
heapq.heappush(q,(0,x))

# 최소 거리 구하기
while q:
    distance, now = heapq.heappop(q)
    # 이미 처리된 경우는 무시 , 첫 시작의 경우가 등호에 해당하므로 등호는 뺀다
    if distance > shortcut[now]:
        continue
    for way in graph[now]: # now에 연결된 도시들
            # 갱신이 필요한 경우
            if distance + 1 < shortcut[way]:
                shortcut[way] = distance+1
                heapq.heappush(q,(shortcut[way],way))

cnt=0
for i in range(1,n+1):
    if shortcut[i] == k:
        print(i)
        cnt+=1
if cnt == 0:
    print(-1)
```
한 가지 출발지점이 정해진 경우에 대해서 각 지점에 대해 최소 거리를 구하는 다익스트라 알고리즘을 사용했다. 다익스트라 알고리즘의 복잡도는 선형로그시간 O(ElogV)이므로 주어진 큰 범위에 적합한 알고리즘이다. (V는 노드, E는 간선, 우선순위 큐로 인해 logV)
<br>

### 모범 답안
그래프에서 __간선비용이 모두 동일할 때는 BFS__ 를 이용하여 최단 거리를 찾을 수 있다.  
문제 조건에서 노드의 개수 N은 최대 300,000개이며 간선의 개수 M은 최대 1,000,000개이다. 따라서 BFS를 이용해 O(N+M)으로 동작하는 소스 코드를 작성하여 시간 초과 없이 해결할 수 있다.(선형 시간 알고리즘에서는 천만까지 범위가 가능하다.) 먼저 특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한 뒤, 각 최단 거리를 하나씩 확인하며 그 값이 K인 경우에 해당 도시의 번호를 출력하면 된다.  
간선 정보에서 각각의 거리가 다르다면 다익스트라를 써야하지만, 비용이 모두 같다면 시작지점으로부터 연결되있는 차례대로 비용을 계산하면 최소거리가 되기 때문에 BFS를 사용해도 된다.  
다익스트라의 경우는 간선비용이 다를 때 같을 때 모두 사용할 수 있다. 그래서 나는 다익스트라를 알아두는게 좋을 것 같다는 생각이 든다. BFS와 코드도 매우 비슷하다. 단지 큐 대신 우선순위 큐를 사용한다는 점 이외에는 BFS와 비슷하다.
```python
import sys
from collections import deque

n, m, k, x = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)  # 최단 거리
distance[x] = 0  # 시작위치 0
# 간선 정보 입력
for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

q = deque([x])
while q:
    now = q.popleft()
    # 현재 위치에서 연결되어있는 노드
    for way in graph[now]:
        # 최단 거리 갱신이 안되어있다면
        if distance[way] == -1:
            # 최단거리 갱신
            distance[way] = distance[now] + 1
            # 큐 삽입
            q.append(way)

cnt = False  # k있는지 판단할 변수
for i in range(1, n + 1):
    if distance[i] == k:
        cnt = True
        print(i)
if cnt == False:
    print(-1)
```

## 3. 연구소
---
[문제 클릭](https://www.acmicpc.net/problem/14502){: target="_blank"}  

### 모범 답안
이 문제는 벽을 3개 설치하는 모든 경우의 수를 다 계산해야 한다. 간단하게 생각해보면 전체 맵의 크기가 8 * 8 이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우 (바이러스가 하나도 존재하지 않는 경우) 64C3이 될 것이다. 이는 100,000보다도 작은 수이므로, 대략 선형 로그 시간의 알고리즘을 설계하면 되는데 주요 풀이 알고리즘이 BFS/DFS 이므로 인접 리스트를 사용하면 선형 시간 알고리즘으로 풀이할 수 있다. 따라서 모든 경우의 수를 고려해도 제한 시간 안에 문제를 해결할 수 있다는 것을 알 수 있다.  
또한 모든 조합을 계산할 때는 파이썬의 조합 라이브러리를 사용하거나, DFS 혹은 BFS를 이용하여 해결할 수 있다. 따라서 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서 안전 영역의 크기를 계산하면 된다. 안전영역의 크기를 구하는 것 또한 DFS나 BFS를 이용하여 계산할 수 있다. 결과적으로 여기서는 가능한 모든 경우의 수를 계산하되, 안전 영역을 계산할 때 DFS나 BFS를 적절히 사용해야 된다는 것이다.  
문제 풀이 아이디어를 간략히 설명함현, 초기에 비어 있는 모든 공간 중에서 3개를 골라 벽을 설치하는 것이다. 매번 벽을 설치할 때마다, 각 바이러스가 사방으로 퍼지는 것을 BFS/DFS로 계산하여 안전 영역을 구해야 한다.  
python3 로 제출시 시간초과가 발생하고 pypy3로 하면 합격점을 받을 수 있다.
```python
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 주어진 그래프와 벽 세우고 난 후의 그래프
graph = []
temp = [[0] * m for _ in range(n)]
result = 0  # 안전 영역 개수
# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 그래프 입력
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))


# dfs형식을 통한 바이러스 전염
def virus(x, y):
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        # 범위 내, 빈칸
        # 조건을 0<= px <n 으로 합치는 것보다 각각 쓰는게 더 빠르게 걸러진다.
        if 0 <= px and px < n and 0 <= py and py < m and temp[px][py] == 0:
            temp[px][py] = 2
            virus(px, py)  # 재귀적 dfs


# 안전 영역 카운트
def score():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


# 모든 경우의 칸 세우기
def dfs(count):
    global result
    # 벽이 모두 설치되었을 때
    if count == 3:
        # 그래프 옮기기
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, score())
        return

    # 울타리 세우기
    for i in range(n):
        for j in range(m):
            # 빈칸이면
            if graph[i][j] == 0:
                graph[i][j] = 1  # 벽설치
                count += 1
                dfs(count)
                count -= 1
                graph[i][j] = 0  # 벽설치 해제


dfs(0)
print(result)
```
<br>

## 4. 경쟁적 전염
---
[문제 클릭](https://www.acmicpc.net/problem/18405){: target="_blank"}  

### 내가 작성한 코드
```python
import sys
from collections import deque
input = sys.stdin.readline

# 시험관 크기 n, 바이러스 종류 k
n, k = map(int, input().split())
graph = [[] for _ in range(n)]
cnt = 0  # 시간초

# U R D L 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시험관 정보
for i in range(n):
    graph[i] = list(map(int, input().rstrip().split()))

# s초후 x,y 위치의 값
s, x, y = map(int, input().split())

next =[]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            next.append((graph[i][j], i, j))  # (바이러스 종류, 좌표)
next.sort()  # 바이러스 번호순 정렬

# 입력된 시간 까지
while cnt < s:
    if not next : # 전염 시작 위치가 없는 경우
        break
    q = deque(next)  # 큐에 삽입
    next.clear()  # 이후 사용을 위해 비우기
    # 큐가 빌때까지 반복
    while q:
        num, i, j = q.popleft()
        # 4방향
        for z in range(4):
            pi = i + dx[z]
            pj = j + dy[z]
            # 범위 내에 있으면서 빈칸인 경우만
            # 따로 해주는게 더 빨리 끝남 
            if 0 <= pi and pi < n and 0 <= pj and pj < n and graph[pi][pj] == 0:
                graph[pi][pj] = num  # 바이러스 전염
                next.append((num, pi, pj))  # 다음 전염 시작의 기준 위치
    cnt +=1 # 큐가 다 비게 되면 1초 카운트


print(graph[x-1][y-1])
```
하나씩 옆에 있는 것부터 처리하는 과정을 통해 BFS를 생각해냈다. 바이러스 번호가 작은 것부터 전염을 시작해야 하기 때문에 큐를 바로 사용하기 전에 먼저 전염 번호 순으로 정렬시키고 큐에 대입하는 방법으로 설계했다.

### 모범 답안
낮은 번호부터 증식하므로, 초기에 큐에 원소를 삽입할 때는 낮은 바이러스의 번호부터 삽입해야 한다. 이후 BFS를 수행하며 방문하지 않은 위치를 차례대로 방문하도록 하면 된다.
```python
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)
 
target_s, target_x, target_y = map(int, input().split())
 
# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
```
<br>

## 5. 괄호 변환
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60058){: target="_blank"}  

### 모범  답안
구현을 위한 알고리즘 자체는 문제에 그대로 제시되어 있기 때문에, 재귀 함수를 이용하여 문제에 기재되어 있는 알고리즘을 안정적으로 구현할 수 있으면 해결할 수 있다.  
실수 없이 풀려면 소스코드를 최대한 단순화하는 것이 좋다. 따라서 특정 문자열에서 '균형잡힌 괄호 문자열'의 인덱스를 반환하는 함수와 특정한 '균형잡힌 괄호 문자열'이 '올바른 괄호 문자열'인지 판단하는 함수를 별도로 구현하고 재귀 함수에서 이 두 함수를 불러오도록 소스코드를 작성하자.  

```python
# 균형잡힌 문자열 분리
def balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        # 균형 잡힌 순간의 인덱스 반환
        # 입력 자체가 균형잡힌 괄호 문자열로 주어지므로 결국 return 발생
        if count == 0:
            return i


# 올바른 괄호 문자열 판단
def proper(u):
    count = 0
    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        else:
            # count==0인 시점에 )가 오면 올바른 문자열이 아님
            if count == 0:
                return False
            count -= 1
    return True


# 균형잡힌 괄호 문자열을 올바른 괄호 문자열로 반환하는 솔루션
def solution(p):
    answer = ''
    # 빈 문자열일 경우 빈 문자열 반환
    if p == '':
        return p
    idx = balance(p)
    u = p[:idx + 1]
    v = p[idx+1:]
    # 올바른 문자열이라면
    if proper(u):
        answer = u + solution(v)
    # 올바른 문자열이 아니라면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # 앞 뒤 문자 제거
        u = list(u[1:-1]) # 문자열로 표현되기때문에 list로 형변환
        # 뒤집기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u) # 리스트를 다시 문자열로
    return answer
```
<br>

## 6. 연산자 끼워 넣기
---
[문제 클릭](https://www.acmicpc.net/problem/14888){: target="_blank"}  

### 내가 작성한 코드
연산자 갯수가 n-1개 이므로 n-1!하면 모든 경우의수가 나온다. 3백만 정도의 연산 횟수가 되므로 완전 탐색을 해도 될 것 같아서 다음과 같이 설계했다. 
```python
import sys
from itertools import permutations

input = sys.stdin.readline
minus_INF = -int(1e9)
INF = int(1e9)

n = int(input())
a = list(map(int, input().rstrip().split()))
# 덧 뺄 곱 나눗
operators = list(map(int, input().rstrip().split()))
# 실제 문자로 연산자를 넣을 리스트
operator = []

# 연산자 넣기
for _ in range(operators[0]):
    operator.append('+')
for _ in range(operators[1]):
    operator.append('-')
for _ in range(operators[2]):
    operator.append('*')
for _ in range(operators[3]):
    operator.append('//')

# 순열
operators = list(permutations(operator, n - 1))

ans_max = minus_INF
ans_min = INF

# 비교 시작
for operator in operators:
    tmp = a[0]
    # 인덱스 n-1까지 정수 있고 연산자는 n-2까지 있다.
    for i in range(1, n):  # 연산자 인덱스는 -1 해주자
        if operator[i - 1] == '+':
            tmp += a[i]
        elif operator[i - 1] == '*':
            tmp *= a[i]
        elif operator[i - 1] == '-':
            tmp -= a[i]
        else:
            # 음의 경우
            if tmp < 0:
                tmp = -tmp
                tmp //= a[i]
                tmp = -tmp
            else:
                tmp //= a[i]
    ans_max = max(ans_max, tmp)
    ans_min = min(ans_min, tmp)

print(ans_max)
print(ans_min)
```

### 모범 답안
최대 11개의 수가 주어졌을 때, 각 수와 수 사이에 사칙연산 중 하나를 삽입하는 모든 경우에 대하여 만들어질 수 있는 결과의 최댓값 및 최솟값을 구하면 된다. 따라서 모든 경우의 수를 계산하기 위하여 완전탐색(DFS / BFS)를 이용하여 해결할 수 있다.  
이 문제에서는 각 사칙연산을 중복하여 사용할 수 있기 때문에, 중복 순열을 이용해 풀 수도 있다. 하지만 DFS를 이용하여 풀 수도 있다.  
__여기서 기억해야 할 점은 중복 순열을 DFS로 나타낼 수 있다는 것이다.__  
```python
import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().rstrip().split()))

plus, minus, mul, div = map(int, input().rstrip().split())

max_value = int(-1e9)
min_value = int(1e9)


def dfs(cnt, now):
    global plus, minus, mul, div, max_value, min_value
    # 주어진 연산자 다 사용했을때
    if cnt == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(cnt + 1, now + num[cnt])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(cnt + 1, now - num[cnt])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(cnt + 1, now * num[cnt])
            mul += 1
        if div > 0:
            div -= 1
            dfs(cnt + 1, int(now / num[cnt]))
            div += 1


dfs(1, num[0])
print(max_value)
print(min_value)
```
__python 음수 나눗셈__  
[![그림1](https://backtony.github.io/assets/img/post/python/intermediate/intermediate-3.PNG)](https://kj-said.tistory.com/entry/Python-%EB%82%98%EB%88%97%EC%85%88%EC%97%90-%EA%B4%80%ED%95%9C-%EA%B3%A0%EC%B0%B0-%EC%9D%8C%EC%88%98-%EB%82%98%EB%88%84%EA%B8%B0-divmod){: target="_blank"}  

그림과 같이 몫은 좌측값, 즉, 작은 값을 가리킨다. 따라서 연산 결과 아래와 같다.
```python
2018 / 5 # 403.6
2018 // 5 # 403

-2018 / 5 # -403.6
-2018 // 5 # -404 
```
따라서 위의 문제에서 주어진 나눗셈은 몫의 나눗셈이 아닌 실수 나눗셈을 한 뒤에 나머지를 버림으로 작성해야한다.  
<br>


#### DFS 중간정리
3번, 6번을 못 풀었었는데 모두 DFS문제였다. 
```python  
count += 1
dfs(count)
count -= 1
```
dfs는 위와 같은 형태로 대부분 인자를 탈출조건에 사용했으며, 간단히 정리하자면 아래와 같다.  
+ 만약 3개를 선택했다고 가정하면, 먼저 선택한 2개는 유지하면서 나중에 선택한 1개를 다른 것으로 바꾸기.. 이후에 남은 것들을 다 선택했다면 2번째 선택했던 것을 바꾸고 마지막 선택한 것을 다시 처음부터 바꾸기 이 과정을 반복하는데 사용되었다.
+ 특정한 개수를 모두 선택한 뒤 서로의 순서를 바꾸는, 즉, 중복순열을 나타낼 때도 사용할 수 있었다.

## 7. 감시 피하기
---
[문제 클릭](https://www.acmicpc.net/problem/18428){: target="_blank"}  

### 내가 작성한 코드
```python

```

## 8. 인구 이동
---
[문제 클릭](https://www.acmicpc.net/problem/16234){: target="_blank"}  

### 내가 작성한 코드
```python
import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
visited = [[0] * n for _ in range(n)]
# 그래프 입력
for i in range(n):
    graph[i] = list(map(int, input().rstrip().split()))

unions = deque()  # 큐
q = deque()  # 큐
# 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 이동 전과 이동 후 위치에서 값을 비교해야 하므로 bfs 사용
# 0,0 시작으로 대입
def bfs(graph, x, y):
    ans = 0  # 연합 여부
    q.append((graph[x][y], x, y))  # 첫 위치 삽입
    total = graph[x][y]  # 연합 총인구
    cnt = 1  # 연합국 개수
    # 연합 형성
    while q:
        value, bx, by = q.popleft()
        # 4방향 연산
        for i in range(4):
            px = bx + dx[i]
            py = by + dy[i]
            # 범위 내, 차이도 범위 내, 연합이 되지 않은 곳

            if 0 <= px < n and 0 <= py < n and l <= abs(graph[px][py] - graph[bx][by]) <= r and visited[px][py] != 1:
                unions.append((graph[px][py], px, py))  # 연합에 넣기
                q.append((graph[px][py], px, py))  # 큐에 넣기
                ans = 1  # 연합여부
                visited[px][py] = 1  # 연합이 된 지역 표시
                visited[bx][by] = 1  # 시작 지역 연합 표시
                cnt += 1  # 연합국 개수 더하기
                total += graph[px][py]  # 연합국 인구 더하기
    total //= cnt  # 연합국 개별 인구
    graph[x][y] = total
    # 연합의 인구이동
    while unions:
        union, x, y = unions.popleft()
        graph[x][y] = total

    return ans



cnt =0 # 이동 횟수
while True:
    ans = 0
    for i in range(n):
        for j in range(n):
            # 연합이 안되어 있는 경우
            if visited[i][j] != 1:
                ans = max(ans, bfs(graph, i, j)) # 연합이 된 경우 1이 반환됨
    if not ans: # 연합이 안 된 경우
        break
    cnt+=1
    visited = [[0] * n for _ in range(n)]  # 연합 초기화

print(cnt)
```

## 9. 블록 이동하기
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60063){: target="_blank"}  

### 내가 작성한 코드
```python

```

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
