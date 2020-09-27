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

### 내가 작성한 코드(시간초과)
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
실행 결과는 맞으나 1가지 경우에 대해 시간 초과가 발생했다. 여기서 하나 고려해볼 점은 자른 모든 길이를 일일이 저장하고 min을 구하기 보다 자른 길이를 구할 때 마다 비교해서 저장하면 어떨까라는 생각이 들었다. 그래서 아래와 같이 수정했고 합격점을 받았다.  
__수정한 내 코드__  
```python
def solution(s):
    answer = len(s)  # 길이
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
        answer = min(answer,zip_length)
    return answer
```
<br>

### 모범 답안
입력으로 주어지는 문자열의 길이가 1,000 이하이기 때문에 가능한 모든 경우의 수를 탐색하는 완전 탐색을 수행할 수 있다. 예를 들어 길이가 N인 문자열이 입력되었다면 1부터 N/2까지의 모든 수를 단위로 하여 문자열을 압축하는 방법을 모두 확인하고, 가장 짧게 압축되는 길이를 출력하면 된다.
```python
def solution(s):
    answer = len(s)
    # 1개 단위 step부터 압축 단위를 늘려가며 확인
    for step in range(1,len(s)//2+1):
        compressed= ""
        prev = s[0:step] # 앞에서부터 step까지 추출
        count =1
        # step 만큼 증가시켜가며 이전 문자열과 비교
        # 인덱싱의 경우 out of index에 대해서는 무시되므로 참고하자
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count+=1
            else :
                compressed += str(count)+prev if count>=2 else prev
                prev = s[j:j+step]
                count=1
                
        # 남은 문자열 처리 (if문 앞의 경우는 딱 떨여졌을경우에 해당된다)
        compressed += str(count)+prev if count>=2 else prev
        answer = min(answer,len(compressed))
    return answer
```
<br>

## 5. 자물쇠와 열쇠
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60059){: target="_blank"} 
잠겨있는 자물쇠는 격자 한 칸의 크기가 1 * 1인 n * n 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 m * m크기인 정사각 격자 형태로 되어 있다. 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조이다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.  
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열 수 있으면 true 없으면 false를 return하는 solution 함수를 완성하시오.  
__제한 사항__  
+ key는 M * M (3<= M <=20) 크기의 2차원 배열
+ lock는 N * N (3<= N <=20) 크기의 2차원 배열
+ M은 항상 N이하
+ key와 lock의 원소는 0 또는 1이다. 이때 0은 홈, 1은 돌기를 나타낸다.

