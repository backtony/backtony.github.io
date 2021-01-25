---
layout: post
title: 그래프 이론 기출문제
subtitle:   그래프 이론 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 간단 정리](#1-간단-정리)
  - [2. 여행 계획](#2-여행-계획)
  - [3. 탑승구](#3-탑승구) 
  - [4. 어두운 길](#4-어두운-길)
  - [5. 행성 터널](#5-행성-터널)
  - [6. 최종 순위](#6-최종-순위)


## 1. 간단 정리
---
### 서로소 집합
서로소 집합은 공통 원소가 없는 두 집합이다. 이때 집합 간의 관계를 파악하기 위해서 서로소 집합 알고리즘을 사용할 수 있다. 서로소 집합 알고리즘은 union - find 연산으로 구성되며, 모든 노드는 자신이 속한 집합을 찾을 때 루트 노드를 재귀적으로 찾는다. 서로소 집합 알고리즘은 최소 신장 트리를 찾는 크루스칼 알고리즘에서 사용되기도 한다.
<br>

### 신장 트리
신장 트리는 하나의 그래프가 있을 때 모든 노드를 포함하는 부분 그래프를 의미한다. 일반적으로 코딩테스트에서는 최소 신장 트리 문제가 출제된다.

### 크루스칼 알고리즘
크루스칼 알고리즘은 가능한 최소 비용의 신장 트리를 찾아주는 알고리즘이다. 시간 복잡도는 O(ElogE)로 간선을 정렬한 뒤에 간선의 비용이 작은 순서대로 차례대로 최소 신장 트리를 만들어 가는 그리디 알고리즘의 일종이다.

### 위상 정렬 알고리즘
위상 정렬 알고리즘은 방향 그래프의 모든 노드들을 방향성에 거스르지 않도록 순서대로 나열한 정렬 기법이다. 예를 들어 선수과목을 고려한 학습 순서 설정 문제 등에서 사용될 수 있다. 큐 자료구조를 이용한 위상 정렬의 시간 복잡도는 O(V+E)이다.  
<br>

서로소 집합 알고리즘과 최소 신장 트리 알고리즘은 종종 코딩테스트에서 출제되는 알고리즘 유형이며, 위상 정렬 알고리즘은 난이도가 높은 후반부 문제에서 가끔 출제되므로 기억해두자.  

<br>

## 2. 여행 계획
---
주인공이 사는 나라에는 N개의 여행지가 있으며, 각 여행지는 1 ~ N번까지의 번호로 구분된다. 또한 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있다. 이때, 여행지가 도로로 연결되어 있다면 양방향으로 이동이 가능하다는 의미이다. 주인공은 하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지의 여부를 판단하고자 한다. 여행지의 개수와 여행지 간의 연결 정보가 주어졌을 때, 주인공의 여행 계획이 가능한지 여부를 판별하는 프로그램을 작성하시오.  
__입력 조건__  
+ 첫째 줄에 여행지의 수 N과 여행 계획에 속한 도시의 수 M이 주어진다. (1<= N,M <=500)
+ 다음 N개의 줄에 걸쳐 N * N 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부가 주어진다. 그 값이 1이라면 서로 연결되었다는 의미이며, 0이라면 서로 연결되지 않았다는 의미이다.
+ 마지막 줄에 주인공의 여행 계획에 포함된 여행지 번호들이 주어지며 공백으로 구분한다.

__출력 조건__  
+ 첫째 줄에 주인공의 여행 계획이 가능하다면 yes, 불가능시 no출력

```
입력 예시
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

출력예시
yes
```


### 내가 작성한 코드
```python
# 인자로 받은 배열은 C언어의 주소로 받은 것과 같음 -> 서로 영향을 준다
# 파이썬의 경우는 인자로 받지 않아도 밖에 있는 배열 사용 가능

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

graph = []

# 그래프 입력
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 계획 여행지 정보
plan = list(map(int, input().split()))

# 부모노드 저장
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i  # 처음에는 자기자신이 부모

# 그래프 정보 입력과 동시에 union작업
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i + 1, j + 1)

ans = find_parent(plan[0])
key = 0
for i in plan[1:]:
    if ans != find_parent(i):
        key = 1
        break
if key:
    print("no")
else:
    print("yes")

```
서로소 집합 알고리즘을 이용하여, 그래프에서 노드간의 연결성을 파악해 해결할 수 있다. 즉, 여행 계획에 해당하는 모든 노드가 같은 집합에 속하면 가능한 여행 경로 라는 것이다.

### 모범 답안
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우 합집합(Union) 연산 수행
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plan = list(map(int, input().split()))

result = True
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지) 확인
if result:
    print("YES")
else:
    print("NO")
```
union한 이후에는 그래프의 정보를 저장해야할 필요가 없기 때문에 한 줄씩 그래프 정보를 받고 처리한 후에 다시 다음 그래프 정보로 덮어씌운다는 점이 내 코드랑 다른 점이다. 이렇게 하면 메모리를 조금이나마 아낄 수 있다.

<br>

## 3. 탑승구
---
공항에는 G개의 탑승구가 있으며, 각각 탑승구는 1번부터 G번까지의 번호로 구분된다. 공항에는 P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 g번째 탑승구 중 하나에 영구적으로 도킹해야한다. 이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다.  
또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떤 탑승구에 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서 공항의 운행을 중지시킨다. 공항의 관리자는 최대항 많은 비행기를 공항에 도킹하고자 한다. 비행기를 최대 몇 대 도킹할 수 있는지 출력하는 프로그램을 작성하시오.  
__입력 조건__  
+ 첫째 줄에는 탑승구의 수 G(1<=G<=100,000)
+ 둘째 줄에는 비행기의 수 P(1<=P<=100,000)
+ 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 g(1<=g<=G)가 주어진다. 이는 i 번째 비행기가 1번부터 g번째 탑승구 중 하나에 도킹할 수 있다는 의미이다.

__출력 조건__  
+ 첫째 줄에 도킹할 수 있는 비행기의 최대 개수를 출력

```
입력 예시
4
3
4
1
1

출력 예시
2

입력 예시
4
6
2
2
3
3
4
4

출력 예시
3
```

### 내가 작성한 코드
첫 공부, 1차 리뷰에서 풀지 못했다. 주어진 도커 범위에서 제일 마지막 번호에 연결해야한다는 점은 눈치챘다. 그럼 다음에 들어올 것이 번호가 같으면 그 번호 앞에 연결시켜야한다. 그럼 처음 도커에 연결했을 때 연결하고 이후에는 바로 앞쪽에 연결하도록 조치를 취해줘야 한다. 여기서 사용해야할 것이 서로소 집합 알고리즘의 union이다. union을 통해 다음 연결 도커를 지정해주고, 만약 부모를 찾았을 때 0이 나오게 된다면 더이상 도커에 연결 할 수 없는 것이다.
```python
g = int(input())
p = int(input())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 부모는 자기 자신
parent = [0] * (g + 1)
for i in range(g + 1):
    parent[i] = i

# 도커 정보
docks=[]
for i in range(p):
    docks.append(int(input()))


cnt = 0
for dock in docks:
    pos_dock = find_parent(parent, dock)
    if pos_dock==0:
        break
    union(parent, pos_dock, pos_dock - 1)
    cnt += 1

print(cnt)
```

### 모범 답안
이 문제는 서로소 집합 알고리즘을 이용하면 쉽게 해결할 수 있다. 각 탑승구를 서로 다른 집합으로 나타낸다고 해보자. 전체 탑승구가 4개라고 가정하면 각각 parent는 자신의 탑승구 번호를 가리킨다. 이때 비행기가 순서대로 들어오면 차례대로 도킹을 수행해야 하는데, 가능한 큰 번호의 탑승구로 토킹을 우선 시행해야한다. 이때 도킹하는 과정을 탑승구 간 union 연산으로 이해할 수 있다. 새롭게 도킹이 되면, 해당 집합은 바로 왼쪽에 있는 집합과 합친다. 단, 집합의 루트가 0이되면 더이상 도킹이 불가능 한것으로 판단한다. 
```python
import sys

input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


# 탑승구 수, 비행기 수
g = int(input())
p = int(input())
parent = [0] * (g + 1)
cnt = 0
limit = []
# 집합 설정
for i in range(g + 1):
    parent[i] = i

for _ in range(p):
    limit.append(int(input()))

for i in limit:
    # 더이상 불가
    if find_parent(i) == 0:
        break
    # 자기 자신이면
    if find_parent(i) == i:
        union(i, i - 1)

    else:
        a = find_parent(i)
        union(a, a - 1)
    cnt += 1

print(cnt)
```
<br>

## 4. 어두운 길
---
한 마을은 N개의 집과 M개의 도로로 구성되어 있다. 각 집은 0번부터 N-1번까지의 번호로 구분된다. 모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용을 해당 도로의 길이와 동일하다. 예를 들어 2,3번 집 사이를 연결하는 길이가 7인 도로가 있다면 하루 종일 켜두는 비용은 7이다.  
정부에서 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 한다. 결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자 한다. 마을의 집과 도로 정보가 주어졌을 때, 이룹 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하시오.  
__입력 조건__  
+ 첫째 줄에 집의 수 N(1<=N<=200,000)과 도로의 수 M(N-1<=M<=200,000)이 주어진다.
+ 다음 M개의 줄에 걸쳐서 각 도로에 대한 정보 X,Y,Z가 주어지며, 공백으로 구분한다. (0<=X,Y < N ) 이는 X번 집과 Y번 집 사이에 양방향 도로가 있으며, 그 길이가 Z라는 의미이다. 단 x,y가 동일한 경우는 없으며 마을을 구성하는 모든 도로의 길이 합은 2^31보다 작다.

__출력 조건__  
+ 첫째 줄에 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력

```
입력 예시
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15 
3 5 6
4 5 8
4 6 9
5 6 11

출력 예시
51
```
### 내가 작성한 코드
전형적인 최소 신장 트리 문제이므로 크루스칼 알고리즘을 사용해 해결했다.  
비용을 기준으로 좌표와 함께 정렬하고 union작업을 했다. 부모가 같다면 이미 연결되어있으므로 union작업을 하지 않고 절약 비용에 추가했다. 
```python
import sys
input = sys.stdin.readline  # 입력 횟수가 매우 많으므로


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


dp = []
ans = 0  # 절약 비용
n, m = map(int, input().split())

parent = [0] * n  # 포함 집합의 부모
for i in range(n):  # 처음에는 자기 자신으로 초기화
    parent[i] = i

# 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    dp.append((z, x, y))
# 정렬
dp.sort()

for i in dp:
    cost, x, y = i
    # 부모가 같다면 이미 연결되어 있음
    if find_parent(parent, x) == find_parent(parent, y):
        ans += cost
    # 부모가 다르면 연결이 필요함
    else:
        union(parent, x, y)

print(ans)
```

<br>

## 5. 행성 터널
---
[문제 클릭](https://www.acmicpc.net/problem/2887){: target="_blank"}  

### 내가 작성한 코드
첫 공부, 1차 리뷰에서도 풀지 못했다.  
메모리 초과 판정을 받았다. 생각해보면 모든 행성에 대해 모든 행성으로까지의 비용을 계산해서 크루스칼 알고리즘을 실행했는데, 행성의 최대 개수가 10만개다. 크루스칼 알고리즘은 정렬에서의 복잡도 비용이 제일 크다. 그런데 모든 행성으로의 계산을 하게 되면 간선이 n-1, n-2.. 1개로 약 n^2개가 나오게 되면서 10만을 훨씬 넘어간다. 따라서 다른 방법을 생각해내야 했는데 하지 못했다.  
답안의 코드를 참고해보면, __최소 거리를 구하는데 굳이 모든 행성까지의 거리를 구할 필요가 없었다. 최소거리 이므로 현재 행성에서 3방향(x,y,z) 방향의 최소거리만 구해서 돌리면 되는 것이다.__  
```python
import sys

input = sys.stdin.readline  # 입력 횟수가 매우 많으므로


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
# 부모 설정
parent = [0] * n
for i in range(n):
    parent[i] = i

# 행성 정보 입력
planet = []
for _ in range(n):
    planet.append(list(map(int, input().split())))

dis = []
for i in range(n):
    for j in range(i+1,n):
        cost = min(abs(planet[i][0] - planet[j][0]),
                   abs(planet[i][1] - planet[j][1]),
                   abs(planet[i][2] - planet[j][2]))
        dis.append((cost, i, j))

dis.sort()  # 정렬

ans = 0  # 거리 비용
for i in dis:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        union(parent, i[1], i[2])
        ans += i[0]

print(ans)
```

### 모범 답안
이 문제는 n - 1개의 터널을 설치해서 모든 행성이 연결되도록 요구하므로, 최소 신장 트리를 만드는 문제로 이해할 수 있다. 여기서 당연히 크루스칼 알고리즘을 생각해 낼 것이다. 하지만 여기서 주의해야 한다. 크루스칼 알고리즘은 정렬하는 부분이 가장 많은 복잡도를 소요하므로 (ElogE)이다. 그런데 이 문제에서는 임의의 두 노드 사이에 터널을 연결할 수 있다고 가정하고 있다. 따라서 간선의 개수가 n-1, n-2, n-3 ... 1 개가 생성되어 간선의 총 개수가 N(N-1)/2이다. N의 범위가 100,000까지이므로 간선의 개수가 매우 커져 시간 안에 해결할 수 없다.  
하지만 터널 비용의 정의를 이용하면 간선의 개수를 줄일 수 있다. 입력 받은 x,y,z축을 기준으로 각각 정렬을 수행한다. x축만 고려해서 예시를 들어보면, 주어진 예시를 정렬시 -1,10,11,14,19로 정렬 될 것이다. 그렇다면 차례대로 간선을 만들어 주면 n-1개가 생기게 된다.  
여기서 살짝 이해가 안될 수 있다. 생각해보자. 지금 문제 조건은 최소 거리로 터널을 만드는 것이다. 그렇다면 현재 행성에서 최소 거리에 있는 거리만 고려하면 된다는 것이다. -1과 10을 간선으로 연결하지 않고 -1과 11을 연결하면 그 비용이 더 커진다. 따라서 인접한 것 끼리만 간선을 만들어 주는 것이다.  
결과적으로 계속 진행하면 축마다 n-1개의 간선이 생기므로 총 3 * (n-1)개의 간선이 생기고 이를 크루스칼 알고리즘을 수행하면 시간 안에 해결할 수 있다.  

```python
import sys

input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
x = []
y = []
z = []
parent = [0] * (n + 1)

# 처음 parent 초기화
for i in range(1, n + 1):
    parent[i] = i

# 좌표별로 삽입
for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

# 간선 정보 담을 곳
answer = []

# 간선 담기
# 간선의 개수는 n-1개이므로 
for i in range(n - 1):
    answer.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    answer.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    answer.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

answer.sort()
total = 0
for cost, x, y in answer:
    if find_parent(x) != find_parent(y):
        union(x, y)
        total += cost
print(total)
```
<br>

## 6. 최종 순위
---
[문제 클릭](https://www.acmicpc.net/problem/3665){: target="_blank"}  

### 내가 작성한 코드
첫 공부, 1차리뷰에서 풀지 못했다.
문제에서 약간 혼동되게 작성되있는 부분이 있다. 상대적 순위 변동 시, (6,13)으로 주어져 있는데 이건 6이 순위가 더 높아졌다는 뜻이 아니라, 팀6과 팀 13의 상대적 순위에 변동이 있다는 의미이고 작은 수부터 앞에 작성한다는 뜻이다.  
두 관계의 변화에 대해 좀 더 생각해보자. 문제에서 주어진 바로는 상대적 관계의 변화가 있는 경우가 있을 경우 주어진다고 했다. 그럼 6,13 팀의 상대적 변화가 있다면 일단 둘의 관계만 고려를 한다. 만약 두 팀 사이에 다른 팀을이 있어도 지금 고려해서는 안된다. 두 팀 사이의 팀에 대해 관계 변화가 있다면 6,13이후에 주어질 것이기 때문에 먼저 사이의 관계를 고려해서는 안된다는 뜻이다. 
전에 풀었던 [위상정렬 문제 커리큘럼](https://backtony.github.io/algorithm/2020/09/09/algorithm-basics-coding-11/)에서는 인접리스트 방법을 사용했다. 주어진 문제는 커리큘럼 관련 문제인데 커리큘럼은 고정되있고, 순서의 변화가 없었다. 순차적으로 진행 시 해당 리스트에 연결된 모든 값에 접근해 차수를 수정해야했기 때문에 굳이 특정 위치만 빠르게 찾는 인접 행렬 방식을 사용하지 않아도 되었던 것이다. 하지만 이 경우에는 순서가 변한다. 즉, 인접리스트를 사용할 경우 리스트 맨 앞에서부터 변화한 값을 찾아서 수정해줘야 하기에 시간이 너무 많이 소요된다는 것이다. 따라서, 해당 위치만 빠르게 찾아서 수정하는 인접 행렬을 사용해야 한다.

### 모범 답안
문제에서는 작년 순위와 상대적으로 순위가 바뀐 팀들의 목록이 주어졌을 때, 올해 순위를 만들 것을 요구하고 있다. 즉, __정해진 우선순위에 맞게 전체 팀들의 순서를 나열한다(선수과목)__ 는 점에서 위상 정렬 알고리즘을 떠올릴 수 있어야 한다.  
다시 말해 이 문제는 팀 간의 순위 정보를 그래프 정보로 표현한 뒤에, 위상 정렬 알고리즘을 이용해 해결할 수 있다. 주어진 예시를 가지고 생각해보자. 작년 순위 정보를 기준으로하여 __자기보다 낮은 등수를 가진 팀을 가리키토록 방향 그래프__ 를 만들 수 있다. 즉, 1등팀인 팀5는 1,2,3,4로 방향을 가리킬 수 있는 것이다. 이대로 위상 정렬을 수행하게 되면, 수행 결과는 5-4-3-2-1로 나온다.  
상대적인 순위가 바뀌게 되는 경우에는 해당 간선의 방향을 반대로 변경하면 된다. 여기서 위상 정렬을 수행하게 되면 사이클이 발생하는 경우와 위상 정렬의 결과가 1개가 아니라 여러 가지인 경우로 2가지 특이 케이스가 발생한다. 이 2가지 경우에 해당하지 않는다면 위상 정렬을 수행한 결과는 오직 하나의 경우만 존재한다. 즉, 가능한 순위가 하나라는 뜻이다.  
따라서 변경된 상대적 순위를 적용한 이후에, 위상 정렬 알고리즘을 실행하면서 사이클이 발생하는지, 혹은 결과가 여러 가지인지 확인하면 된다. 일반적인 위상 정렬의 경우, 정확히 N개의 노드가 큐에서 출력이 된다. 만약 N번 나오기 전에 큐가 비게 된다면, 사이클이 발생한 것으로 이해할 수 있다. 또한 특정 지점에 2개 이상의 노드가 큐에 한꺼번에 들어갈 때는, 가능한 정렬 결과가 여러 가지라는 의미가 된다. 그러므로 위상 정렬 수행 과정에서 큐에서 노드를 뽀을 때 큐의 원소가 항상 1개로 유지되는 경우에만 고유한 순위가 존재하는 것으로 이해할 수 있다. 따라서, 위상 정렬 코드에 매 시점마다 큐의 원소가 0개이거나 2개 이상인지 체크하는 부분을 넣어주면 된다.  

```python
import sys
from collections import deque

input = sys.stdin.readline

def topology_sort(count_graph, link_graph, n):
    answer=[]
    q = deque()
    # 진입차수가 0인 것 큐에 삽입
    for i in range(1,n+1):
        if count_graph[i]==0:
            q.append(i)

    # 노드의 개수 만큼만 반복
    for i in range(n):
        # 사이클 발생이 발생하면 일관성이 없음
        if len(q) == 0:
            print("IMPOSSIBLE")
            return
        # 2개 이상 들어오면 확실한 순위를 찾을 수 없음
        if len(q) > 1:
            print("?")
            return
        idx = q.popleft()
        answer.append(idx)
        # 연결 관계, 진입차수 수정
        for i in range(1,n+1):
            if link_graph[idx][i]== True:                
                count_graph[i]-=1
                # 사실 여기서 false로 안해줘도 된다.
                # 더이상 사용하지 않기 때문
                link_graph[idx][i] = False
                if count_graph[i]==0:
                    q.append(i)

    return answer

case = int(input())
# 테스트 케이스 만큼 반복
for _ in range(case):
    n = int(input())
    # 작년 순위
    rank = list(map(int, input().rstrip().split()))
    # 진입차수 그래프와 연결 상태 그래프
    count_graph = [0] * (n + 1)
    link_graph = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            count_graph[rank[j]] += 1
            link_graph[rank[i]][rank[j]] = True

    m = int(input())
    # 순위 뒤집기
    for i in range(m):
        a,b = map(int,input().split())
        if link_graph[a][b]: # 이게 어떤 경우지?
            count_graph[a]+=1
            count_graph[b]-=1
            link_graph[a][b]=False
            link_graph[b][a] = True
        else :
            count_graph[a] -= 1
            count_graph[b] += 1
            link_graph[a][b] = True
            link_graph[b][a] = False

    answer = topology_sort(count_graph,link_graph,n)
    if answer:
        for i in answer:
            print(i,end =" ")
        print()
```




 
<br>

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
