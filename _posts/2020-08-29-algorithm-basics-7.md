---
layout: post
title:  코드업 기초 100제 파이썬 1071 ~ 1077
subtitle:   코드업 기초 100제 파이썬 1071 ~ 1077
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1071번](#1071번)
  - [1072번](#1072번)
  - [1073번](#1073번)
  - [1074번](#1074번)
  - [1075번](#1075번)
  - [1076번](#1076번)
  - [1077번](#1077번)
  

[[코드업 기초 100제 링크](https://codeup.kr/problemsetsol.php?psid=23){: target="_blank"}]

# 1071번
```python
a=input().split()
for i in a:
    if int(i) ==0:
        break
    print(i)
```

# 1072번
```python
a = int(input())
b=input().split()
for i in range(a):    
    print(b[i])
```

# 1073번
```python
a=input().split()
for i in a:
    if int(i) ==0:
        break
    print(i)
```

# 1074번
```python
a = int(input())
for i in range(a,0,-1):
    print(i)
```

# 1075번
```python
a = int(input())
for i in range(a-1,-1,-1):
    print(i)
```

# 1076번
```python
a = ord(input())
for i in range(ord('a'),a+1):
    print(chr(i))
```

# 1077번
```python
a=int(input())
for i in range(a+1):
    print(i)
```

