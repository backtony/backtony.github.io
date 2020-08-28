---
layout: post
title:  코드업 기초 100제 파이썬 1028 ~ 1037
subtitle:   코드업 기초 100제 파이썬 1028 ~ 1037
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1028번](#1028번)
  - [1029번](#1029번)
  - [1030번](#1030번)
  - [1031번](#1031번)
  - [1032번](#1032번)
  - [1033번](#1033번)
  - [1034번](#1034번)
  - [1035번](#1035번)
  - [1036번](#1036번)
  - [1037번](#1037번)

[[코드업 기초 100제 링크](https://codeup.kr/problemsetsol.php?psid=23){: target="_blank"}]


# 1028번
```python
print(int(input()))
```

# 1029번
```python
x = float(input())
print("%.11f" %x)
```

# 1030번
```python
print(int(input()))
```

# 1031번
```python
x = int(input())
print("%o" %x)
```

# 1032번
```python
x = int(input())
print("%x" %x)
```

# 1033번
```python
x = int(input())
print("%X" %x)
```

# 1034번
```python
x = input()
print(int(x,8))
int(a, b) # a는 n진수 형태인데 문자열이어야함
```
int는 n진수를 10진수로 변환시켜준다.

# 1035번
```python
x = input()
x = int(x,16)
x= oct(x)
print(x[2:]) # 범위지정 안하면 0o가 앞에 붙어서 출력된다.

또는
x = input()
x = int(x,16)
print("%o" %x)
```
__cf) 진수변환__  
10진수 -> 2, 8, 16 진수  
+ 2진수로 변환 : bin()
+ 8진수로 변환 : oct()
+ 16진수로 변환 : hex()


# 1036번
```python
x = input()
print(ord(x))
```
아스키코드값 정수로 바꿔주는 내장함수 ord() 사용

# 1037번
```python
x = int(input())
print(chr(x))
```
아스키코드값 정수를 문자로 바꿔주는 내장함수 chr() 사용
