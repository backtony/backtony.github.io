---
layout: post
title:  코드업 기초 100제 파이썬 1059 ~ 1070
subtitle:   코드업 기초 100제 파이썬 1059 ~ 1070
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1059번](#1059번)
  - [1060번](#1060번)
  - [1061번](#1061번)
  - [1062번](#1062번)
  - [1063번](#1063번)
  - [1064번](#1064번)
  - [1065번](#1065번)
  - [1066번](#1066번)
  - [1067번](#1067번)
  - [1068번](#1068번)
  - [1069번](#1069번)
  - [1070번](#1070번)

[[코드업 기초 100제 링크](https://codeup.kr/problemsetsol.php?psid=23){: target="_blank"}]



# 1059번
```python
a = int(input())
print(~a)
```
+ 부정 연산자(~) : 2진법에서 ~연산은 1을 0으로, 0을 1로 바꾼다. 결과적으로 10진법에서는 ~n = -n -1의 관계가 성립한다.
+ 10진법 음수 -> 2진법 음수 : 10진법 음수에서 부호를 빼고 2진법으로 만든다. 보수로 만든다.(0과 1을 바꾼다) 1을 더한다. 그러면 해당 10진법 음수를 2진법 음수로 만든게 된다.(참고로 32비트에서 맨 앞자리는 0이면 양수 1이면 음수를 나타낸다.)


# 1060번
```python
a,b = input().split()
print(int(a)&int(b))
```
+ 비트별 논리곱 연산(&) : &연산은 두 비트가 모두 1인 경우에만 1로 계산한다.


# 1061번
```python
a,b = input().split()
print(int(a)|int(b))
```
+ 비트별 논리합 연산자(\|) : \| 연산은 두 비트 중에서 하나라도 참이면 1로 계산


# 1062번
```python
a,b = input().split()
print(int(a)^int(b))
```
+ 비트별 배타적 논리합 연산자(^) : ^연산은 두 비트가 서로 다른 경우에만 1로 계산

# 1063번
```python
a,b = input().split()
print(int(a) if int(a)>int(b) else int(b))
```


# 1064번
```python
x = input().split()
y = map(int,x)
print(min(y))
```


# 1065번
```python
a = input().split()
a = map(int,a)
for i in a:
    if i%2==0:
        print(i)
```


# 1066번
```python
a = input().split()
a = map(int,a)
for i in a:
    if i%2==0:
        print('even')
    else :
        print('odd')
```


# 1067번
```python
a = int(input())
if a>0:
    print('plus')
    if a%2==0:
        print('even')
    else :
        print('odd')
else :
    print('minus')
    if a%2==0:
        print('even')
    else :
        print('odd')
```


# 1068번
```python
a = int(input())
if 90<=a<=100: print('A')
elif 70<=a<=89: print('B')
elif 40<=a<=69: print('C')
else : print('D')
```


# 1069번
```python
a = input()
if a == 'A': print('best!!!')
elif a == 'B': print('good!!')
elif a =='C': print('run!')
elif a == 'D': print('slowly~')
else : print("what?")
```


# 1070번
```python
a = int(input())
if a ==12 or a == 1 or a == 2: print('winter')
elif a == 3 or a == 4 or a == 5: print('spring')
elif a == 6 or a == 7 or a == 8: print('summer')
else : print('fall')
```
