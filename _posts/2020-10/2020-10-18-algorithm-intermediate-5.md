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
범위가 매우 넓고 특정한 위치를 찾아야 한다는 점에서 이진탐색을 생각해냈다. c개의 공유기를 설치해야하고 가장 인접한 공유기 사이의 최대 거리를 구해야 하므로 일단 맨 앞과 맨 끝에 설치하는 것이 옳다고 판단했고 이후에는 이 중간값에 설치했다. 이후에서가 문제였다. 이제 중간을 기준으로 왼쪽에서 찾아야 하는지, 오른쪽에서 찾아야하는지가 문제였다. 여기서 생각하면 할수록 선택과정이 너무 복잡해졌다. 여기서 막혔는데 이후 생각을 해보니 이렇게 막히면 내가 생각한 방법이 틀렸고 다른 방법을 찾았어야 했다. 그리고 접근이 틀린점이 공유기간의 최소거리가 가장 큰 경우는 결국에 모든 공유기 사이의 거리가 같아야 한다. 정해진 거리에서 공유기를 설치하는 것이기 때문에 어느쪽이 멀면 어느쪽은 가까워지게 되기 때문이다.  
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
<br>

2차 리뷰에서도 풀지 못했다. 1차 리뷰처럼 접근에서 실패하진 않았다. 양쪽 설치하고 쪼개고 쪼개면 어느쪽을 선택하는지에 대해 방법이 틀렸다는 것을 인지했고, 범위가 넓고 특정 거리를 찾는 것이므로 이진탐색, 집의 위치가 아닌 집들 사이의 거리를 기준으로 설계해야한다는 것까지 생각했다. 하지만 여기서 이진탐색으로 거리를 구하고 첫 위치에서 더했을 때 그 지점에 집이 없다면 어떻게 처리해야 하는가에서 막혔다. 답안에서 보면 if array[i] >= value + mid: 이 코드를 이해하지 못했다. 첫 위치에서 이진탐색으로 구한 거리를 더했을 때 바로 그 위치에 집이 없고 그 뒤에 집이 있다면 어떻게 해야할까?, 만약 조건에서 =가 성립되지 않고 계속 > 이면 어떻게 처리해야할까에서 이해하지 못했다. 다시 생각해보면 이것은 이진탐색의 과정에서 처리해준다. 만약 계속 >이면 while문이 돌면서 다음에는 최소거리가 더 커질 것이다. 이 과정을 계속하다보면 결국 >이면서 =인 경우가 나올 때까지 반복하게 되는 것이다. 그리고 더했을 때 그 위치에 집이 없고 뒤에 있는 경우의 처리는 현재의 위치를 수정해가면서 진행하면 해결된다. 그리고 start와 end가 찾을 수 있는 탐색은 다 끝났다는 뜻.
<br>

3차 리뷰 코드
```python
n, c = map(int, input().split())
homes = []
for _ in range(n):
    homes.append(int(input()))
homes.sort()

start = 1
end = homes[-1] - homes[0]
ans = 0
while start <= end:
    mid = (start + end) // 2  # 공유기 사이의 최소 거리
    pos = homes[0] + mid
    cnt = 1
    for home in homes[1:]:
        # 최소거리에 걸치거나 범위 밖에 집이 있는 경우 pos값 수정
        # 현재는 최소거리 mid를 더한 위치에 집이 없을 수 있지만
        # 이진탐색이 진행되면서 최소거리mid을 더한 위치에서 집이 만나는 시점의 값 중 mid의 최대거리를 찾아준다.
        if pos <= home:
            pos = home + mid
            cnt += 1

    if cnt >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

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
처음 공부와 1차 리뷰에서 둘 다 풀지 못했다. 둘 다 시간 초과가 나왔고 작성한 코드도 거의 비슷했다. 생각을 다르게 해야할 필요가 있다.
```python
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    for query in queries:
        n = len(query)  # 쿼리의 길이
        tmp_query = sorted(query)
        length = bisect_right(tmp_query, '?') - bisect_left(tmp_query, '?')  # ? 갯수
        # 물음표가 뒤에서 부터 있음
        if query[0] != '?':
            cnt = 0
            for word in words:
                # 길이가 같고 문자가 같으면
                if n == len(word) and query[:n - length] == word[:n - length]:
                    cnt += 1
            answer.append(cnt)
        # ?가 맨 앞에서부터 있는 경우
        else:
            cnt = 0
            for word in words:
                # 길이가 같고 문자가 같으면
                if n == len(word) and query[length:] == word[length:]:
                    cnt += 1
            answer.append(cnt)

    return answer
