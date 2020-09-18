---
layout: post
title:  파이썬 파트 5-2. 함수 고급
subtitle:   파이썬 파트 5-1. 함수 고급
categories: python
tags: basics book python 
comments: true
# header-img:
---
+ __목차__
  - [1. 튜플](#1-튜플)
  - [2. filter함수와 map함수](#2-filter함수와-map)
  - [3. 람다](#3-람다)
  - [4. 파일 처리](#4-파일-처리)
  - [5. 제너레이터](#5-제너레이터)


## 1. 튜플
---
+ 튜플은 리스트와 비슷한 자료형이다.
+ 리스트와 다른 점은 한번 결정된 요소를 바꿀 수 없다는 것이다.   
+ 딕셔너리의 키로 사용할 수 있다.
+ 리스트와 달리 () 으로 선언하지만 생략할 수 있다.
+ 요소를 하나만 가질 수 있다.
+ 추가 변수 없이 스왑이 가능하다.
+ 함수에 리턴값으로 사용시 여러 값을 리턴이 가능하다.

```
기본 형태
(데이터, 데이터, 데이터, ...)

# 예시
tuple_test = (10,20,30)
print(tuple_test[0]) # 10

# 요소 하나만 가지는 튜플
(273) # 괄호는 숫자를 그냥 감싼것으로 생략
(273, ) # 쉼표를 넣어주고 선언시 요소를 하나만 가짐

# 괄호 없이 사용 가능
tuple_test = 10,20,30
print(tuple_test) # (10,20,30)

a,b,c = 10,20,30 # 이것도 튜플
print(a) # 10
```
__리스트와 튜플의 특이한 사용__  
변수를 선언하고 할당할 수 있다. 
```
[a,b] = [10,20]
(c,d) = (10,20)
print(a) # 10
print(d) # 20
```
__swap이 가능한 튜플__  
추가적 변수 없이 swap이 가능하다.
```
a,b = 10,20
print(a,b) # 10 20

a,b = b,a
print(a,b) # 20 10
```
__여러개 값 리턴__  
```
def test() :
  return 10,20

a,b = test()
print(a,b) # 10 20
```
__튜플을 리턴하는 함수(for, divmod)__  
```
for i, value in enumerate([1,2,3,4,5]): # i, value는 튜플

# 몫과 나머지를 반환하는 divmod() 함수
a,b = 97,40

x,y = divmod(a,b)
print(x,y) # 2 17
```
<br>

## 2. filter함수와 map함수
+ map() 함수는 매개인자 리스트의 요소를 매개인자 함수에 넣고 리턴된 값으로 새로운 리스트를 구성한다. 결과값은 제너레이터이다.
+ filter() 함수는 매개인자 리스트의 요소를 매개인자 함수에 넣고 리턴된 값이 True 인 것으로, 새로운 리스트를 구성한다. 결과값은 제너레이터이다.
  - 매개인자로 들어온 함수의 반환값이 불 이어야 한다!

```
기본 형태
map(함수, 리스트)
filter(함수, 리스트)

# map 과 filter 사용 예시
def power(item):
    return item**2

def under_3(item):
    return item < 3

list_a = [1,2,3,4,5]

#제너레이터 
output_a = map(power,list_a)
output_b = filter(under_3,list_a)

#제너레이터이므로 강제 list변환
print(list(output_a))
print(list(output_b))
```
<br>

## 3. 람다
---
프로그래밍 언어에서는 함수라는 '기능'을 매개변수로 전달하는 코드를 많이 사용하는데 이런 코드를 효율적으로 작성할 수 있도록 람다라는 기능을 파이썬에서 제공한다.  
```
기본 형태
lambda 매개변수: 리턴값

# map, fliter 함수 응용 예시
list_a = [1,2,3,4,5]

power = lambda x:x**2
print(list(map(power,list_a)))

# 더욱 간결하게
print(list(map((lambda x:x**2),list_a)))
print(list(filter((lambda x:x<3),list_a)))
```
<br>

## 4. 파일 처리
---
파일은 크게 텍스트 파일과 바이너리 파일로 나뉜다.  

모드|설명
---|---
w|write 모드(새로 쓰기 모드)
a|append 모드(뒤에 이어서 쓰기 모드)
r|read 모드(읽기 모드)

### 파일 열고 쓰고 닫기
```
# 파일 열기
파일 객체 = open(문자열: 파일경로, 문자열: 일기모드)

파일 쓰기
파일 객체.write()

# 파일 닫기
파일 객체.close()

# 예시
file = open("basic.txt","w")
file.write("hello world")
file.close()
```

### with 키워드
파일 처리과정에서 실수로 파일을 열었다가 닫지 않는 경우가 있다. 이런 실수를 방지하지 위해서 with를 사용한다.  
```
기본 형태
with open(문자열: 파일 경로, 문자열: 모드) as 파일 객체:
  문장

# 예시
with open("basic.txt","w") as file: # 파일이 열리고 마지막에 자동으로 닫힘
  file.write("hello world")
```

### 텍스트 읽기
파일에 텍스트를 쓸 때는 write을 썼던 것 처럼 읽을 때는 read를 사용한다.
```
파일 객체.read()

# 예시
with open("basic.txt","r") as file: # 읽기모드
  contents = file.read() # 읽은 내용 저장
print(contents) # 출력
```

### 텍스트 한 줄씩 읽기
텍스트를 사용해 데이터를 구조적으로 표현할 수 있는 방법으로 CSV, XML JSON이 있다. 이 중 CSV(Comma Separated Values)를 알아보자.  
```
# 랜덤한 숫자를 만들기 위해 가져온다.
import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w") as file:
  for i in range(1000):
    # 랜덤값으로 변수 생성
    name = random.choice(hanguls) + random.choice(hanguls)
    weight = random.randrange(40,100)
    height = random.randrange(140,200)
    file.write("{}, {}, {}\n".format(name,weight,height))

with open("info.txt","r") as file:
    # 변수 선언과 잘라서 리스트로 형성
    for line in file:
        (name,weight,height) = line.strip().split(", ")
        # 데이터가 문제 있는지 확인
        if (not name) or (not weight) or (not height):
            continue
        print("\n".join([
            "이름 : {}",
            "몸무게: {}",
            "키 : {}"
        ]).format(name,weight,height))
        print()
```
## 5. 제너레이터
---
제너레이터는 이터레이터를 직접 만들 때 사용하는 코드이다. 함수 내부에 yield 키워드를 사용하면 해당 함수는 제너레이터 함수가 되며, 일반 함수와는 달리 함수를 호출해도 함수 내부의 코드가 실행되지 않는다.  
cf) 반복할 수 있는 것을 '이터러블' 이라고 하고 이 중에서 next() 함수를 적용해 하나하나 꺼낼 수 있는 요소를 '이터레이터'라고 한다.
```
def test():
  print("함수 호출")
  yield "test"

print("A")
test()

print("B")
test()
print(test())

# 출력
A
B
generator object ~~~
```
생각으로는 함수 호출이라는 문자열이 2번 출력되야 하는데 출력되지 않는다. 이유는 제너레이터 함수는 제너레이터를 리턴하기 때문이다. 제너레이터 객체는 next() 함수를 사용해 함수 내부의 코드를 실행해야 한다. 이때 yield 키워드 부분까지만 실행하며, next()함수의 리턴값으로 yield 키워드 뒤에 입력된 값이 반환된다. 만약 next 함수를 호출하고 yield 키워드를 만나지 못하고 함수가 끝나면 StopIteration이라는 예외가 발생한다.  
이처럼 제너레이터 객체는 함수의 코드를 조금씩 실행할 때 사용하는데 이는 메모리의 효율성을 위해서이다.

```
def test():
  print("A pass")
  yield 1
  print("B pass")
  yield 2
  print("C pass")
  yield 3

output = test() # 제너레이터가 output에 들어감
a = next(output) # A pass
# yield 1 까지 실행되어 next는 1을 반환
print(a) # 1
a = next(output) # B pass
print(a) # 2
a = next(output) # C pass
print(a) # 3
```
<br>

__문제 : 1::2::3::4::5::6 출력하기__  
```
numbers = [1,2,3,4,5,6]

# 결과값이 제너레이터이지만 
#리스트로 구성되어 있으므로 변환하지않고 대입 가능
print("::".join(map(str,numbers)))
```
<br>

__문제 : 리스트에서 특정값 추출하기__  
```
numbers = list(range(1,10+1))

print("홀수 추출")
print(list(filter(lambda x: x%2==1,numbers)))

print("3 이상 7 미만 추출")
print(list(filter(lambda x: x>2 and x<7,numbers)))

print("제곱해서 50미만 추출")
print(list(filter(lambda x: x**2<50,numbers)))
```

---
__본 포스팅은 '혼자 공부하는 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__