### 모범 답안
우리가 해야 할 일은 열쇠를 적당히 회전하고 이동시켜 자물쇠의 홈에 딱 맞게 끼워 넣는 것이다. 자물쇠와 열쇠의 크기는 20 * 20 보다 작다. 모든 원소에 접근할 때는 400만큼의 연산이 필요할 것이다. 코딩 테스트 채점 환경에서는 1초에 2,000만에서 1억정도의 연산을 처리할 수 있다. 즉, 범위가 매우 작으므로 복잡도를 고려하지 않아도 될 수준이다. 그렇기 때문에, 완전 탐색을 이용해서 열쇠를 이동이나 회전시켜서 자물쇠에 끼워보는 작업을 전부 시도해도는 접근 방법을 이용해 볼 수 있다. 완전 탐색을 수월하게 하기 위해서 자물쇠 리스트의 크기를 3배 이상으로 변경하면 계산이 수월해진다. 예를 들어 열쇠와 자물쇠가 3 * 3 크기라고 가정하자. 이때 가장 먼저 자물쇠를 크기가 3배인 새로운 리스트로 만들어 중앙 부분으로 옮긴다. 이제 열쇠 배열을 왼쪽 위부터 시작해서 한 칸씩 이동하는 방식으로 차례대로 자물쇠의 모든 홈을 채울 수 있는지 확인하면 된다. 자물쇠 리스트에 열쇠 리스트의 값을 더한 뒤에, 자물쇠 부분의 모든 결과값이 1이 되면 홈 모두를 채운 것이라고 볼 수 있다. 여기서 2차원 리스트의 회전 결과값을 반환하는 함수를 사용해야하는데 가끔씩 사용되므로 알아두도록 하자.
```python
# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    x = len(a)  # 행의 길이 계산
    y = len(a[0])  # 열의 길이 계산

    # 회전하는 결과 리스트는 행과 열의 길이가 바뀐다.
    result = [[0] * x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            # result[y-j-1][i] = a[i][j]# 왼쪽으로 회전
            result[j][x - i - 1] = a[i][j]  # 오른쪽으로 회전
    return result


# 자물쇠 부분이 모두 1인지 확인
def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True
    # if total == lock_len*lock_len:
    #     return True
    # else :
    #     return False


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 알고리즘 설계를 자물쇠 리스트와 키 리스트의 값의 합이 모두 1이되는 경우 완성
    # 비교를 편하게 하기 위해서 원래 자물쇠 크기의 3배로 새로운 리스트 생성
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    # lock를 new_lock의 중앙으로 옮기기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j]=lock[i][j]

    # 4가지 방향에 대한 확인
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        # new_lock의 비교 시작 좌표
        for x in range(n*2): # 1부터 해도 되나 시간의 차이는 거의 없으므로 편의상
            for y in range(n*2):
                # key의 비교 좌표, 자물쇠에 열쇠 넣기
                for a in range(m):
                    for b in range(m):
                        new_lock[x+a][y+b] += key[a][b]
                # 채워졌는지 확인
                if check(new_lock):
                    return True
                # 다시 key 빼내기
                for a in range(m):
                    for b in range(m):
                        new_lock[x+a][y+b] -= key[a][b]
    return False
```

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
2차원 배열상의 특정 위치에서 동,남,서,북의 위치로 이동하는 기능을 구현해야 한다. 이 문제의 경우, 뱀이 처음에 오른쪽(동쪽)을 바라보고 있다는 점을 고려하자. 더불어 뱀의 머리가 뱀의 몸에 닿는 경우 종료해야 하므로, 매 시점마다 뱀이 존재하는 위치를 항상 2차원 리스트에 기록해야 한다.  
이러한 시뮬레이션 문제 유형을 가장 쉽게 풀기 위해서는 그림으로 그려보는 것이 좋다. 
```python
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
```
<br>

## 7. 기둥과 보 설치
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60061){: target="_blank"}

### 모범 답안
전체 명령의 개수는 총 1,000개 이하이다. 따라서 O(N^2)으로 해결하는 것이 이상적이나 시간제한이 5초로 넉넉하기 때문에 O(N^3)의 알고리즘을 이용해도 정답판정을 받을 수 있다. 따라서 후자로 해결하는 가장 간단한 방법은, 설치 및 삭제 연산을 요구할 때마다 일일이 전체 구조물을 확인하며 규칙을 확인하는 것이다. 이렇게 복잡한 문제의 경우 해결에 따른 함수를 따로 만들어 사용하는 것이 좋다.
```python
# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 기둥인 경우
            # 바닥 위, 보의 한쪽 끝 부분 위, 다른 기둥 위라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            # 아니면
            return False
        else:  # 설치된 것이 보인 경우
            # 한쪽 끝부분이 기둥 위, 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y,
                                                                                                      1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, stuff, operate in build_frame:
        if operate == 0:  # 삭제
            answer.remove([x, y, stuff])  # 일단 삭제
            if not possible(answer):  # 불가능한 형태
                answer.append([x, y, stuff]) # 다시 설치
        else:  # 설치
            answer.append([x, y, stuff])  # 일단 설치
            if not possible(answer):  # 불가능한 형태
                answer.remove([x, y, stuff])  # 삭제
    return sorted(answer)
    # answer.sort()
    # return answer

# 코딩 중간에 생겼던 의문점
# 삭제의 경우 answer에서 삭제 후 모양 성립 조건에 위배되어 다시 추가했다
# 근데 맨 뒤에 추가해도 되나?
# 상관 없다 -> answer의 순서에 관계 없이 in으로 안에 있는지 없는지로 판단하기 때문
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
