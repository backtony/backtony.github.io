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
__이진탐색을 사용해야 하는 문제의 특징은 엄청나게 넓은 범위에서 특정한 지점을 찾아야 하는 것이다.__

### bisect 클래스
__단순히 정렬된 배열에서 특정한 데이터를 찾도록 요구하는 문제__ 에서는 이진 탐색을 직접 구현할 필요 없이 단순히 파이썬의 표준 라이브러리 중에서 bisect 모듈을 사용하여 right, left의 인자로 같은 값을 주게되면 위치를 찾을 수 있다. bisect와 bisect_right은 같은 동작을 한다.
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
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
table = list(map(int, input().split()))

start = bisect_left(table, x)
end = bisect_right(table, x)
ans = end - start
if ans == 0:
    print(-1)
else:
    print(ans)
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

### 내가 작성한 코드
```python
def binary_search(start, end):
    # 순서가 역전되면 찾지 못함을 의미
    if start > end:
        return -1
    mid = (start + end) // 2
    # 찾으면 인덱스 반환
    if table[mid] == mid:
        return mid
    # 찾지 못했을 경우 start,end 수정
    if table[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1
    # 수정한 값을 가지고 다시 이진탐색
    return binary_search(start, end)


n = int(input())
table = list(map(int, input().split()))
print(binary_search(0, n - 1))
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

### 내가 작성한 코드
첫 번재 공부에서도 1차리뷰에서도 풀지 못했다.  
범위가 매우 넓고 특정한 위치를 찾아야 한다는 점에서 이진탐색을 생각해냈다. c개의 공유기를 설치해야하고 가장 인접한 공유기 사이의 최대 거리를 구해야 하므로 일단 맨 앞과 맨 끝에 설치하는 것이 옳다고 판단했고 이후에는 이 중간값에 설치했다. 이후에서가 문제였다. 이제 중간을 기준으로 왼쪽에서 찾아야 하는지, 오른쪽에서 찾아야하는지가 문제였다. 여기서 생각하면 할수록 선택과정이 너무 복잡해졌다. 여기서 막혔는데 이후 생각을 해보니 이렇게 막히면 내가 생각한 방법이 틀렸고 다른 방법을 찾았어야 했다.  
다시 생각해보자. 주의해야할 점은 집마다 일정 거리가 아니라 모두 다 다른 거리를 가지고 있다는 점이다. 만약 두 집 사이에 여러 집이 있는 경우가 있고 두 집 사이에는 아무 집도 없는 경우가 있는데 아무집도 없는 경우가 거리가 더 멀수도 있다는 것이다. 따라서 key포인트는 집 각각의 위치가 아니라 __집들 사이의 거리를 기준으로 접근해야 한다는 점이다.__ 이진 탐색으로 설계해야한다는 점은 눈치챘고, 접근은 집들 사이의 거리를 기준으로 한다. 집들간의 최대거리와 최소거리 사이에서 이진탐색으로 찾아나가면서 공유기 설치에 따른 최대사이거리를 찾는다. 집들 사이의 거리의 중간값으로 먼저 설치를 해보고 설치개수가 부족하다면 거리최대값을 수정해서 다시 탐색, 설치개수가 일치한다면 일단 저장하고 mid를 이용해 값을 수정하고 더 늘려보는 식으로 이진탐색을 사용하여 역전된다면 그 지점이 최대라는 것을 이용한다.
```python
n,c = map(int,input().split())
house = []

for _ in range(n):
    house.append(int(input()))
house.sort()

end = house[-1]-house[0] # 최대거리
start =1 # 집 좌표 중복없으므로 최소거리는 1

# 집간의 최소거리와 최대거리 사이에서 이진탐색으로 공유기 설치에 따른 최대사이거리를 찾는다.
# 역전될때까지 반복
while start<=end:
    cnt=1 # 첫집에 설치 카운트
    dis = house[0] # 기준이 되는 집 위치
    mid = (start+end)//2
    for i in range(1,n):
        # 설치위치 도달
        if house[i]-dis>=mid:
            cnt+=1
            dis=house[i]
            if cnt==c:
                break
    # 할댱량만큼 설치 완료
    # 뒤에 길이가 더 남아서 길이를 늘릴수 있을 수도 있으므로 확인 필요
    if cnt==c:
        ans = mid # 일단 먼저 해당 길이 저장
        start=mid+1
    # 주어진 거리가 너무 길이서 할당량만큼 설치를 못함
    else:
        end = mid-1

print(ans)
```


### 모범 답안
가장 인접한 두 공유기 사이의 거리의 최댓값을 탐색해야 하는 문제로 이해할 수 있다. 이때 각 집의 좌표가 최대 10억이므로, 이진 탐색을 이용하여 문제를 해결해야 한다. 따라서 이진 탐색으로 가장 인접한 두 공유기 사이의 거리를 조절해가며, 매 순간 실제로 공유기를 설치하여 C보다 많은 개수로 공유기를 설치할 수 있는지 체크하여 문제를 해결할 수 있다. 다만 가장 인접한 두 공유기 사이의 거리의 최댓값을 찾아야 하므로, C보다 많은 개수로 공유기를 설치할 수 있다면 가장 인접한 두 공유기 사이의 거리를 증가시켜 더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색을 수행한다.
```python
# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
     array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    # 첫째 집에는 무조건 공유기를 설치한다고 가정
    value = array[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치하기
    for i in range(1, n): # 앞에서부터 차근차근 설치 
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1

print(result)
```

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
