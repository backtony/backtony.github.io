---
layout: post
title:  파이썬 파트 4-1. 집합 자료형, 리스트와 반복문
subtitle:   파이썬 파트 4-1. 집합 자료형, 리스트와 반복문
categories: python
tags: basics book python 
comments: true
# header-img:
---
+ __목차__
  - [1. 리스트](#1-리스트)
  - [2. for 반복문](#2-for-반복문)
  - [3. 집합 자료형](#3-집합-자료형)


## 1. 리스트
---
### 리스트 선언하고 요소에 접근하기
```
기본형태
[요소, 요소, 요소...]

list_a = [273, 32, 103, "문자열", True, False]
list_a[-1] # False
list_a[-2] # True
list_a[3][0] # 문  => 인덱스 3 인 문자열을 가져오고 거기서 0번째 인덱스
list_a[[1,2,3],[4,5,6]]
```
+ 리스트는 한 가지 자료형만으로 구성할 수도 있고 여러 종류의 자료형으로 구성할 수도 있다.
+ 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있다.
+ 리스트 접근 연산자를 이중으로 사용할 수 있다.
+ 리스트 안에 리스트를 사용할 수 있다.
+ 리스트의 길이를 넘는 인덱스 접근시 IndexError 예외

<br>

### 리스트 연산자: 연결(+), 반복(*), len()
```
list_a = [1,2,3]
list_b = [4,5,6]

print(list_a + list_b) # [1,2,3,4,5,6]
print(list_a * 3) # [1,2,3,1,2,3,1,2,3]
print(len(list_a)) # 3
```
<br>

### 리스트에 요소 추가하기: append, insert, extend
+ 리스트명.append(요소) : 리스트 뒤에 요소 추가
+ 리스트명.insert(위치,요소) : 리스트 중간에 추가, 해당 위치의 요소는 뒤로 밀림
+ 리스트명.extend(리스트) : 매개변수로 리스트를 입력받아 원래 리스트 뒤에 새로운 리스트의 요소를 모두 추가

```
list_a = [1,2,3]
list_a.append(4) # [1,2,3,4]
list_a.insert(1,5) # [1,5,2,3,4]
list_a.extend([1,2,3]) # [1,5,2,3,4,1,2,3]
```

__cf) 리스트 연결 연산자와 요소 추가의 차이__  
+와 *의 연산자의 경우 본래 변수에는 어떠한 변화도 없는 비파괴적 처리이고 append, insert, extend 의 요소 추가의 경우 본래 변수에 영향을 주는 파괴적 처리이다.  
<br>

### 리스트 요소 제거하기: del, pop, remove, clear
+ del 리스트명[인덱스] : 특정 인덱스 요소 제거, 범위 지정 가능
+ 리스트명.pop(인덱스) : 특정 인덱스 요소 제거, 매개변수 미입력시 자동으로 -1이 들어가 마지막 요소 제거
+ 리스트.remove(값) : 값을 지정해서 가장 먼저 발견되는 하나만 제거
+ 리스트.clear() : 리스트 내부의 요소를 모두 제거

```
list_a = [0,1,2,3,4,5]

del list_a[1] # [0,2,3,4,5]
list_a.pop(2) # [0,2,4,5]
del list_a[0:3] # [5]

list_b = [1,2,1,2]
list_b.remov(2) # [1,1,2]
list_b.clear() # []
```
<br>

### 리스트 정렬하기
+ sort() : 기본 정렬 기능으로 오름차순으로 정렬한다.
+ sort(reverse = True) : 내림차순으로 정렬한다.

시간복잡도 O(NlogN)  
```
a = [1,4,3]
a.sort()
print(a) # [1,3,4]
a.sort(reverse = True)
print(a) # [4,3,1]
```


<br>

### 리스트 내부에 있는지 확인하기: in, not in 
+ 값 in 리스트 : 있으면 True 없으면 False
+ 값 not in 리스트 : 없으면 True 있으면 False

```
list_a = [1,2,3]
print(1 in list_a)  # True
print(5 not in list_a) # True
```
<br>

## 2. for 반복문
---
__기본 형태__
```
for 반복자 in 반복할 수 있는것 :
    코드
```
if와 마찬가지로 콜론(:) 반드시 필요  
```
arr = [273,32,103]

for i in arr
     print(arr)

# 출력
273
32
103

# 문자열도 가능
for i in "안녕"
    print(i)

# 출력
안
녕
```
<br>

__문제 : 주어진 리스트에서 자릿수 출력하기__  
```
numbers = [273,103,5,32,65,9,72,800,99]

for i in numbers:
    print("{}는 {} 자리수 입니다".format(i,len(str(i))))
```
리스트 안에 정수가 들어있으므로 정수를 str함수로 문자형으로 바꾼뒤 len 함수를 이용해서 자리수 출력가능  

__cf) print문 공백 없애는 법__  
+ 숫자의 경우 str로 문자열로 바꾼후 + 연산자 사용
+ format함수 사용

<br>

## 3. 집합 자료형
---
집합은 기본적으로 리스트 혹은 문자열을 이용해서 만들 수 있는데, 다음과 같은 특징이 있다.
+ 중복을 허용하지 않는다.
+ 순서가 없다.

리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다. 반면에 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다는 특징이 있다. 이와 더불어 집합 자료형에서는 키가 존재하지 않고, 값 데이터만을 담게 된다. 특정 원소가 존재하는지를 검사하는 연산의 시간 복잡도는 사전 자료형과 마찬가지로 O(1)이다.  

### 초기화 방법
set() 함수를 이용하거나, 중괄호 {} 안에 각 원소를 콤마를 기준으로 구분해서 넣으면 된다.  
```
data = set([1,1,2,3,4,4,5])
print(data) # {1,2,3,4,5}

data = {1,1,2,3,4,4,5}
print(data) # {1,2,3,4,5}

# 완전 같은 1,1은 중복이 제거되고 순서가 다른 1,2 2,1은 유지된다.
# 중복순열을 찾을 때 사용할 수 있다.
data = {(1,1),(1,1),(2,1),(1,2)} 
```

### 집합 자료형의 연산
기본적인 집합 연산으로는 합집합(|), 교집합(&), 차집합(-) 연산이 있다.
```
a= {1,2,3,4,5}
b = {3,4,5,6,7}
print(a|b) # {1,2,3,4,5,6,7}
print(a&b) # {3,4,5}
print(a-b) # {1,2}
```

### 집합 자료형 관련 함수
+ add() : 추가(O(1))
+ update() : 여러 개의 값을 한 번에 추가
+ remove() : 특정 값 제거 (O(1))

```
data = {1,2,3}
data.add(4) # {1,2,3,4}
data.update({5,6}) # {1,2,3,4,5,6} # ([5,6]) 도 가능
data.remove(3) # {1,2,4,5,6}
```

### 집합 인덱싱
list로 형변환을 시켜준 뒤 접근한다.
```
data = {1,2,3}
data = list(data)
print(data[0]) # 1
```


---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__