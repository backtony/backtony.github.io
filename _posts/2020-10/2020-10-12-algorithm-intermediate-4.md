---
layout: post
title:  정렬 기출문제
subtitle:   정렬 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 간단 정리](#1-간단-정리)
  - [2. 국영수](#2-국영수)
  - [3. 안테나](#3-안테나) 
  - [4. 실패율](#4-실패율)
  - [5. 카드 정렬하기](#5-카드-정렬하기)

## 1. 간단 정리
---
정렬은 데이터를 특정한 기준에 따라서 정렬하기 위해 사용하는 알고리즘이다. 대표적인 정렬 라이브러리를 성능에 따라서 비교하는 다음과 같다.

정렬 알고리즘|평균 시간 복잡도|공간 복잡도|특징
---|---|---|---|---
선택 정렬|O(N^2)|O(N)|아이디어가 매우 간단
삽입 정렬|O(N^2)|O(N)|데이터가 거의 정렬되어 있을 때는 가장 빠름
퀵 정렬|O(NlogN)|O(N)|대부분의 경우에 가장 적합하며, 충분히 빠름
계수 정렬|O(N+K),(K는 데이터 중 가장 큰 양수)|O(N+K),(K는 데이터 중 가장 큰 양수)|데이터의 크기가 한정되어 있는 경우에만 사용 가능, 매우 빠름

또한 각 정렬 알고리즘의 동작 아이디어를 한 문장으로 정리하면 다음과 같다.

정렬 알고리즘|핵심 아이디어
---|---
선택 정렬|가장 작은 데이터를 선택해서 정렬되지 않은 데이터 중에서 가장 앞쪽에 있는 데이터와 위치를 바꾸는 방법
삽입 정렬|데이터를 앞에서부터 하나씩 확인하며 데이터를 적절한 위치에 삽입하는 방법
퀵 정렬|기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
계수 정렬|특정한 값을 가지는 데이터의 개수를 카운트 하는 방법

파이썬의 표준 라이브러리에서 기본으로 제공하는 정렬 라이브러리는 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다. 따라서 계수 정렬을 사용해 매우 빠르게 정렬해야 하는 특이한 케이스가 아니라면 파이썬의 정렬 라이브러리를 사용하는 것이 가장 합리적이다. 정렬은 다양한 알고리즘에서 사용되는데, 대표적으로 이진 탐색의 경우 데이터가 정렬되어 있을 때만 사용할 수 있다. 크루스칼 알고리즘의 경우, 간선의 정보를 정렬하는 과정이 반드시 필요하다. 
<br>

## 2. 국영수
---
[문제 클릭](https://www.acmicpc.net/problem/10825){: target="_blank"}  

### 내가 작성한 코드
```python
n = int(input())
table = []

for _ in range(n):
    table.append(input().split())

table.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(n):
    print(table[i][0])
```
파이썬의 정렬 내장함수는 최악의 경우에도 NlogN을 보장하기 때문에 주어진 범위 내에서 충분히 사용할 수 있다.



<br>

## 3. 안테나
---
[문제 클릭](https://www.acmicpc.net/problem/18310){: target="_blank"}  

### 내가 작성한 코드
```python
n = int(input()) # 집의수
table = list(map(int,input().split())) # 집의 위치
table.sort() # 정렬
print(table[(n-1)//2]) # 정렬후 가장 가운데 있는 곳에 설치해야 최소
```
범위가 200,000만 이므로 적어도 선형 로그 시간 알고리즘으로 설계해야한다. 따라서 각각의 위치에 설치하고 일일이 비교하는 설계는 시간초과가 발생할 것이다. 내장함수를 이용해서 정렬하고 결국 집들의 가운데 있는 집에 설치하는 것이 최소거리를 만족할 것이므로 집들 중에서 가운데 있는 곳에 설치하면 된다. 홀수는 상관없으나 짝수의 경우 인덱스때문에 -1을 해주고 나눗셈을 해줘야 제일 먼저 나오는 최소거리 집의 위치가 된다.

<br>

## 4. 실패율
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/42889){: target="_blank"}  

### 내가 작성한 코드
```python
def solution(n,stages):
    answer=[]
    table=[0]*(n+2)# 해당 스테이지에 도달했으나 클리어 못한 플레이어 리스트
    passer=[0]*(n+2) # 스테이지에 도달한 플레이어수
    fail=[0]*(n)

    # 스테이지에 도달했으나 클리어 못한 플레이어수 처리
    for i in stages:
        table[i]+=1

    # 해당 스테이지를 클리어한 플레이어수
    for i in range(n,0,-1):
        passer[i]=passer[i+1] + table[i+1]

    print(passer)
    # 실패율
    for i in range(n):
        # 도달한 유저가 없는 경우
        if passer[i+1]+table[i+1]==0:
            fail[i] = (0,i+1)
        else:
            fail[i] = (table[i+1]/(passer[i+1]+table[i+1]),i+1)

    fail.sort(key = lambda x:(-x[0],x[1]))

    for i in range(n):
        answer.append(fail[i][1])

    return answer
```
실패율을 처리할 때 모범답안과 같이 length를 이용해서 하는 것이 더 좋아보인다. 코딩 기술보다 뭔가 사고적인것을 요구하는 문제인 것 같다. 앞으로 단계별 퍼센트를 구하는 문제의 경우 전체길이를 생각하고 처음부터 구하면서 길이를 이용하는 방법을 먼저 생각해보도록 하자.

<br>

2차 리뷰 코드
```python
def solution(N, stages):
    position=[0] *(N+2)
    people = len(stages) # 총 인원
    temp = []
    # 각 스테이지별 사람
    for i in stages:
        position[i]+=1

    # 실패율
    for i in range(1,N+1):
        if position[i]==0:
            rate=0
        else :
            rate = position[i]/people
        temp.append((rate,i)) # 실패율, 층수
        people-=position[i] # 스테이지 올라간 사람 수정

    temp.sort(key=lambda x:(-x[0],x[1])) # 실패율 높은 순 정렬

    answer = [x[1] for x in temp]

    return answer
```

### 모범답안
```python
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if count == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    # 애초에 스테이지 번호가 작은 순으로 저장되었기때문에 기준으로 정렬한 뒤에는
    # 원래 있었던 순으로 정렬되므로 따로 스테이지 번호순 정렬을 할 필요가 없다.
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer
```


<br>

## 5. 카드 정렬하기
---
[문제 클릭](https://www.acmicpc.net/problem/1715){: target="_blank"}  

### 내가 작성한 코드
첫 공부때는 풀었으나 1차 리뷰때는 풀지 못했다.  
첫 시도에서는 덧셈결과값이 작으면 되니까 정렬하고 0부터 차례대로 더하는 식으로 설계했다. 하지만 이렇게 하면 나중에 어느 순간에는 덧셈결과값이 이제 덧셈할 값보다 커지게 되는 순간이 오므로 최소값이 아니게 된다.  
문제상 결국 덧셈에서 앞서 계산한 결과값이 중복되므로 최소한의 결과를 내려면 앞서 계산값이 항상 최소값이어야 한다. 그렇다면 __항상 작은 것을 꺼내서 작은 것끼리 더애햐 한다는 점에서 우선순위 큐__ 를 생각해내야 한다. __while문의 조건으로 len(우선순위큐)로 우선순위큐의 길이또한 조건으로 사용할 수 있음을 기억해두자.__
```python
import heapq
# 문제에서 주어진바에 따르면 가장 작은 것끼리의 합이 최적의 해를 보장한다.
n = int(input())

card = []
for _ in range(n):
    heapq.heappush(card,int(input()))


tot=0 # 최소비교횟수

# 우선순위큐에 남은게 1개면 연산 끝
while len(card) !=1:
    a= heapq.heappop(card)
    b= heapq.heappop(card)
    tot +=a+b
    heapq.heappush(card,a+b)

print(tot)
```
<br>

2차 리뷰 코드
```python
import heapq
n = int(input())
q=[]
for _ in range(n):
    heapq.heappush(q,int(input()))

ans =0
while len(q)>1:
    ans += heapq.heappop(q) + heapq.heappop(q)
    heapq.heappush(q,ans)

print(ans)
```



  

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
