---
layout: post
title:  코드업 기초 100제 파이썬 1047 ~ 1058
subtitle:   코드업 기초 100제 파이썬 1047 ~ 1058
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1047번](#1047번)
  - [1048번](#1048번)
  - [1049번](#1049번)
  - [1050번](#1050번)
  - [1051번](#1051번)
  - [1052번](#1052번)
  - [1053번](#1053번)
  - [1054번](#1054번)
  - [1055번](#1055번)
  - [1056번](#1056번)
  - [1057번](#1057번)
  - [1058번](#1058번)

[[코드업 기초 100제 링크](https://codeup.kr/problemsetsol.php?psid=23){: target="_blank"}]


# 1047번
```python
x = int(input())
print(x<<1)
```

+ 왼쪽 시프트 연산자(<<)
    - 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동
    - 왼쪽으로 1비트 밀때마다 2배씩 증가
    - ex) a << b : a^(2^b)
+ 오른쪽 시프트 연산자(>>)
    - 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동
    - 오른쪽으로 1비트 밀때마다 1 / 2 씩 줄어든다
    - ex) a >> b : a/(2^b)


# 1048번
```python
a,b = input().split()
print(int(a)<<int(b))
```

# 1049번
```python
a,b = input().split()
a = int(a)
b = int(b)
if a>b:
    print(1)
else :
    print(0)
```

# 1050번
```python
a,b = input().split()
a = int(a)
b = int(b)
if a==b:
    print(1)
else :
    print(0)
```

# 1051번
```python
a,b = input().split()
a = int(a)
b = int(b)
if a<=b:
    print(1)
else :
    print(0)
```

# 1052번
```python
a,b = input().split()
a = int(a)
b = int(b)
if a!=b:
    print(1)
else :
    print(0)
```

# 1053번
```python
a = int(input())
print(int(not a)) 
# not으로 True or Flase를 int로
```

# 1054번
```python
a,b = input().split()
if a == '1' and b == '1':
    print(1)
else :
    print(0)
```

# 1055번
```python
a,b = input().split()
if a =='1' or b =='1':
    print(1)
else :
    print(0)
```

# 1056번
```python
a,b = input().split()
if a != b:
    print(1)
else :
    print(0)
```

# 1057번
```python
a,b = input().split()
if a==b:
    print(1)
else :
    print(0)
```

# 1058번
```python
a,b = input().split()
if a =='0' and b =='0':
    print(1)
else :
    print(0)
```