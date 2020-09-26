---
layout: post
title:  구현 기출문제
subtitle:   구현 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 구현이란?](#1-구현이란?)
  - [2. 럭키 스트레이트](#2-럭키-스트레이트)
  - [3. 문자 재정렬](#3-문자-재정렬) 
  - [4. 문자열 압축](#4-문자열-압축)
  - [5. 자물쇠와 열쇠](#5-자물쇠와-열쇠)
  - [6. 뱀](#6-뱀)
  - [7. 기둥과 보 설치](#7-기둥과-보-설치)
  - [8. 치킨 배달](#8-치킨-배달)
  - [9. 외벽 점검](#9-외벽-점검)

## 1. 구현이란?
---
머릿속에 있는 알고리즘을 정확하고 빠르게 프로그램을 작성하는 과정을 구현이라고 한다. 동일한 알고리즘이라면 더 간결하고 효율적으로 작성한 코드가 잘 작성된 코드이므로, 무네 핵셜 아이디어를 떠올리는 것과 별개로 구현 능력은 코딩 테스트뿐만 아니라 실무에서도 중요하다.  
구현 능력이 요구되는 대표적인 알고리즘 문제 유형으로는 완전 탐색과 시뮬레이션이 있다. 완전 탐색은 모든 경우의 수를 빠짐없이 다 계산하는 해결 방법을 의미하고, 시뮬레이션은 문제에서 제시하는 논리나 동작 과정을 그대로 코드로 옮겨야 하는 유형을 의미한다.  
완전 탐색 문제는 모든 경우의 수를 다 계산해야 하기 때문에 반복문 혹은 재귀 함수를 적절히 사용하며 예외 케이스를 모두 확인해야 하는 경우가 많다. 그러므로 일반적으로 DFS/BFS 알고리즘을 이용해서 해결한다. 시뮬레이션 문제 또한 문제에서 요구하는 복잡한 구현 요구 사항을 그대로 코드로 옮겨야 한다는 점에서 해결 방법이 비슷하다.  
원소를 나열하는 모든 경우의 수를 고려하는 상황에서 보통 순열이나 조합 라이브러리를 사용해야 한다. 이때는 파이썬 라이브러리 itertoos로 쉽게 구현할 수 있다.  
<br>

## 2. 럭키 스트레이트
---
게임 내 럭키 스트레이트 라는 기술이 있다. 이는 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다. 특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 예를 들어 123,402가 현재 점수라면 왼쪽은 1 + 2 + 3 오른쪽은 4 + 0 + 2이므로 합이 6으로 동일하여 기술을 쓸 수 있게 된다.  
현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지 알려주는 프로그램을 작성하시오.  
__입력 조건__  
+ 첫째 줄에 점수 N이 정수로 주어진다.(10<=N<=99,999,999) 단, 점수 N의 자리수는 항상 짝수이다.

__출력 조건__  
+ 첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY", 없다면 "READY"를 출력

```
입력 예시
123402

출력 예시
LUCKY
```
<br>

### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

n = list(map(int,input().rstrip()))
mid =len(n)//2
left = n[:mid]
right = n[mid:]

if sum(left) == sum(right):
    print("LUCKY")
else :
    print("READY")
```
<br>

## 3. 문자 재정렬
---
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출련한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다. 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다.  
__입력 조건__  
+ 첫째 줄에 하나의 문자열 S가 주어진다. (1<=S의 길이 <=10,000)

__출력 조건__  
+ 첫째 줄에 문제에서 요구하는 정답을 출력한다.

```
입력 예시
AJKDLSI412K4JSJ9D

출력 예시
ADDIJJJKKLSS20
```
<br>

### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

s = list(input().rstrip())
alpha =[]
num =[]
for i in s:
    if '0' <= i <='9':
        num.append(int(i))
    else :
        alpha.append(i)
alpha.sort()
alpha.append(sum(num))
print(*alpha,sep="")
```
<br>

## 모범 답안
```python
data = input()
result =[]
value =0

# 문자를 하나씩 확인하며
for x in data:
    if x.isalpha():
        result.append(x)
    else :
        value +=int(x)

# 알파벳 오름차순 정렬
result.sort()
if value !=0:
    result.append(str(value))

print(''.join(result))
```
<br>

## 4. 문자열 압축
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60057){: target="_blank"}  
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고자 한다.  
간단한 예로 aabbaccc의 경우 2a2ba3c과 같이 표현할 수 있다. 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있다. 예를 들면 abcabcdede와 같은 문자열은 전혀 압축되지 않는다. 이러한 단점을 해결하기 위해 문자열을 1개 이상 단위로 잘라서 압축하여 더 짧은 문자열로 표현하는 방법을 찾아보려고 한다.  
예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있다. 다른 방법으로 8개 단위로 자르면 2ababcdcd로 표현할 수 있으며 이때가 가장 짧게 압축하여 표현할 수 있는 방법이다.  
다른 예로 abcabcdede와 같은 경우 2개로 잘라서 압축하면 abcabc2de가 되지만, 3개 단위로 자른다면 2abcdede가 되어 가장 짧은 압축 방법이 된다.  
압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return하도록 solution 함수를 완성하시오.  
__제한 사항__  
+ s의 길이는 1이상 1,000 이하
+ s는 알파벳 소문자로만 구성

```
입력 예시
"aabbaccc"

출력예시
7
```

### 내가 작성한 코드
```python
def solution(s):
    ans = []  # 자른 문자열의 문자개수를 append
    n = len(s)
    for i in range(1, n//2+1):  # 자를 문자열 개수, 절반 이상 넘어가면 자르는 의미가 없음
        j = 0
        cnt = 1
        zip_length=n
        while j<=n-1-i:
            if s[j:j+i]==s[j+i:j+2*i]:
                cnt+=1
                j+=i
                if j>n-1-i:
                    zip_length -= i * (cnt - 1) - len(str(cnt))

            else :
                if cnt>1:
                    zip_length-=i*(cnt-1)-len(str(cnt))
                j+=i
                cnt=1
        ans.append(zip_length)
    return min(ans)


```
실행 결과는 맞으나 1가지 경우에 대해 시간 초과가 발생했다.  
<br>

### 모범 답안
```python

```
<br>

## 5. 자물쇠와 열쇠
---
잠겨있는 자물쇠는 격자 한 칸의 크기가 1 * 1인 n * n 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 m * m크기인 정사각 격자 형태로 되어 있다. 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조이다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.  
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열 수 있으면 true 없으면 false를 return하는 solution 함수를 완성하시오.  
__제한 사항__  
+ key는 M * M (3<= M <=20) 크기의 2차원 배열
+ lock는 N * N (3<= N <=20) 크기의 2차원 배열
+ M은 항상 N이하
+ key와 lock의 원소는 0 또는 1이다. 이때 0은 홈, 1은 돌기를 나타낸다.


<br>

## 6. 뱀
---
Dummy라는 도스 게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀의 길이가 늘어난다. 뱀이 이리저리 기어 다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다.  
게임은 N * N 정사각 보드 위에서 진행되고 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에는 벽이 있다. 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1이다. 뱀은 처음에 오른쪽을 향한다.  
뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
+ 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
+ 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
+ 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸의 길이가 변하지 않는다.

사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하시오.  
__입력 조건__  
+ 첫째 줄에 보드의 크기 N이 주어진다. (2<=N<=100) 다음 줄에 사과의 개수 K가 주어진다. (0<=K<=100)
+ 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측(1행 1열)에는 사과가 없다.
+ 다음 줄에는 뱀의 방향 변환 횟수 L이 주어진다.(1<=L<=100)
+ 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져있으며, 게임 시작시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')으로 90도 방향을 회전시킨다는 뜻이다. X는 10,00이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

__출력 조건__  
+ 첫째 줄에 게임이 몇 초에 끝나는지 출력

```
입력 예시
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

출력 예시
9
```

### 내가 작성한 코드
```python
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 보드 크기
k = int(input())  # 사과의 개수

# 첫 위치가 1행 1열이므로 맞추기 위해 n+1
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1  # 사과가 있으면 1

l = int(input())  # 방향 변환 횟수
direction_l = []
for _ in range(l):
    x, c = input().split()  # x초후 c로 방향변환
    direction_l.append((x, c))

direction = ['U', 'R', 'D', 'L']
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

a = b = 1  # 첫 시작 위치
graph[1][1] = 2  # 시작 위치 자리 차지 표시
cnt = 0  # 경과시간
prevd = 'R'  # 시작 방향
j = 0  # direction_l 카운트
x, d = direction_l[j] # 첫 x초후 방향에 대한 정보
q = deque()  # 방문하는 순서를 기록
q.append((a, b))


while True:
    if cnt == int(x):  # 시간이 끝나면 새로운 시간,방향 정보를 받아야함
        if d == 'D':
            prevd = direction[(i+1)%4]
        else :
            prevd = direction[(i-1)%4]

        j += 1
        if j<len(direction_l):
            x, d = direction_l[j]

    for i in range(4):
        if direction[i] == prevd:
            break
    pa = a + da[i]
    pb = b + db[i]
    cnt += 1

    if pa <=0 or pa >=n+1 or pb<=0 or pb >=n+1 or graph[pa][pb]==2: # 먼저 머리 움직이고 확인 후 꼬리 거둠
        break

    if graph[pa][pb] == 0:  # 사과가 없다면
        tail_a, tail_b = q.popleft()
        graph[tail_a][tail_b] = 0  # 꼬리 방문 지우기

    graph[pa][pb] = 2  # 사과가 없으나 있으나 현재 방문위치 처리
    a = pa
    b = pb
    q.append((a, b))


print(cnt)
```

### 모범 답안
```python

```
<br>

## 7. 기둥과 보 설치
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60061){: target="_blank"}


### 내가 작성한 코드(틀림)
```python

def solution(n, build_frame):
    # n=5 이면 0부터 5까지 포함
    # x가 가로 y가 세로
    answer = [] # [x,y,a] 좌표와 기둥,보 형태
    # 중복입력은 없고 설치, 삭제만 조건에 따라 할 건지 무시할건지만 정하면 완성

    # 설치는 기둥의 경우 좌표를 기준으로 위/ 보는 오른쪽
    # 범위를 넘어가는 경우는 무시
    # 기둥 설치의 경우
    # 바닥에 있는가? / 보 위에 있는가? / 기둥 위에 있는가 3 경우에만 설치 가능
    # 보의 경우
    # 한쪽 끝이 기둥 위에 있는가? / 양쪽 끝 부분이 다른 보와 동시에 연결인가?

    # 즉 앞서 설치했던 내용들을 확인해야함
    for x, y,a,b in build_frame:
        if b==1: # 1 설치 / 0 삭제
            if a==0: #기둥
                if 0<=x<=n and 0<=y<=n-1 : # 범위 내에 존재
                    # 바닥에 있는가? / 받쳐줄 보가 있는가? / 아래 기둥이 있는가?
                    if y==0 or ((x-1,y,1) in answer) or ((x,y,1) in answer) or((x,y-1,0) in answer):
                        answer.append((x,y,a))
            else : # 보
                if 0<=x<=n-1 and 0<y<=n: # 범위 내 존재
                    # 아래 받치는 기둥이 있는가? / 양쪽에 보가 있는가
                    if ((x,y-1,0) in answer) or ((x+1,y-1,0) in answer) or(((x-1,y,1) in answer) and ((x+1,y,1) in answer)):
                        answer.append((x,y,a))
        else : # b=0일때 즉, 삭제
            if a ==0:   # 기둥
                # 위에 보가 있는데, 보가 양쪽에 있으면 삭제가능
                if (((x-1,y+1,1)in answer) and ((x,y+1,1)in answer)):
                    answer.remove((x,y,a))
                # 보가 한쪽만 있다면 삭제 불가능하므로 무시
            else :   # 보
                # 삭제 가능한 경우만 삭제 코드를 작성하면 된다., 안되는건 무시
                # 보는 언제 삭제가 가능하지?
                # 기둥위에 있는데 보 오른쪽이 없다면 삭제가능 / 만약 내가 가운데 보이고 양쪽에 보의 바닥에 기둥이 있으면 삭제가능
                if (((x,y-1,0) in answer) and ((x+1,y,1) not in answer)) or (((x-1,y,1) in answer) and ((x+1,y,1)in answer) and ((x-1,y-1,0) in answer) and ((x+1,y-1,0) in answer)):
                    answer.remove((x,y,a))
    # 기준대로 정렬
    answer.sort()
    return answer
```
틀림

### 모범 답안
```python

```
<br>

## 8. 치킨 배달
---
크기가 N * N인 도시가 있다. 도시는 1 * 1 크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈칸(0), 집(1), 치킨집(2) 중 하나이다. 도시의 칸은 (r,c)와 같은 형태로 나타내고, r행 c열을 의미한다. r과 c는 1부터 시작한다.  
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다. 임의의 두 칸(r1,c1), (r2,c2) 사이의 거리는 절댓값( (r1-r2) + 절댓값(c1-c2))로 구한다.  
가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M이라고 가정하고 도시에 있는 치킨집 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야한다. 어떻게 하면 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.  
__입력 조건__  
+ 첫째 줄에 N(2<=N<=50)과 M(1<=M<=13)이 주어진다.
+ 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
+ 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다는 작거나 같다.

__출력 조건__  
+ 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값을 출력하시오.

```
입력 예시
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

출력 예시
5

입력 예시
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

출력 예시
10

입력 예시
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

출력 예시
11
```

### 내가 작성한 코드(틀림)
```python
# 범위가 매우 작으므로 복잡도를 고려 안해도 될 수준
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i]=(list(map(int,input().rstrip().split())))
INF = int(1e9)
shortcut = [[INF] * n for _ in range(n)] # 최단거리
chick =[] # (카운트횟수,치킨집위치)
house =[] # 집 위치
chicken_house=[] # 치킨집 위치
total = 0 # 도시의 치킨 거리 최소값

# 집과 치킨집 위치 찾기
# x,y는 1부터 시작이어도 어쩌피 서로의 거리 차이므로 0부터 해도 무관
for x in range(n): # x는 행
    for y in range(n): # y는 열
            if graph[x][y]==1: #집
                house.append((x,y))
            if graph[x][y]==2: # 치킨집
                chicken_house.append((x,y))

# 각 집마다 최소 치킨거리의 치킨집에 카운트
for x1,y1 in house:
    for x2,y2 in chicken_house:
        if shortcut[x1][y1] > abs(x1-x2) + abs(y1-y2):
            shortcut[x1][y1] = abs(x1-x2) + abs(y1-y2)
            px = x2
            py = y2
    graph[px][py]+=1

for x1,y1 in chicken_house: # 카운트, 치킨집위치 넣고
    chick.append((graph[x1][y1],x1,y1))
chick.sort(reverse=True) # 내림차순
for i in range(m,len(chick)) : # m개 이후의 치킨집은 빈칸으로 초기화
    _, idx1, idx2=chick.pop()
    graph[idx1][idx2]=0

for x1,y1 in house:
    for cnt, x2,y2 in chick:
        if shortcut[x1][y1] > abs(x1-x2) + abs(y1-y2):
            shortcut[x1][y1] = abs(x1-x2) + abs(y1-y2)
    total += shortcut[x1][y1]

print(total)
```
예시 3 의 경우를 만족시키지 못했음

<br>

## 9. 외벽 점검
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60061){: target="_blank"}

### 내가 작성한 코드
```python

```



---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
