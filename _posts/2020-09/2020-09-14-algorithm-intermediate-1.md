---
layout: post
title:  그리디 기출문제
subtitle:   그리디 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 그리디란?](#1-그리디란?)
  - [2. 모험가 길드](#2-모험가-길드)
  - [3. 곱하기 혹은 더하기](#3-곱하기-혹은-더하기) 
  - [4. 문자열 뒤집기](#4-문자열-뒤집기)
  - [5. 만들 수 없는 금액](#5-만들-수-없는-금액)
  - [6. 볼링공 고르기](#6-볼링공-고르기)
  - [7. 무지의 먹방 라이브](#7-무지의-먹방-라이브)


## 1. 그리디란?
---
현재 상황에서 가장 좋아보이는 것만 선택하는 알고리즘이다. 코딩 테스트에서는 대부분 최적의 해를 찾는 문제가 출제되기 때문에 그리디 알고리즘의 정당성을 고민하면서 문제 해결 방안을 생각해야 한다. 대표적인 예시로는 거스름돈 문제와 1이 될 때까지 1빼기 혹은 K나누기 연산의 최소값 문제가 있다. 그리디 유형의 문제 특징은 다양한 알고리즘에서 사용되고 있다는 점인데 다익스트라 최단 경로 알고리즘과 크루스칼 알고리즘은 모두 그리디 알고리즘에 속한다.  
<br>

## 2. 모험가 길드
---
한 마을에 모험가가 N명이 있고 모험가를 대상으로 공포도를 측정했다. 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다는 규정이 있다. 길드장은 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금해한다. 길드장을 위해 N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최대값을 구하는 프로그램을 작성하시오. 단, 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없다.  
__입력 조건__  
+ 첫째 줄에 모험가의 수가 주어진다. (1<=N<=100,000)
+ 둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며 공백으로 구분한다.

__출력 조건__  
+ 여행을 떠날 수 있는 그룹의 최대 수를 출력한다.

```
입력예시
5
2 3 1 2 2

출력 예시
2
```

### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

n = int(input())
scared = list(map(int,input().split()))
scared.sort()

cut =0 # 그룹포함된 마지막 사람
count=0 # 그룹 카운트
for i in range(len(scared)):
    if scared[i]==i+1-cut:
        cut=i+1
        count+=1
print(count)
```
공포도를 정렬하고 하나씩 확인하면서 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 같거나 크다면 이를 그룹으로 설정한다는 아이디어로 설계했다.  
<br>

### 모범 답안
```python
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
```

<br>

## 3. 곱하기 혹은 더하기
---
각 자리가 숫자 0 ~ 9로만 이루어진 문자열 S가 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 * 혹은 + 연산자를 넣어 결과적으로 가질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오. 단, 일반적인 우선순위와 다르게 모든 연산은 왼쪽부터 순서대로 이루어진다고 한다. 또한 만들어 질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어진다.  
__입력 조건__  
+ 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다. (1<=S의 길이<= 20)

__출력 조건__  
+ 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력한다.

```
입력 예시
02984

출력 예시
576
```

### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

s = list(map(int,input().rstrip()))
total =0
for i in s:
    if i >1 and total !=0:
        total *=i
    else :
        total+=i

print(total)
```
<br>

### 모범 답안
```python
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
```
<br>

## 4. 문자열 뒤집기
---
주인공은 0과 1로만 이루어진 문자열 S를 가지고 있다. 주인공은 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 주인공이 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 예를 들어 0001100일 때는 다음과 같다.  
1. 전체를 뒤집으면 1110011
2. 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 두 번 만에 모두 같은 숫자로 만들 수 있다.

하지만 처음부터 4번째 문자부터 5번째 문자까지 뒤집으면 모두 0으로 한 번 만에 모두 같은 숫자로 만들 수 있다. 주인공이 해야하는 행동의 최소 횟수를 구하여라.  
__입력 조건__  
+ 첫째 줄에 0과 1로만 이루어진 문자열 S가 주어진다. S의 길이는 100만보다는 작다.

__출력 조건__  
+ 첫째 줄에 주인공이 해야 하는 행동의 최소 횟수 출력

```
입력 예시
0001100

출력 예시
1
```

### 내가 작성한 코드
```python
import sys
input = sys.stdin.readline

s = list(map(int,input().rstrip()))

i=0
count0=0
count1=0
while i<len(s):
    while i<len(s) and s[i]==0:
        i+=1
    count0+=1
    if i==len(s):
        break
    while i < len(s) and s[i]==1:
        i+=1
    count1+=1
if count0<count1:
    print(count0)
else :
    print(count1)
```
<br>

### 모범 답안
```python
data = input()
count0 = 0  # 전부 0으로 만들기 위해 뒤집기 횟수
count1 = 0  # 전부 1로 만들기 위해 뒤집기 횟수

# 두 번째 원소부터 마지막 원소 까지
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

# 첫 번째 원소 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

print(min(count1, count0))
```
i번째 원소와 i+1번째 원소가 다른 경우에서 i+1번째 원소가 1이면 1을 0으로 뒤집기 위해서 count0+=1, 반대의 경우 count1+=1을 한다. 하지만 이 경우에서는 뒤에 대상을 뒤집는 경우이므로 제일 첫 원소에 대해서는 계산을 해주지 못한다. 따라서 첫 번째 원소 처리는 따로 해준다.  
<br>

## 5. 만들 수 없는 금액
---
동네 편의점의 주인은 N개의 동전을 가지고 있다. 이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오.  
예를 들어 N=5이고, 각 동전이 3,2,1,1,9원 짜리 동전이라고 가정하자. 이때 주인이 만들 수 없는 최소 양의 정수는 8이다.  
__입력 조건__  
+ 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어진다. (1<=N<=1,000)
+ 둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며 공백으로 구분한다. 화폐의 단위는 1,000,000 이하의 자연수이다.

__출력 조건__  
+ 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최소값을 출력

```
입력 예시
5
3 2 1 1 9

출력 예시
8
```

### 모범 답안
```python
import sys
input = sys.stdin.readline

n = int(input())
pays = list(map(int,input().split()))
pays.sort()
target = 1

for x in pays:
    if x>target:
        break
    target+=x

print(target)
```
1부터 terget -1 까지의 모든 수를 만들 수 있다고 가정해보자. 화폐 단위가 작은 순서대로 동전을 확인하며, 현재 확인하는 동전을 이용해 금액 target 또한 만들 수 있는지 확인하면 된다. 1부터 만들 수 있는지 없는지 확인해야 하므로 target은 1로 초기화한다.  
__왜 위와 같이 하면 될까?__  
1부터 target - 1 까지의 모든 수는 만들 수 있다고 가정했다. 그럼 pays에서 뽑은 수가 target보다 작다면 이미 만들 수 있는 수에 각각 뽑은 수를 더하여 target를 만들 수 있고 나아가 target -1 + 뽑은 수 까지 만들 수 있다. 뽑은 수가 target과 같다면 target은 뽑은 수로 바로 만들 수 있고 target-1 + 뽑은 수 까지 다 만들 수 있게 된다.
<br>

__주어진 화폐로 해당 금액을 만들 수 있을까?__  
위의 문제를 응용해서 주어진 화폐로 주어진 금액을 만들 수 있는지 묻는 문제도 풀이할 수 있을 것 같아 혼자 코딩해보았다. 책에 있는 문제가 아니라 답안은 없지만 위의 코드를 약간만 변형해서 만들어 보았다.  
```
입력 예시
3
1 3 5
9
출력 예시
yes

입력 예시
3
1 2 4
9
출력 예시
no
```
```python
import sys
input = sys.stdin.readline

n = int(input())
pays = list(map(int,input().split()))
ans = int(input()) # 주어지는 금액
pays.sort()
target = 1

start=0 # 해당 위치부터 target-1까지 만들 수 있음
for x in pays:
    if x>target: 
        start = x 
        # target보다 x값이 크다면 x ~ x + target-1는 만들 수 있음 
    target+=x
    if target >ans : # ans보다 target이 크다면 종료
        break

if start <= ans <target:
    print('yes')
else :
    print('no')
```

<br>

## 6. 볼링공 고르기
---
A, B 두 사람이 볼링을 치고 있다. 두 사람은 무게가 서로 무게가 다른 공을 고르려고 한다. 볼링공은 총 N개 있으며 각 볼링공마다 무게가 적혀있고, 공의 번호는 1번부터 순서대로 부여된다. 또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주한다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재한다.  
N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하시오. 단, (1번공, 2번공)과 (2번공, 1번공)은 같은 경우로 간주한다.  
__입력 조건__  
+ 첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 자연수 형태로 주어진다. (1<=N<=1,000, 1<=M<=10)
+ 둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어진다.(1<=K<=M)

__출력 조건__  
+ 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력한다.

```
입력 예시
5 3
1 3 2 3 2

출력 예시
8
```

### 내가 작성한 코드
```python
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
ball = list(map(int, input().split()))
pick = list(combinations(ball, 2))
count = len(pick)

for a, b in pick:
    if a == b:
        count -= 1
print(count)
```
<br>

### 모범 답안
```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ball = list(map(int,input().split()))
ball_count = [0]*(m+1)
for i in ball:
    ball_count[i]+=1

result =0
for i in range(1,m+1):
    n-=ball_count[i]
    result += ball_count[i]*n
print(result)
```
A를 기준으로 생각해보면, [A가 1무게 공을 사용하는 경우의 수 * 전체 공 개수에서 1무게 공을 뺀 개수], [A가 2무게 공을 사용하는 경우의수 * 전체 공 개수에서 1무게 공 빼고 2무게공 뺀 개수] ..... 이런 방식이다. 조합이므로 A가 1무게 공을 사용하는 과정에서 1무게 사용하는 모든 경우의 수를 계산했으므로 이후의 계산에서는 1무게 공을 사용하면 안된다.

<br>

## 7. 무지의 먹방 라이브
---
[링크](https://programmers.co.kr/learn/courses/30/lessons/42891)  
무지는 라이브 먹방을 하기로 했다. 회전판에 먹어야할 N개의 음식이 있다. 각 음식에는 1부터 N까지의 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다. 무지는 다음과 같은 방법으로 음식을 섭취한다.  
1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다. 다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
4. 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.

무지가 먹방을 시작한 지 k초 후에 네트워크 장애로 잠시 중단되었다. 무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야하는지 알고자 한다. 각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 food_times, 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하시오.  
__제한 사항__  
+ food_times는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열이다.
+ k는 방송이 중단된 시간을 나타낸다.
+ 만약 더 섭취해야할 음식이 없다면 -1을 반환한다.
+ food_times의 길이는 1이상 200,000이하이고, 원소는 1이상 100,000,000이하의 자연수 이다.
+ k는 1이상 2*10^13이하의 자연수이다.

```
입력 예시
3 5 # n, k
3 1 2 # food_times

출력 예시
1
```

### 내가 작성한 코드
```python
import sys
from collections import deque

input = sys.stdin.readline

def solution(food_times,k):
    q = deque()
    count =0 # 시간
    for i in range(n):
        if food_times[i] !=0:
            q.append(i)
    while q:
        idx = q.popleft() # 남은 시간이 0이 아닌 것들의 인덱스, 리턴할때는 +1
        food_times[idx]-=1 # 한 입 먹음
        count+=1
        if count == k: # 멈춤시간과 같아질때
            if q: # 큐에 다음 먹을게 남아 있다면
                return q.popleft()+1
            else : # 남은게 없다면
                return -1
        if food_times[idx] !=0:
            q.append(idx)
```
내가 작성한 코드는 정답은 나올 수 있지만 효율성이 매우 떨어진다. 범위가 매우 큰데 확인을 일일이 하고 있으니 말이다. 따라서 어떠한 자료구조를 이용해야 한다고 생각해내야 한다.
<br>

### 모범 답안
```python
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    # +1을 해주고 나눠줘야하지 않을까? 아니다!
    # result의 인덱스는 0부터시작
    # 만약 k-sum_value의 값이 3이라면 다음 값인 4번째 값을 리턴해야함
    # 하지만 result는 인덱스 0부터 시작하므로 3이 4 번째 값임
    return result[(k - sum_value) % length][1]  
```





<br>

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
