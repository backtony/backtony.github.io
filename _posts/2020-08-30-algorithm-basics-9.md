---
layout: post
title:  코드업 기초 100제 파이썬 1093 ~ 1099
subtitle:   코드업 기초 100제 파이썬 1093 ~ 1099
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1093번](#1093번)
  - [1094번](#1094번)
  - [1095번](#1095번)
  - [1096번](#1096번)
  - [1097번](#1097번)
  - [1098번](#1098번)
  - [1099번](#1099번)
 

[[코드업 기초 100제 링크](https://codeup.kr/problemsetsol.php?psid=23){: target="_blank"}]


# 1093번
```python
a = int(input())
b = list(map(int,input().split()))
for i in range(1,24):
    print(b.count(i),end=" ")
```
map의 결과값은 제너레이터이므로 list로 변환시켜준다.  

# 1094번
```python
a = int(input())
b = list(map(int,input().split()))
c =list(reversed(b))
print(*c)
```

# 1095번
```python
a = int(input())
b = list(map(int,input().split()))
print(min(b))
```

# 1096번
```python
# [0] * 19 => 리스트 크기가 19, 요소는 모두 0
# for i in range(19) 위의 해당 리스트가 19개 생성
list_A = [[0] * 19 for i in range(19)]
a = int(input())
for i in range(a):
    x,y = map(int,input().split())
    list_A[x-1][y-1]=1
for i in range(19):
    print(*list_A[i])    
```

# 1097번
```python
a=[None]*19 
for i in range(19):
    a[i]=list(map(int,input().split()))
b = int(input())
for i in range(b):
    x,y = map(int,input().split())
    for j in range(19):
        if a[x-1][j]==0:
            a[x-1][j]=1
        else :
            a[x-1][j]=0
        if a[j][y-1]==0:
            a[j][y-1]=1
        else:
            a[j][y-1]=0
for i in range(19):
    print(*a[i])
```

# 1098번
```python
a,b = map(int,input().split())
k = [[0]*b for i in range(a)]
n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0: # 가로
        for i in range(l):
            k[x-1][y-1]=1
            y+=1
    else :
        for i in range(l):
            k[x-1][y-1]=1
            x+=1
for i in range(a):
    print(*k[i])
```

# 1099번
```python
a = [[0]*10 for i in range(10)]
for i in range(10):
    a[i]= list(map(int,input().split()))

x=y=1
while True:
    if a[x][y]==0:
        a[x][y]=9
        if x==8 and y==8:
            break
        y+=1        
    elif a[x][y]==1:
        y-=1
        x+=1
    else : # 2일때
        a[x][y]=9
        break        
for i in range(10):
    print(*a[i])
```
