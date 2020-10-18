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
  - [2. 국영수](#2-특정한-거리의-도시-찾기)
  - [3. 안테나](#3-연구소) 
  - [4. 실패율](#4-경쟁적-전염)
  - [5. 카드 정렬하기](#5-괄호-변환)

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
import sys

input = sys.stdin.readline

n = int(input())
students = []
for i in range(n):
    name, kor, eng, math = input().rstrip().split()
    students.append([name,int(kor),int(eng),int(math)])

students.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))
for student in students:
    print(student[0])

```
내장함수를 사용했다. 모범답안과 매우 유사하다. 모범답안은 문자열을 그대로 저장하고 아래와 같이 정렬했다.
```python

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
```


<br>

## 3. 안테나
---
[문제 클릭](https://www.acmicpc.net/problem/18310){: target="_blank"}  

### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

# 집 개수와 위치
n = int(input())
location = list(map(int,input().rstrip().split()))

# 정렬하고 가운데 위치가 가장 적절한 위치
location.sort()

# n은 개수라 1부터 카운트하지만 인덱스는 0부터이므로 조정이 필요함
# 짝수개수면 인덱스는 전체 길이 나누기2 -1
if n%2==0 :
    print(location[len(location)//2-1])
# 홀수면 나누기2
else :
    print(location(len(location)//2))
```
범위가 200,000만 이므로 적어도 선형 로그 시간 알고리즘으로 설계해야한다. 따라서 받은 위치를 일일이 뺀 값을 정리해서 정렬하는 풀이는 시간초과하게 된다. 내장함수 정렬을 이용하면 쉽게 풀 수 있다.

### 모범답안
```python
n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값(median)을 출력
print(a[(n - 1) // 2])
```
홀수는 -1한 뒤 몫 나눗셈을 해도 결과값이 같다. 따라서 n-1한 값에 나누기2를 하면 짝 홀 구분없이 한번에 코드를 작성할 수 있다.
<br>

## 4. 실패율
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/42889){: target="_blank"}  

### 내가 작성한 코드
```python
def solution(N, stages):
    temp = []
    answer=[]
    count = [0] * (N + 2) # N+1은 마지막 스테이지 클리어한 사용자
    approach_people = len(stages) # 스테이지에 도달한 플레이어 수
    # 각 스테이지에 있는 인원을 count에 정리
    for i in stages:
        count[i] += 1
    # 실패율
    for stage in range(1, N + 1):
        # 도달한 사람이 없으면
        if count[stage] == 0:
            temp.append((0, stage))
            continue

        fail_percent = count[stage] / approach_people
        approach_people-=count[stage]
        temp.append((fail_percent, stage))
    temp.sort(key = lambda x:(-x[0],x[1]))
    for i in temp:
        answer.append(i[1])
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
        if length == 0:
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
내가 작성한 코드와 비슷하지만 좀 더 간결하게 작성할 수 있다는 점을 볼 수 있다.

<br>

## 5. 카드 정렬하기
---
[문제 클릭](https://www.acmicpc.net/problem/1715){: target="_blank"}  

### 내가 작성한 코드
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
더한 값보다 작은 값이 2개 이상인 경우 더한 값은 그대로 두고 다시 앞에 작은 2값을 먼저 연산해줘야 한다. 따라서 우선순위 큐를 사용하면 쉽게 풆 수 있다. 모범답안은 내 코드와 거의 유사하므로 생략한다.

  

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
