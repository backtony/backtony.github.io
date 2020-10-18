---
layout: post
title:  이진 탐색 기출문제
subtitle:   이진 탐색 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 간단 정리](#1-간단-정리)
  - [2. 정렬된 배열에서 특정 수의 개수 구하기](#2-정렬된-배열에서-특정-수의-개수-구하기)
  - [3. 고정점 찾기](#3-고정점-찾기) 
  - [4. 공유기 설치](#4-공유기-설치)
  - [5. 가사 검색](#5-가사-검색)

## 1. 간단 정리
---
### 이진 탐색
탐색의 범위를 반으로 줄여나가면서 데이터를 빠르게 탐색하는 탐색 기법이다. 이진 탐색은 배열 __내부의 데이터가 정렬되어 있을 때만__ 사용할 수 있으며, 이진 탐색 알고리즘에서는 3가지 변수를 사용한다(시작점, 끝점, 중간점)  
시작점, 끝점은 탐색하고자 하는 범위를 나타내기 위해 사용하며, 탐색 범위의 중간점에 있는 데이터와 찾고자 하는 데이터를 비교한다.  

### bisect 클래스
단순히 정렬된 배열에서 특정한 데이터를 찾도록 요구하는 문제에서는 이진 탐색을 직접 구현할 필요 없이 단순히 파이썬의 표준 라이브러리 중에서 bisect 모듈을 사용하면 된다. bisect와 bisect_right은 같은 동작을 한다.
```python
from bisect import bisect_left,bisect_right

a = [1,2,4,4,8]
print(bisect_left(a,4)) # 2 # 4가 들어가야할 가장 왼쪽 인덱스 반환
print(bisect_right(a,4)) # 4 # 4가 들어가야할 가장 오른쪽 인덱스 반환
# left는 값의 제일 왼쪽 수의 인덱스를 반환하지만
# right는 값의 제일 오른쪽 수의 +1 인덱스 값을 반환한다.

# 만약 문자열에서 사용할 경우 문자열개수우선이 아니라 각 자리에 맞춰서 우선순위에 따라 값을 반환한다
['frame', 'frodo', 'front', 'frost', 'frozen', 'kakao']
print(bisect_right(a,'frozz')) # 5가 반환된다. 4가 아니다!! 주의해라.
```
<br>

## 2. 정렬된 배열에서 특정 수의 개수 구하기
---
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이때 수열에서 x가 등장하는 횟수를 계산하시오. 시간복잡도는 O(logN)으로 설계해야한다.  
__입력 조건__  
+ 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력된다. (1<=N<=1,000,000), (-10^9<=x<=10^9)
+ 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다 (-10^9<=각 원소의 값<=10^9)

__출력 조건__  
+ 수열의 원소 중에서 값이 x인 원소의 개수를 출력한다. 단 x인 값이 없다면 -1을 출력한다.

```
입력 예시
7 2
1 1 2 2 2 2 3

출력 예시
4

입력 예시
7 4
1 1 2 2 2 2 3

출력 예시
-1
```

### 내가 작성한 코드
```python
import sys
from bisect import bisect_left,bisect_right

input =sys.stdin.readline

n,x = map(int,input().split())
num = list(map(int,input().rstrip().split()))

a = bisect_left(num,x)
b = bisect_right(num,x)
ans = b-a
if ans:
    print(ans)
else :
    print(-1)
```

### 모범 답안
```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
```
내 코드와 다른 부분은 단지 함수를 따로 만들어서 사용했다는 점
<br>

## 3. 고정점 찾기
---
고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다. 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있다. 이때 이 수열에서 단 하나의 고정점이 있다고 가정하고, 고정점을 출력하는 프로그램을 작성하시오. 없다면 -1을 출력하시오. 시간 복잡도는 O(logN)으로 설계해야 한다.  
__입력 조건__  
+ 첫째 줄에 N이 입력 된다.(1<= N <= 1,000,000)
+ 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다. (-10^9<= 각 원소의 값 <=10^9)

__출력 조건__  
+ 고정점을 출력하고 없다면 -1을 출력한다.

```
입력 예시
5
-15 -6 1 3 7 

출력 예시
3

입력 예시
7
-15 -4 2 8 9 13 15

출력 예시
2

입력 예시
7
-15 -4 3 8 9 13 15

출력 예시
-1
```


### 모범 답안
```python
def binary_search(a,start,end):
    mid = (start+end)//2
    if start>end:
        return -1
    elif a[mid]==mid:
        return mid
    elif a[mid]>mid:
        return binary_search(a,start,mid-1)
    elif a[mid]<mid:
        return binary_search(a,mid+1,end)

# 문제 조건에 따라 이진 탐색을 사용해야 한다.
# 수열은 오름차순으로 정렬되어있으므로 바로 이진 탐색을 사용할 수 있다

n = int(input())
num = list(map(int,input().split()))
ans = binary_search(num,0,n-1)
print(ans)
```
문제 조건에 따라 이진 탐색을 사용해야 하고, 수열은 오름차순으로 이미 정렬되어 있으므로 바로 이진 탐색을 사용할 수 있다. 고정점은 인덱스 값과 해당 값이 같은 점이므로 이진 탐색으로 쉽게 풀 수 있다.
<br>

## 4. 공유기 설치
---
[문제 클릭](https://www.acmicpc.net/problem/2110){: target="_blank"}  


### 모범 답안
가장 인접한 두 공유기 사이의 거리의 최댓값을 탐색해야 하는 문제로 이해할 수 있다. 이때 각 집의 좌표가 최대 10억이므로, 이진 탐색을 이용하여 문제를 해결해야 한다. 따라서 이진 탐색으로 가장 인접한 두 공유기 사이의 거리를 조절해가며, 매 순간 실제로 공유기를 설치하여 C보다 많은 개수로 공유기를 설치할 수 있는지 체크하여 문제를 해결할 수 있다. 다만 가장 인접한 두 공유기 사이의 거리의 최댓값을 찾아야 하므로, C보다 많은 개수로 공유기를 설치할 수 있다면 가장 인접한 두 공유기 사이의 거리를 증가시켜 더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색을 수행한다.
```python
import sys
input =sys.stdin.readline

# 집 개수, 공유기 개수
n,c = map(int,input().split())
# 집 주소
address = []
for _ in range(n):
    address.append(int(input()))
# 이진 탐색을 위해 정렬
address.sort()
# gap의 최솟값과 최댓값
start = address[1]-address[0]
end = address[-1]-address[0]

# 이진탐색
while start<=end:
    cnt=1
    distance = address[0]
    mid = (start+end)//2 # mid는 최대사이거리
    # 공유기 설치
    for i in range(1,n): # 0번째집은 설치했다고 가정
        if address[i]-distance >= mid:
            cnt+=1 # 설치
            distance=address[i]
            if cnt==c:
                break
    # 주어진 공유기 개수만큼 설치된 경우
    # 사이거리값을 저장해두고 거리값을 늘려보기
    if cnt>=c:
        ans = mid
        start=mid+1
    # 공유기 개수 설치 부족
    else :
        end = mid-1
print(ans)
```
처음 start 초기화 과정에서 의문점이 있었다. 정렬 후 1,2 번째 집 사이의 거리의 차이보다 2,3번째 집 사이의 거리가 더 작을 수도 있는데 그럼 그것을 start로 초기화해야 하지 않을까라고 생각했다.  
생각해보면 공유기는 무조건 첫번째 집에 설치되어야 한다. 그리고 다음 집에 설치하기 위해서는 적어도 1번째 집과 2번째 집 사이의 거리만큼은 이동할 수 있는 거리가 되어야한다. 따라서 1,2번째 집 사이의 거리차가 범위의 최소값이 되어야하는 것이다. 


__내가 왜 답안처럼 접근을 못 했을까?__  
이진 탐색에 대해 다시 생각해보자. 이진 탐색은 탐색의 방법 중에 탐색을 빠르게 해주는 방법이다. 탐색이란 무엇인가? 컴퓨터에서 탐색 자체는 원래 원초적인 것이다. 예를 들자면, 조건에 맞는 숫자를 찾도록 0부터 시작해서 주어진 범위까지 차례대로 비교해가면서 확인하는 것이다. 근데 원초적인 방법으로 탐색을 하면 시간이 너무 오래걸리기 때문에 이진 탐색을 사용하는 것이다. 이진 탐색은 원초적인 방법과 다르게 시작을 0부터 하는 것이 아니라 주어진 범위 내에서 중간값을 찾는 값이라고 가정하고 비교해가면서 진행하는 과정이다.  
그렇다면 위의 문제에는 어떻게 적용되었나 생각해보자. 가장 인접한 공유기 사이의 최대거리를 찾아야한다. 즉, 탐색해야 한다는 것이다. 위에서 말했다싶이 탐색은 원초적이다. 최대 거리를 1이라고 가정하고 범위내에서 값을 증가시켜가면서 조건이 맞는 최대 거리를 찾으면 되는 것이다. 그렇다면 이 과정을 빠르게 수행하기 위해서 이진탐색을 사용하는 것이 이 문제의 핵심이다. 최대거리를 1부터 시작하는게 아니라 주어진 범위 내에서 중간점을 최대거리라고 가정하고 이진탐색으로 찾아나가는 것이다.
<br>

## 5. 가사 검색
---
[문제 클릭](https://programmers.co.kr/learn/courses/30/lessons/60060){: target="_blank"}  

### 내가 작성한 코드 (시간초과)
```python
from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    for queiry in queries:
        count = 0
        # ?가 접두사에 있나 접미사에 있나 판단
        # ?가 접두사에 있는 경우
        if queiry[0] == '?':
            idx = bisect_right(queiry, '?')
            # 단어별 확인작업
            for word in words:
                if queiry[idx:] == word[idx:] and len(queiry) == len(word):
                    count += 1
        # 접미사에 있는 경우
        else:
            # 이진탐색은 정렬이 된 경우에만 사용 가능
            # 정렬해서 ? 개수 카운트
            pre_queiry = list(queiry)
            pre_queiry.sort()
            idx = bisect_right(pre_queiry, '?')

            # 단어별 확인작업
            for word in words:
                if queiry[:-idx] == word[:-idx] and len(queiry) == len(word):
                    count += 1
        answer.append(count)
    return answer
```
실행결과는 맞지만 효율성 테스트에서 시간 초과 판정을 받았다. 모든 갯수를 일일이 확인했기 때문이다. 일일이 count하는 것이 아니라 조건 범위에 딱 맞게 끝에서 처음을 빼주는 형식으로 코드를 작성해야했다.

### 모범 답안
bisect로 갯수 차이 확인할 때는 관례적으로 함수 이름을 count_by_range 로 한다. bisect는 sort와 다르게 문자열의 개수 상관없이 각 자리끼리의 우선순위를 판단해서 인덱스 값을 반환한다. 예를 들어 a=[frodo, frozen]와 같이 정렬된 리스트가 있을 때 bisect_right(a,'frozz')를 사용하면 1이 아니라 2를 반환한다. 따라서 __bisect를 사용하는데 문자열의 개수에 대한 고려가 필요하다면 bisect를 사용하기 전에 우선 문자열의 길이를 기준으로 리스트를 따로 선언한 후 사용해야 한다는 점을 반드시 기억하자.__  
자주 사용되진 않지만 풀이에 사용된 replace 함수의 사용법도 기억해두고, 리스트를 뒤집어서 풀이할 수 있다는 접근도 기억해두자.  
```python
from bisect import bisect_left,bisect_right
def count_by_range(words,start,end):
    a = bisect_left(words,start)
    b = bisect_left(words,end)
    return b-a


def solution(words, queries):
    answer=[]
    array=[[] for _ in range(10001)]
    reverse_array=[[] for _ in range(10001)]
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1]) # 접두사의 경우 처리를 위해

    # 정렬
    for i in range(1,10001):
        array[i].sort()
        reverse_array[i].sort()

    for query in queries:
        # 접미사
        if query[0] !='?':
            answer.append(count_by_range(array[len(query)],query.replace('?','a'),query.replace('?','z')))
        # 접두사
        else:
            answer.append(count_by_range(reverse_array[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
    return answer
```
<br>


---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
