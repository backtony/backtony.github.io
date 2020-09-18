---
layout: post
title:  파이썬 자료구조 1장. 알고리즘 기초
subtitle:   파이썬 자료구조 1장. 알고리즘 기초
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 알고리즘이란?](#1-알고리즘이란)
  - [2. 반복하는 알고리즘](#2-반복하는-알고리즘)
  - [3. 파이썬의 변수 알아보기](#3-파이썬의-변수-알아보기)

## 1. 알고리즘이란?
---
어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차  

### 세 정수의 중앙값 구하기
```
def fuc(a,b,c):
    if a>=b:
        if b>=c:
            return b
        elif c>=a:
            return a
        else :
            return c
    elif c>=b:
        return b
    elif c<=a:
        return a
    else:
        return c
   
print(f"중앙값은 {fuc(1,2,3)}")
```
<br>

__삼항 연산자__  
if~else문이 파이썬에서 유일한 삼항 연산자이다. 조건식 a if b else c 에서 b를 평가한 값이 참이면 a를 거짓이면 c를 반환한다.  
```
# 예시
x,y=10,20,
a = x if x>y else y
print(a)
```
<br>

## 2. 반복하는 알고리즘
---
### 1부터 n까지 정수의 합 구하기
```
# while 문
n = int(input("정수 입력: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(f"1부터 {n}까지의 합 : {sum}")

# for문
n = int(input("정수 입력: "))
sum =0
for i in range(1,n+1):
    sum +=i
print(f"1부터 {n}까지의 합 : {sum}")
```
<br>

__cf) range 함수로 이터러블 객체 생성하기__  
range()함수는 이터러블 객체를 생선한다. 이터러블 객체는 반복할 수 있는 객체를 말한다. 파이썬에서 대표적인 이터러블 자료형으로는 list, str, tuple 이 있다.  

### 연속하는 정수의 합을 구하기 위해 값 정렬하기
```
print("a부터 b까지 정수의 합 구하기")
a = int(input("a : "))
b = int(input("b : "))
sum =0
if a>b :
    a,b = b,a

for i in range(a,b+1):
    sum +=i

print(f"a부터 b까지의 합 : {sum}")
```

### 반복 과정에서 조건 판단하기 1
a에서 b까지의 정수 합을 구하는 과정을 출력하면서 구하기  
```
# 방법 1(효율적이지 못한 코딩)
print("a부터 b까지 정수의 합 구하기")
a = int(input("a : "))
b = int(input("b : "))
sum =0
if a>b :
    a,b = b,a

for i in range(a,b+1):
    if i<b:
        print(f"{i} +",end=" ")
    else :
        print(f"{i} =",end=" ")
    sum +=i

print(sum)

# 방법 2
print("a부터 b까지 정수의 합 구하기")
a = int(input("a : "))
b = int(input("b : "))
sum =0
if a>b :
    a,b = b,a

for i in range(a,b):
    print(f"{i} +",end=" ")
    sum +=i
sum +=b
print(f"{b} = {sum}")
```
방법 1에서 a=1, b=10000 이라고 가정하면 for 문에서 10000번 반복되는 동안 9999번은 i<b 가 참이고 마지막 1번만 else문이 실행된다. 이는 너무 비효율적이다. 방법 2는 if문이 없으므로 for문만 돌리면 된다. 따라서 방법 1보다 효율적이다.  

### 반복 과정에서 조건 판단하기 2
홀수인 경우 -, 짝수인 경우 +를 출력하시오.  
```
# 방법 1 (효율적이지 못한 코딩)
n = int(input("몇 개 출력? : "))

for i in range(n):
    if i%2:
        print("-",end="")
    else:
        print("+",end="")

# 방법 2
n = int(input("몇 개 출력? : "))

for _ in range(n//2):
    print("+-",end="")
if n%2:
    print("+")
```
방법 1의 경우, for 루프 횟수만큼 if문을 돌려야하지만 방법 2의 경우 if문은 1번 for문은 n//2번만 돌리면 된다. 따라서 방법 2가 효율적이다.  
__cf) 방법 2에서 for문에 언더스코어(_)를 사용한 이유는 for문에서 range 함수가 for문을 순환하며 반환하는 값(인덱스)을 사용할 필요가 없기 때문이다. 파이썬에서 무시하고 싶은 값은 언더스코어로 표현할 수 있으니 알아두자.__  

### 반복 과정에서 조건 판단하기 3
*를 n개 출력하되 w개마다 줄바꿈하는 프로그램을 작성하시오.  
```
# 방법 1 (효율적이지 못한 코딩)
n = int(input("몇 개 출력? : "))
w = int(input("몇 개 마다 줄바꿈? : "))

for i in range(1,n+1):
    print("*",end='')
    if i%w == 0:
        print()
if n%w:
    print()
  
# 방법 2
n = int(input("몇 개 출력? : "))
w = int(input("몇 개 마다 줄바꿈? : "))

for i in range(n//w):
    print("*"*w)
if n%w:
    print("*"*(n%w))
```
방법 1의 경우 for문 n번 if문은 n+1번 돌리게 되지만 방법 2는 for문 n//w번 if문 1번만 돌리게 되므로 방법 2가 더 효율적이다.  

### 직사각형 넓이로 변의 길이 구하기
변의 길이와 넓이가 모두 정수인 직사각형에서 변의 길이를 구하시오. 예를 들어 직사각형의 넓이가 32이면 변의 길이를 1 * 32 , 2 * 16, 4 * 8 만 출력한다. 2 * 16은 이미 출력했으므로 16 * 2 는 출력하지 않는다.  
```
area = int(input("넓이 : "))

for i in range(1,area//2+1):
    if i*i > area :
        break
    if area % i:
        continue
    else:
        print(f"{i} * {area//i}")
```

###  10 ~ 99 사이의 난수 n개 생성하기(13이 나오면 중단)
```
import random

n = int(input("난수의 갯수: "))

for i in range(n):
    a = random.randint(10,99) 
    if a == 13 :
        print("\n 프로그램 중단")
        break
    print(a,end=" ")
else :
    print("\n 난수 생성 종료")
```
random.randint(a,b) : a이상 b이하의 정수중 무작위 선택  
for else 구문 : for문을 break로 탈출하지 않았을 경우 실행된다. break로 탈출시 실행되지 않는다.  

### 반목문 건너뛰기와 여러 범위 스캔하기
1~12까지 8을 뛰고 출력하기
```
# 방법 1 (효율적이지 못한 코딩)
for i in range(1,12+1):
    if i==8:
        continue
    print(i,end=" ")
  
# 방법 2
for i in list(range(1,8))+ list(range(9,13)):
    print(i,end=" ")
```
방법 2는 if문이 없으므로 더욱 효율적이다. 건너뛰어야 할 부분을 알고 있다면 그 부분을 제외하고 for문을 작성하자.  
<br>

__비교 연산자를 연속으로 사용하는 방법과 드모르간의 법칙__  
드모르간 법칙 : 각 조건을 부정하고 논리곱을 논리합으로, 논리합을 논리곱으로 바꾸고 다시 전체를 부정하면 원래의 조건과 같다.  
```
# 비교 연산자를 연속으로 사용하는 방법
if 10 <= n <= 99  # n>= 10 and n <= 99 와 같다.

# 드모르간 법칙
if not(10 > n or n > 99) # n>= 10 and n <= 99 와 같다.
```

### 직각 이등변 삼각형으로 출력하기
```
# 왼쪽 벽에 붙이기
n = int(input("짧은 변의 길이 : "))

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

# 오른쪽 벽에 붙이기
n = int(input("짧은 변의 길이 : "))

for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
```
<br>

## 3. 파이썬의 변수 알아보기
---
파이썬에서는 데이터, 함수, 클래스, 모듈, 패키지 등을 모두 객체로 취급한다. 객체는 자료형을 가지며 메모리(저장 공간)을 차지한다. 파이썬의 이런 특징 때문에 파이썬의 변수는 값을 갖지 않는다는 특징이 있다.  
예를 들어  x = 17은 x가 17이라는 값을 갖고 있다고 말할 수 없다. 보통 프로그래밍 언어에서 변수란 값을 저장하는 상자와 같다고 비유하는데 파이썬에서는 이 비유가 옳지 않다. 파이썬의 변수와 객체는 다음과 같이 정리할 수 있다.  
+ 변수는 객체를 참조하는 객체에 연결된 이름에 불과하다.
+ 모든 객체는 메모리를 차지하고, 자료형 뿐만아니라 식별 번호를 가진다.
  - 식별 번호는 다른 객체와 구별할 수 있는 객체의 고유 번호를 말한다.

```
n = 17
print(id(n))
print(id(17))
```
같은 값이 출력된다. 즉, 파이썬의 대입 연산자는 변수에 값을 복사하는 것이 아니라 17의 int형 객체를 참조하는 n이라는 이름을 결합한다. 그러므로 17의 식변 번호와 n의 식별 번호가 같다. 정리하면 정수 리터럴 17의 식별 번호와 n의 식별 번호가 같다는 뜻이다.  
__cf) 리터럴이란 값 자체를 의미한다. 즉, 문자 자체에 의해 값이 주어지는 문자열이다. 예를 들어 숫자 리터럴 7은 7의 값을 가지며, 문자 리터럴 characters는 charracters의 값을 가진다.__  
상자라는 표현을 사용해서 정리하면 17이라는 int형 객체 자체가 상자라고 할 수 있다. 파이썬에서 변수는 값을 저장하는 상자가 아니라 단순한 이름에 불과하다. 만약 n의 값을 17이 아닌 다른 값으로 갱신하면 새로운 값을 갖는 객체(상자)가 생성되고, 그 값을 n이 참조하는 것이다. n의 식별 번호 역시 갱신된다.  
```
n=1
def put_id():
  x = 1
  print(f"id(x) = {id(x)}")

print(f"id(n) = {id(n)}")
print(f"id(1) = {id(1)}")
put_id()
```
n은 전역변수이고 x는 지역변수인데 출력값이 모두 같은 것을 볼 수 있다. 즉, n이건 x건 둘 다 1이라는 int형 객체를 그저 참조만 하는 이름에 불과하다는 것을 알 수 있다.  
C언어를 알고 있다면 조금 이상할 수 있다. C언어에서는 함수 내부에 선언한 지역 변수는 함수가 실행될 때 생성되고 종료될 때 소멸한다. 하지만 파이썬에는 이러한 개념이 없다는 것을 알 수 있다. 프로그램에서 1이라는 정수 객체는 put_id() 함수와 무관하게 존재하기 때문이다. 파이썬에서는 함수가 시작하고 종료함에 따라 객체가 생성되거나 소멸하지 않는다.  
<br>

---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__