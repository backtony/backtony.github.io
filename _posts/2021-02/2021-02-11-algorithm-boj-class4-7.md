---
layout: post
title: (Python) 백준 1629번 곱셈 - class 4
subtitle:   (Python) 백준 1629번 곱셈 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1629){:target="_blank"}]


## 1629번 곱셈
---
참고로 자연수는 양의 정수이므로 0은 포함되지 않는다.
### 방법 1 내장함수
```python
a, b, c = map(int, input().split())

print(pow(a,b,c))
```
+ pow(밑,지수,나눗셈수) : pow(5,2,3) = 5 * 5 % 3
+ pow(밑,지수) : pow(5,2) = 25

<br>

### 방법 2 분할정복
분할정복은 보통 재귀로 구현한다.  
a**b 처럼 일일이 a를 b번 곱하는 식은 범위가 매우 크기때문에 시간초과가 발생하므로 반복하는 연산을 줄여줘야한다. 예를 들면, 10을 10번 곱한 결과는 10을 5번 곱한 것을 2번 곱한것과 같다. 따라서 이러한 연산이 반복되면 연산횟수가 약 절반으로 줄어든다. 그리고 지수승이 홀수인지 짝수인지 구분해줘야 한다. 또한, 범위가 워낙 크다보니 각각의 연산결과가 매우 크므로 최종적으로 구한 값을 나눠주는게 아니라 분배법칙을 사용해서 중간에 값을 줄여줘야 한다. 나머지에 대한 분배법칙은 다음과 같다.  
(a * b) % c = ((a % c) * (b % c)) %c  
즉, 어떤 수의 나머지연산은 인수 각각에 나머지연산한 것들의 곱을 나머지 연산한 것과 같다. 또한, 어떤 인수는 나머지 연산하고 어떤 인수는 나머지 연산하지 않은 것들의 곱은 나머지 연산한 것하고 곱한 것과 같다.(인수를 나머지 연산해도 되고 안해도 된다는 뜻 -> 결국 결과값은 같음) 
```python
a, b, c = map(int, input().split())

## a^b%c를 반환하는 함수
def solution(a, b):
    # 어떤 수든 재귀를 타면 b==1이 되게 된다.
    if b==1:
        return a%c
    ans = solution(a, b // 2) # 지수승 절반값의 %c한 값 호출
    if b%2==0: # 짝수
        return ans*ans%c
    else: # 홀수
        return ans*ans*(a%c)%c
        # 공식상으로는 ans*ans*(a%c)%c지만 ans*ans*a%c 랑 같다.
        # 나머지 연산 (a*b*c*d)%f 는 a,b,c,d를 각각 f로 나눈 나머지를 곱한뒤 f로 나눈 값이나, 몇개는 냅두고 몇개는 f로 나눈 나머지를 곱한 값을 f로 나눈값이나 같다.

print(solution(a,b))
```
재귀함수를 구현할 때는 항상 어떤 것을 반환한다는 목적을 가지고 그대로 설계하면 된다. 하나하나 타고들어가서 확인하면 꼬여서 더욱 어렵게만 생각하게 된다. __이 문제에서는 '나는 a^b%c의 값을 반환하는 함수를 만들거야' 라고 목적을 가지고 반환값을 a^b%c로 설정해주면 이 함수는 목적에 맞게 설계된 것이라고 생각하고 더이상 깊게 생각하지 않도록 하는 것이 바람직하다.__ 이 문제의 경우는 최적화도 필요하므로 최적화를 위해 (a * b) % c = ((a % c) * (b % c)) %c 공식과 분할정복을 생각한다.
