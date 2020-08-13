---
layout: post
title:  파이썬 파트 6. 예외 처리
subtitle:   파이썬 파트 6. 예외 처리
categories: python
tags: basics book python 
comments: true
# header-img:
---
+ __목차__
  - [1. 오류의 종류](#1-오류의-종류)
  - [2. 기본 예외 처리](#2-기본-예외-처리)
  - [3. 예외 고급](#3-예외-고급)

## 1. 오류의 종류
---
+ 프로그램 실행 전에 발생하는 오류
+ 프로그램 실행 중에 발생하는 오류

실행 전에 발생하는 오류를 '구문 오류', 실행 중에 발생하는 오류를 '예외' 또는 '런타임 오류'라고 구분한다.  

### 구문 오류
괄호의 개수, 들여쓰기 문제 등으로 프로그램이 실행되기 전에 발생한다.  
```
print("프로그램이 시작되었다.")
print("따옴표를 빼보자)
```
아무것도 출력되지 않고 SyntaxError가 발생하는데 이는 구문에 문제가 있어 프로그램이 실행조차 되지 않는 오류이다.  

### 예외 또는 런타임 오류
실행 중에 발생하는 오류이다.  
```
print("프로그램이 시작되었다.")
list_a[1]
```
프로그램이 시작되었다.는 출력되지만 list_a is not defined로 예외가 발생한다.  
<br>

## 2. 기본 예외 처리
---
예외를 해결하는 모든 것을 예외 처리라고 한다. 구문 오류는 프로그램이 실행조차 되지 않기 때문에 예외 처리 방법으로 해결할 수 없다. 문법적인 문제가 발생한 코드를 수정해줘야 한다.  
+ 조건문을 사용하는 방법
+ try 구문을 사용하는 방법
    - 단독으로 사용 불가
    - 반드시 except 또는 finally와 함께 사용, 없으면 구문 오류
    - else는 반드시 except 구문 뒤에 사용

### 조건문으로 예외 처리
```
input_a = input("정수입력: ")

if input_a.isdigit():
    print(input_a)

else :
    print("정수가 아님")
```

### try except 구문과 pass 조합
```
기본 형태
try : 
    예외 발생 가능성이 있는 코드
except : 
    예외가 발생했을 때 실행할 코드

# 예시
try : 
    input_a = int(input("정수 입력: "))
    print(input_a)
except :
    print("정수가 아님")

# pass 조합
list_a = ["52","273","32","hello"]
list_n = []

for i in list_a :
    try :
        float(i)
        list_n.append(i)
    except :
        pass # 빈칸으로 두면 오류 발생

print("{}는 리스트 내부 숫자입니다".format(list_n))
```

### try except else 구문
```
기본 형태
try : 
    예외 발생 가능성이 있는 코드
except : 
    예외가 발생했을 때 실행할 코드
else :
    예외가 발생하지 않았을 때 실행할 코드

# 예시
try :
    input_a = int(input("정수입력: "))
except :
    print("정수가 아님")
else :
    print(input_a)
```
많은 언어에서 예외 처리에 else 구문이 없다. 따라서 그냥 try 안에 else 내용을 넣어서 try except 만 사용해도 된다. 하지만 다른 사람이 쓸 수도 있으므로 알고는 있자.  

### finally 구문
예외 처리 구문에서 가장 마지막에 사용할 수 있는 구문이다. 예외 처리가 발생하든 하지 않든 무조건 실행할 때 사용하는 코드이다. 특히 반복문 또는 함수 내부에 있을 때 자주 사용한다.   
```
try : 
    예외 발생 가능성이 있는 코드
except : 
    예외가 발생했을 때 실행할 코드
finally :
    무조건 실행할 코드

# 예시 1
try :
    file = open("info.txt","w")
    return
except :
    print("예외 발생")
finally : 
    file.close()

# file.close() 
# finally를 사용 안하고 함수 밖에서 file.close를 할 경우
함수를 빠져 나갈 때마다 close()를 해야하므로 복잡해진다.

print("file closed? :",file.closed) # 괄호없으면 여부에 따라 불 반환

# 예시 2
print("프로그램 시작")

while True :
    try :
        print("try 구문 시작")
        break
    except :
        print("except 시작")
    finally :
        print("finally 시작")

# break로 루프를 빠져나와도 finally 는 실행된다.
```
<br>

## 3. 예외 고급
---
### 예외 객체
처음 예외 객체를 사용해 보면 '예외의 종류'가 뭔지 몰라 당활할 수 있다. 그럴 때는 '모든 예외의 어머니'라고 불리는 Exception을 사용한다.  
```
기본 형태
try :
    예외가 발생할 가능성이 있는 구문
except 예외의 종류 as 예외 객체를 활용할 변수 이름 : # 변수에 예외가 대입된다고 생각
    예외가 발생했을 때 실행할 구문


try :
    input_a = int(input("정수입력 :"))  # d 입력시
except Exception as exception :
    print(type(exception))  # <class 'ValueError>
    print(exception)        # invalid literal ~~~
```

### 예외 구분하기
```
# 기본 형태
try :
    예외가 발생할 가능성이 있는 구문
except 예외의 종류 A :
    예외A가 발생했을 때 실행할 구문
except 예외의 종류 B :
    예외B가 발생했을 때 실행할 구문

# 예시 : 모든 예외 잡기
list_a = [52,273,32,72,100]

try :
    input_a = int(input("0~4 입력: "))
    print("{}번째 요소: {}".format(input_a,list_a[input_a]))

# 굳이 저장할 변수가 필요 없으므로 as 변수명을 사용 안함.
# except IndexError as exception 이렇게 해도 무관

except IndexError :     
    print("리스트의 인덱스를 벗어났습니다.")
except ValueError :
    print("정수를 입력하세요")
except Exception as exception:
    print("예상치 못한 예외가 발생했습니다.")
    print(type(exception), exception)
```
### raise 구문
프로그램이 강제 종료되는 것을 막기 위해 예외는 꼭 처리해야 한다. 하지만 프로그램을 개발하는 동안에는 '아직 구현하지 않은 부분이니까 확실히 문제가 생기게 만들자', '이 부분은 그냥 넘어가면 나중에 큰 문제가 발생하니까 여기서 강제 종료시키자'라는 경우가 있다. 그래서 raise를 사용한다.    
```
기본 형태
raise 예외 객체

number = int(input("정수 입력: "))
if number > 0 : 
    # 양수일 때: 아직 미구현
    raise NotImplementedError
else :
    # 음수일 때: 마직 미구현
    raise NotImplementedError
```

<br>

__문제 : 구문 오류(Syntax Error)와 예외(Exception)의 차이__  
+ 구문 오류 : 프로그램이 실행되기도 전에 발생하는 오류, 해결하지 않으면 프로그램 자체가 실행되지 않음.
+ 예외 : 프로그램 실행 중에 발생하는 오류, 일단 프로그램이 실행되고 해당 지점에서 오류를 발생

<br>

__문제 : 리스트 요소 존재 여부 try except로 예외 처리하기__  
```
numbers = [52,273,32,103,90,10,275]

print("내부 요소 찾기")
print("{}는 {}위치에 있다".format(52,numbers.index(52)))

number = 10000
try :
    print("{}는 {}위치에 있다".format(number,numbers.index(number)))
except :
    print("리스트 내부에 없는 값")

print("종료")

```
<br>

__문제 : 구문 오류인지 예외인지 구분하기__  
```
output = 10 + "개" # 예외
int("안녕하세요")  # 예외
cursor.close)      # 구문 오류
[1,2,3][5]         # 예외
```
괄호, 들여쓰기 등 작성 구조가 틀린 경우는 구문 오류이고, 구조는 맞으나 자료형 등이 맞지 않는 것은 예외이다.  



---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__