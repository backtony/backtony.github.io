---
layout: post
title:  코드업 기초 100제 파이썬 1010 ~ 1026
subtitle:   코드업 기초 100제 파이썬 1010 ~ 1026
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1010번](#1010번)
  - [1011번](#1011번)
  - [1012번](#1012번)
  - [1013번](#1013번)
  - [1014번](#1014번)
  - [1015번](#1015번)
  - [1017번](#1017번)
  - [1018번](#1018번)
  - [1019번](#1019번)
  - [1020번](#1020번)
  - [1021번](#1021번)
  - [1022번](#1022번)
  - [1023번](#1023번)
  - [1024번](#1024번)
  - [1025번](#1025번)
  - [1026번](#1026번)
  

[[코드업 기초 100제 링크](https://codeup.kr/problemsetsol.php?psid=23){: target="_blank"}]

# 1010번
```python
a = int(input())
print(a)
```

# 1011번
```python
x= input()
print(x)
```

# 1012번
```python
x = float(input()) # float 실수형
print("%f" %x) # 출력 예시가 소수점 6자리 이므로 print(x)로 할 경우 오류 발생
# " " 안의 %f는 실수형을 의미하고 " " 밖의 %x는 안의 %f에 대입된다고 생각하면 된다.
```


# 1013번
```python
a,b= input().split()
print(a,b)
```
split()은 문자열을 나눈다. 인자가 공백일 경우 (스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다. 만약 문자열.split('a')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다. 기본적으로 리스트로 반환한다.

# 1014번
```python
a,b = input().split()
print(b,a)
```

# 1015번
```python
x = float(input())
print("{:.2f}".format(x))

아래 풀이도 맞는데 인식을 못하는 이유는 모르겠다.
"""
x = float(input())
print(f"{x:.2f}")
"""
```


# 1017번
```python
x = int(input())
print(x,x,x)
```

# 1018번
```python
x,y = input().split(":")
print(x,y,sep=":")
```

# 1019번
```python
x,y,z = input().split(".")
print("{:04d}.{:02d}.{:02d}".format(int(x),int(y),int(z)))
또는
print("%04d.%02d.%02d" %(int(x),int(y),int(z)))

# print(f"{int(x):04d}.{int(y):02d}.{int(z):02d}")
# 코드업에서 f-string은 인식을 못하는 것 같다.
```

# 1020번
```python
a=input().split("-")
print(*a,sep="")
또는
a,b=input().split("-")
print(a+b)
```
split함수는 원래 리스트 형태로 반환하는데 앞에 변수가 튜플이므로 각 문자열이 a와 b가 나눠진 문자열을 참조한다.

# 1021번
```python
a=input()
print(a)
```

# 1022번
```python
a=input()
print(a)
```

# 1023번
```python
a,b=input().split(".")
print(a)
print(b)
```

# 1024번
```python
a = input()
for i in a:
    print("'{}'".format(i))
```

# 1025번
```python
a = input()
for i in range(len(a)):    
    print("[{}{}]".format(a[i],'0'*(4-i)))

```

# 1026번
```python
a,b,c = input().split(":")
print(int(b))
```
