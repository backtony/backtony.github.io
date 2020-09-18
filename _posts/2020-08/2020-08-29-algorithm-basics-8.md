---
layout: post
title:  코드업 기초 100제 파이썬 1078 ~ 1092
subtitle:   코드업 기초 100제 파이썬 1078 ~ 1092
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1078번](#1078번)
  - [1079번](#1079번)
  - [1080번](#1080번)
  - [1081번](#1081번)
  - [1082번](#1082번)
  - [1083번](#1083번)
  - [1084번](#1084번)
  - [1085번](#1085번)
  - [1086번](#1086번)
  - [1087번](#1087번)
  - [1088번](#1088번)
  - [1089번](#1089번)
  - [1090번](#1090번)
  - [1091번](#1091번)
  - [1092번](#1092번)

[[코드업 기초 100제 링크](https://codeup.kr/problemsetsol.php?psid=23){: target="_blank"}]


# 1078번
```python
a = int(input())
sum=0
for i in range(1,a+1):
    if i % 2==0:
        sum+=i
        
print(sum)        
```

# 1079번
```python
a = input().split()
for i in a:
    print(i)
    if i =='q':
        break
```

# 1080번
```python

a = int(input())
sum=0
i=0
while sum<a:
   sum+=i
   i+=1
print(i-1)    
```

# 1081번
```python
a,b = input().split()
a = int(a)
b = int(b)
for i in range(1,a+1):
    for j in range(1,b+1):
        print("%d %d" %(i,j))
```

# 1082번
```python
a = int(input(),16)
for i in range(1,16):
    print("%X*%X=%X"%(a,i,a*i))
```
진수문제는 항상 먼저 10진수로 변환하고 시작하는게 편하다.


# 1083번
```python
a = int(input())
for i in range(1,a+1):
    if i%3==0:
        print('X',end=" ")
        continue
    print(i,end=" ")
```

# 1084번
```python
cnt=0
a,b,c = map(int,input().split())
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            cnt+=1
print(cnt)
```

# 1085번
```python
a,b,c,d = map(float,input().split())
sum = a*b*c*d/8/1024/1024
print("%.1f MB"%sum)
```

# 1086번
```python
a,b,c = map(float,input().split())
sum = a*b*c/8/1024/1024
print("%.2f MB"%sum)
```

# 1087번
```python
a = int(input())
sum =0
i=0
while sum<a:
    i+=1
    sum+=i

print(sum)    
```

# 1088번
```python
a = int(input())
for i in range(1,a+1):
    if i%3==0:
        continue
    print(i)
```

# 1089번
```python
a,b,c= map(int,input().split())
print(a+(c-1)*b)
```

# 1090번
```python
a,b,c= map(int,input().split())
print(a*b**(c-1))
```

# 1091번
```python
a,b,c,d= map(int,input().split())
ans = a
for i in range(d-1):
    ans = ans*b+c
print(ans)
```
# 1092번
```python
day =1
a,b,c= map(int,input().split())
while day%a !=0 or day%b !=0 or day%c !=0:
    day+=1
print(day)
```

