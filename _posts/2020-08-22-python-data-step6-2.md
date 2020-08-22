---
layout: post
title:  파이썬 자료구조 6-2장. 정렬 알고리즘 2
subtitle:   파이썬 자료구조 6-2장. 정렬 알고리즘 2
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---

+ __목차__
  - [1. 셸 정렬](#1-셸-정렬)
  - [2. 퀵 정렬](#2-퀵-정렬)
  - [3. 비재귀적인 퀵 정렬 만들기](#3-비재귀적인-퀵-정렬-만들기)
  - [4. sorted() 함수로 정렬하기](#4-sorted-함수로-정렬하기)



## 1. 셸 정렬
---
셸 정렬은 먼저 정렬한 배열의 원소를 그룹으로 나눠 각 그룹별로 정렬을 수행한다. 그 후 정렬된 그룹을 합치는 작업을 반복하여 원소의 이동 횟수를 줄이는 방법이다. 예를 들어 [8,1,4,2,7,6,3,5]라는 배열이 있을 때 처음에는 서로 4칸 떨어진 원소를 정렬하는 방법(4-정렬)으로 [8,7] [1,6] [4,3] [2,5] 4 그룹으로 나눠서 정렬을 마치고 이어서 2칸 떨어진 원소를 모두 꺼내어 [7,3,8,4] [1,2,6,5] 2 그룹으로 나눠서(2-정렬) 수행하고 마지막으로 한 칸 떨어진 배열(1-정렬), 즉 배열 전체에 적용하면 정렬이 완료된다. 이 7번의 정렬 과정은 모두 단순 삽입 정렬로 수행된다. 셸 정렬은 단순 삽입 정렬의 장점은 살리고 단점을 보완하기 위해서 사용된다. 정렬 횟수는 늘어나지만 전체적으로 원소의 이동 횟수가 줄어들어 효율적이다.  
```
# 부족한 셸 정렬
def shell_sort(a):
    n = len(a)
    h = n//2
    while h>0 : # h만큼 떨어진 것끼리 그룹
        for i in range(h,n):
            j = i-h
            tmp = a[i] # 선택 정렬을 위한 저장
            while j>=0 and tmp<a[j]:
                a[j+h] = a[j]
                j-=h
            a[j+h] = tmp
        h//=2
```
n의 값이 8이라면 h는 4->2->1로 변화한다. a = [8,1,4,2,7,6,3,5] 라는 배열이 있다고 하자. 4-정렬로 만들면 [8,7] [1,6] [4,3] [2,5]가 만들어지고 2-정렬로 만들면 [7,3,8,4] [1,2,6,5]가 만들어진다. 이렇게 되면 [[8,7],[4,3]]과 [[1,6][2,5]]는 섞이지가 않는다. 따라서 처음과 같은 단계가 되므로 그룹을 나눠서 정렬했지만 그 기능을 충분히 수행하지 못했다고 할 수 있다. 따라서 이 문제를 해결하려면 h값이 서로 배수가 되지 않도록 해야 한다. 다음 수열을 사용하면 셸 정렬 알고리즘을 효율적으로 사용할 수 있다. 셸 정렬에 도움을 주는 수열이라고 알아두자.  
```
h=1
while h < n//9: 
  h = h*3+1 
  # h가 서로의 배수가 안나오도록 하는 수열이라고 생각해
  # //3으로 나누고 마지막에 1이 나오기 위해 +1
```
1부터 시작하여 3배한 값에 1을 더하고 있다. 하지만 h의 초기값이 지나치게 크면 효과가 없다. 따라서 배열의 원소 수인 n을 9로 나누었을 때 그 몫보다 너무 크지 않게 해야한다. h는 *3+1이므로 //3으로 나누다보면 결국 1이 나온다.  
```
# 개선한 셸 정렬
def shell_sort(a):
    n = len(a)
    h=1
    while h < n//9: # 효율적으로 h선택을 위한 수열
      h=h*3+1
    
    while h>0 : # h만큼 떨어진 것끼리 그룹
        for i in range(h,n):
            j = i-h
            tmp = a[i] # 선택 정렬을 위한 저장
            while j>=0 and tmp<a[j]:
                a[j+h] = a[j]
                j-=h
            a[j+h] = tmp
        h//=3

a = [8,1,4,2,7,6,3,5]
shell_sort(a)
print(a)
```
<br>

## 2. 퀵 정렬
---
퀵 정렬은 가장 빠른 정렬 알고리즘으로 알려져 있다. 
+ 피벗 : 그룹을 나누는 기준
+ pl : 왼쪽 끝 원소의 인덱스
+ pr : 오른쪽 끝 원소의 인덱스
+ a[pl] > x가 성립하는 원소를 찾을 때까지 pl을 오른쪽 방향으로 스캔
+ a[pr] > x가 성립하는 원소를 찾을 때까지 pr을 왼쪽 방향으로 스캔
+ pl > pr +1 인 경우는 pr과 pl이 피벗을 가리키게 되어 의미는 없지만 교환한 후에 진행되어 a[pr+1] ~ a[p-1]이 피벗과 일치하는 그룹이 생긴다. 이 그룹은 다시 나눌 필요가 없으므로 제외한다.

### 효율적인 피벗 설정
빠른 정렬을 원한다면 배열을 정렬한 뒤 가운데에 위치하는 값, 즉 전체의 중앙값을 피벗으로 하는 것이 이상적이다. 하지만 중앙값을 구하려면 그에 대한 처리가 필요하고 많은 계산 시간이 걸리므로 피벗을 구하는 의미가 없어진다. 다음과 같은 방법을 통해 피벗을 구하면 효율적이다.  
1. 나누어야 할 배열의 맽 앞 원소, 가운데 원소, 맨 끝 원소를 오름차순 정렬한다.
2. 가운데 원소와 맨 끝에서 두 번째 원소와 교환한다.
3. 맨 끝에서 두 번째 원소를 피벗으로 선택한다.

이렇게 하면 나눌 대상을 a[left+1]~[right-2]로 좁힘으로써 나눠지는 배열이 한쪽으로 치우지는 것을 방지할 수 있다.

### 시간 복잡도
퀵 정렬은 배열을 조금씩 나누어 보다 작은 문제를 푸느 과정을 반복하므로 시간 복잡도는 O(n log n)이다. 그런데 정렬하는 배열의 초깃값이나 피벗을 선택하는 방법에 따라 실행 시간 복잡도가 증가하는 경우가 있다. 예를 들어 매번 1개의 원소와 나머지 원소로 나누어진다면 n번의 분할이 필요하다. 최악의 경우는 시간 복잡도가 O(n^2)이다.  
퀵 정렬은 원소 수가 적은 경우에는 그다지 빠른 알고리즘이 아닌 것으로 알려져 있으니 원소 수가 9개 미만인 경우 단순 삽입 정렬로 전환하자.  


```
def mid(a,idx1,idx2,idx3):
    if a[idx1]>a[idx2] :
         a[idx1],a[idx2] = a[idx2],a[idx1]
    if a[idx1]>a[idx3] :
         a[idx1],a[idx3]=a[idx3],a[idx1]
    if a[idx2]>a[idx3] : 
        a[idx2],a[idx3]=a[idx3],a[idx2]
    return idx2

def insertion_sort(a,left,right):    
    for i in range(left+1,right+1):
        j= i-1
        tmp = a[i]
        while j>=0 and a[j]>tmp:
            a[j+1]=a[j]
            j-=1
        a[j+1] = tmp 

def qsort(a,left,right):    
    if right - left < 9:
        insertion_sort(a,left,right)    
    
    else :
        idx = mid(a,left,(left+right)//2,right)
        a[right-1], a[idx] = a[idx],a[right-1]
        pivot = a[right-1]
        pr = right-2
        pl = left+1

        # 같을 때도 교환을 해줘야 pr,pl 위치가 교차되어 재귀에 넣을 때 중복을 
        # 피할 뿐만 아니라 피벗과 같은 그룹을 제외 시킬 수 있다.    
        while pr>=pl:
            while pivot > a[pl]: pl+=1
            while pivot < a[pr]: pr-=1
            if pr>=pl:
                a[pl],a[pr] = a[pr],a[pl]
                pr -=1
                pl +=1
        if left <pr : qsort(a,left,pr)
        if right > pl : qsort(a,pl,right)

def quick_sort(a):
    qsort(a,0,len(a)-1)

a = [1,8,7,4,5,2,6,3,9]
quick_sort(a)
print(a)
```
<br>

## 3. 비재귀적인 퀵 정렬 만들기
---
재귀적 구현은 성능상 문제가 있을 수 있으므로 비재귀적으로 구현시 더욱 좋은 퍼포먼스를 낼 수 있다. 비재귀적 구현으로 스택을 사용하자.  

### 스택의 크기
사용할 스택의 크기를 정하는데 두 가지 규칙을 고려할 수 있다.  
1. 원소 수가 많은 쪽의 그룹을 먼저 푸시
2. 원소 수가 적은 쪽의 그룹을 먼저 푸시

원소 수가 많은 쪽의 그룹을 먼저 푸시하게되면 당연히 꺼낼 때는 적은 쪽의 그룹을 먼저 꺼내게 된다. 그 그룹이 쪼개지면서 다시 푸시된다. 하지만 적은 쪽의 그룹을 먼저 푸시해서 꺼낼 때 많은 그룹을 꺼내게 된다고 생각하면 전자보다 더 많은 쪼갬을 통해 푸시가 되어 많은 스택이 쌓이게 될 것이다. 따라서 많은 쪽의 그룹을 먼저 푸시한다면 더욱 작은 크기의 스택을 사용할 수 있다. 1번을 따라 배열의 원소 수가 n이면, 스택에 쌓이는 데이터의 최대 개수는 log n보다 적다. 따라서 원소 수 n이 100만 개라도 스택의 최대 크기는 20으로 충분하다.  

```
from module import Stack # 이전에 구현한 stack 임포트
from math import log

def mid(a,idx1,idx2,idx3):
    if a[idx1]>a[idx2] :
         a[idx1],a[idx2] = a[idx2],a[idx1]
    if a[idx1]>a[idx3] :
         a[idx1],a[idx3]=a[idx3],a[idx1]
    if a[idx2]>a[idx3] : 
        a[idx2],a[idx3]=a[idx3],a[idx2]
    return idx2

def qsort(a,left,right):    
    s=Stack(int(log(right-left+1)))
    s.push((left,right)) # 튜플

    while not s.is_empty():
        pl,pr = left,right = s.pop()        
        idx = mid(a,left,(left+right)//2,right)
        a[right-1], a[idx] = a[idx],a[right-1]
        pivot = a[right-1]
        pr -=2
        pl +=1

        while pr>=pl:
                while pivot > a[pl]: pl+=1
                while pivot < a[pr]: pr-=1
                if pr>=pl:
                    a[pl],a[pr] = a[pr],a[pl]
                    pr -=1
                    pl +=1
        # 길이가 긴 것부터 먼저 넣기
        if pr-left > right - pl:            
            if left <pr : s.push((left,pr))
            if right > pl : s.push((pl,right))            
        else :            
            if right > pl : s.push((pl,right))
            if left <pr : s.push((left,pr))          

def quick_sort(a):
    qsort(a,0,len(a)-1)

a = [1,8,7,4,5,2,6,3,9]
quick_sort(a)
print(a)
```
<br>

## 4. sorted() 함수로 정렬하기
---
파이썬에서는 정렬을 수행하는 sorted() 함수를 내장 함수로 제공한다. 이 함수는 전달받은 이터러블 객체의 원소를 정렬하여 list형으로 반환한다. 정렬을 직접 수행하지 않고 정렬을 수행한 뒤 늘어선 원소를 새로운 리스트로 생성하여 반환한다.  
```
n = int(input("원소 개수: "))
a = [None] * n

for i in range(n):
    a[i] = int(input(f"a[{i}] : "))

print("오름차순")
print(sorted(a))
print("내림차순")
print(sorted(a, reverse = True))
```
__튜플 사용하려면__  
튜플은 이뮤터블의 속성을 가지므로 튜플 자체를 정렬할 수는 없다. 정렬하고 싶다면 다음 방법을 사용하자.  
1. sorted 함수로 정렬한 원소의 나열에서 새로운 리스트를 생성한다.
2. 생성한 리스트를 튜플로 변환한다.

```
a = (1,3,2)

x = tuple(sorted(a))
print(x)
```
<br>

  
---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