```
범위가 매우 크고 특정 위치를 찾는다는 점에서 이진탐색을 생각해냈고, 이진탐색의 조건은 이미 정렬이 완료된 상태여야 한다는 점을 고려해서 '?'의 개수를 카운트 하는 부분에서 이진탐색을 활용할 수 있다고 생각했다. 하지만 문자열을 비교하느 부분에서는 딱히 효율적인 풀이가 생각나지 않았다. 풀이를 보니 내가 생각한 접근방식이 잘못되었다. 결론적으로 ?의 개수를 구하고 남은 부분을 비교한다는 설계자체가 일일이 비교한다는 가정에 작성된 설계라 시간을 너무 많이 소요하게 되는 것이었다. 따라서 다른 접근 방식을 생각해내야만 했다. 복잡도를 고려할 때 주어진 쿼리단어에 만족하는 단어들을 한 번에 묶어서 만족하는 개수를 구해내야했다.
<br>

2차 리뷰(효율성 테스트 실패)  
```python
from bisect import bisect_left, bisect_right


def check(query_a, query_z, word):
    word.sort() # 아래 for문 넣고 이거 지워줘야함
    return bisect_right(word, query_z) - bisect_left(word, query_a)


def solution(words, queries):
    answer = []
    length_tb = [[] for _ in range(10001)]
    reverse_length_tb = [[] for _ in range(10001)]
    for word in words:
        length_tb[len(word)].append(word)
        reverse_length_tb[len(word)].append(word[::-1])

    # for i in range(10001):
    #     length_tb[i].sort()
    #     reverse_length_tb[i].sort()

    for query in queries:
        if query[-1] == '?':
            answer.append(check(query.replace('?', 'a'), query.replace('?', 'z'),
                                length_tb[len(query)]))
        else:
            answer.append(check(query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'),
                                reverse_length_tb[len(query)]))

    return answer
```
효용성테스트 1,2,3번을 통과하지 못했다. solution 함수에서 sort하는 것보다 필요한 것만 check함수로 넘겨서 그 부분만 sort하는 것이 더 빠른 효율성을 보여주는 것이 당연하다고 생각했다. 하지만 결과는 정반대였다. 오히려 solution 함수내에서 정렬을 끝내고 check의 파라미터로 넘겨주는게 훨씬 더 효율적인 코드였다. 이유는 쿼리의 개수 때문이다. check의 파라미터로 넣기 전에 먼저 정렬을 하고 보내주면 총 20002번의 정렬만 하면 된다. 하지만 파라미터로 넣어주는 경우 queries가 최대 10만개이므로 최대 10만번의 정렬을 수행해야한다. 그러므로 먼저 정렬하고 넣어주는 것이 더욱 효율적인 코드이다.


### 모범 답안
bisect는 각 자리끼리의 우선순위를 판단해서 인덱스 값을 반환한다. 예를 들어 a=[frodo, frozen]와 같이 정렬된 리스트가 있을 때 bisect_right(a,'frozz')를 사용하면 1이 아니라 2를 반환한다. 즉, 문자열의 길이를 고려하지 않고 사전순으로 찾아간다는 뜻이다. 따라서 이 문제와 같이 __넓은 범위 내에서 특정위치를 찾아가야하는데 문자열의 길이를 고려해야 한다면 bisect를 사용하기 전에 우선 문자열의 길이를 기준으로 리스트를 따로 선언한 후 사용해야 한다는 점을 반드시 기억하자.__  
'?'이 뒤쪽에 있는 경우는 '?'을 'a'와 'z'로 교체하고 비교하면 쉽게 구할 수 있다. 하지만 '?'가 맨 앞에 있는 경우는 다른 방법을 생각해내야 한다. 왜냐하면 앞에 있는 '?'를 'a'와 'z'로 바꾸게 되면 당연히 맨 앞과 맨 뒤를 차지하게되어 모든 단어를 포함하게 되기 때문이다. 그렇다면 '?'를 뒤로 옮기기위해서 뒤집으면 어떨까? 괜찮다. 왜냐하면 구하는 것은 각 인덱스에 해당하는 문자가 같은지 판단하는 것이기 때문이다.
자주 사용되진 않지만 풀이에 사용된 replace 함수의 사용법도 기억해두고, 리스트를 [::-1]로 뒤집는 방법도 기억해두자.  
```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드 카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드 카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer
```

__이 문제에서 배울점__  
사실 문자열 비교는 일일이 비교하거나, c언어의 strcmp밖에 생각나지 않았다. __파이썬에서는 위 문제와 같이 앞이나 뒤에 문자열이 같은지를 확인하는 경우 문자열 길이별로 저장, 정렬한 뒤에 문자를 수정하거나 추가해 이진탐색을 이용하여 일치하는 문자열을 찾을 수 있다는 점을 반드시 기억해두자. 하지만 앞,뒤가 아닌 중간에서 일치하는 여부는 다른 방법을 생각해야한다.__


<br>

4번, 5번을 다시 풀어볼 필요가 있다.


<br>


---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
