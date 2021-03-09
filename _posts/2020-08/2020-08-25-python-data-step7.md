---
layout: post
title:  파이썬 자료구조 7장. 문자열 검색
subtitle:   파이썬 자료구조 7장. 문자열 검색
categories: python
tags: pdata book python datastructure algorithm
comments: true
# header-img:
---
+ __목차__
  - [1. 문자열 검색이란?](#1-문자열-검색이란)
  - [2. 브루트 포스법](#2-브루트-포스법)
  - [3. 멤버십 연산자와 표준 라이브러리 사용한 문자열 검색](#3-멤버십-연산자와-표준-라이브러리-사용한-문자열-검색)
  - [4. KMP법](#4-kmp법)
  - [5. 보이어 무어법](#5-보이어-무어법)
  - [6. 문자열 검색 알고리즘의 시간 복잡도](#6-문자열-검색-알고리즘의-시간-복잡도)
  
## 1. 문자열 검색이란?
---
문자열 안에 다른 문자열이 포함되어 있는지 검사하고, 만약 포함되어 있다면 어디에 위치하는지 찾아내는 것을 말한다. 검색되는 쪽의 문자열을 텍스트, 찾아내는 문자열을 패턴이라고 한다.  
<br>

## 2. 브루트 포스법
---
```
def bf_match(txt,pat):
    pt=0 # 텍스트 커서
    pp=0 # pat 커서
    while pt != len(txt) and pp != len(pat):
        if txt[pt]==pat[pp]:
            pt+=1
            pp+=1
        else :
            pt=pt-pp+1 
            pp=0
    return pt-pp if pp==len(pat) else -1
```

## 3. 멤버십 연산자와 표준 라이브러리 사용한 문자열 검색
---
### 멤버십 연산자로 구하기
```
a = "abc"

print("b" in a)
print("b" not in a)
```
문자열이 다른 문자열 안에 포함되어 있는지 판단할 수는 있지만 그 위치는 알지 못한다.  

### find, index 계열 함수로 구하기
str 클래스형에 소속된 find, rfind, index, rindex 함수는 문자열을 검색하여 검색한 문자열의 위치를 반환한다. []안의 인수는 생략할 수 있다는 뜻이고 생략시 처음과 끝이 자동으로 입력 된다. 범위는 end-1까지 포함된다.
+ str.find(sub[, start[, end]])
  - 범위 내에 sub가 포함되면 그 가운데 가장 작은 인덱스 반환, 없으면 -1 반환
+ str.rfind(sub[, start [, end]])
  - 범위 내에 sub가 포함되면 그 가운데 가장 큰 인덱스 반환, 없으면 -1
+ str.index(sub[, start [, end]])
  - find와 같은 기능을 수행하나 없으면 ValueError
+ str.rindex(sub[, start [, end]])
  - rfind()와 같은 기능을 수행하나 없으면 ValueError

```
a = "abcdef"

print(a.find("c",0,3))
print(a.rfind("c",0,5))
```

### with 계열 함수로 구하기
어떤 문자열이 다른 문자열의 시작이나 끝에 포함되어 있는지를 판단한다.
+ str.startswith(prefix[, start [, end]])
  - 문자열이 prefix로 시작하면 True, 않으면 False
+ str.endswith(suffix[, start [, end]])
  - 문자열이 suffix로 끝나면 True, 않으면 False


```
a = "abcdef"

print(a.startswith("f"))
print(a.endswith("f"))
```
<br>

## 4. KMP법
---
kmp 알고리즘을 사용했다. kmp 알고리즘은 찾고자 하는 패턴 문자열 p 안에 접두사와 접미사의 중복이 있는 때 대상과 비교하는 도중에 틀린 경우, 대상 문자열의 인덱스를 하나 증가시키고 패턴 문자열의 인덱스를 처음부터 다시 비교하는게 아니라 패턴 문자열의 중복지점 이후부터 검색을 시작하기 때문에 검색 시간을 단축시킬 수 있다. 일일이 비교하면 문자열의 길이가 n(찾을 대상의 전체 길이), m(패턴 길이)이라면 복잡도가 O(mn)이지만, kmp알고리즘을 사용하면 최악의 경우가 O(n)이다. 

```python
# 패턴 문자열의 접두사 접미사 중복 테이블 만들기
def duptable(p):
    n = len(p)
    # 해당 인덱스까지의 문자열에서 중복된 접두,접미사의 개수 저장
    table = [0] * n  

    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
            # 방금전까지 일치했던 접두 접미 개수 j-1
            # j-1개의 문자열에서 접미 접두 중복 개수를 찾아와 j에 대입             
            # p[j]와 p[i]를 다시 비교                              
            # 인덱스는 0시작이라서 개수랑 1차이가 남
            # 따라서 접미접두 중복 개수는 중복 다음의 인덱스,
            # 즉 비교해야할 다음의 인덱스를 가리키게됨

            # 예시로 abadabak 를 생각해보자
            # tb =[0,0,1,0,1,2,3,0]
            # j=3에서 'd'와 'k'가 달라 문제 발생 -> j = tb[2] = 1            
            # 즉, 다른 비교도 건너뛰고 ab ak에서 a는 이미 비교했다고 보고 b와 k를 비교하게 됨              
            

        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table


def kmp(s, p):
    j = 0  # 패턴 인덱스
    cnt = 0 # 일치 개수
    pos = [] # 일치하는 문자열의 시작 위치 담기
    for i in range(len(s)):
        # 비교 중간에 틀린 경우
        # j==0이거나 다음 시작점이 같은 문자를 가리킬때까지 반복
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]

        if s[i] == p[j]:
            j += 1
            if j == len(p):  # 일치 패턴을 찾음
                cnt += 1
                pos.append(i - len(p) + 2) 
                j = table[j - 1]  # j를 끝값으로 했을 때 접두,접미 중복 개수 -> 비교시작위치

    return cnt, pos


s = input()
p = input()
table = duptable(p)

answer, positions = kmp(s, p)
print(answer)
print(*positions)
```
<br>

## 5. 보이어 무어법
---
```
def bm_match(txt: str, pat: str) -> int:
    """보이어 무어법에 의한 문자열 검색"""
    # 아스키 코드에 해당하는 256개 테이블
    skip = [None] * 256  # 건너뛰기 표

    # 건너뛰기 표 만들기  
    # 나쁜 문자 사용법으로 txt의 주목문자(pat에 있는)가 pat에 있는 위치보다
    # 뒤쪽에 있어야한다. 
    for pt in range(256):
        # 배열에 없는 문자일경우 n만큼 건너 뛰도록 해야하므로 길이를 대입
        # 이후에 패턴에 해당하는 문자를 따로 수정
        skip[pt] = len(pat) 
    # skip= [len(pat)]*256 애초에 이렇게 선언해도 돼

    # 틀렸는데 해당 문자가 패턴안에 들어있을 경우
    for pp in range(len(pat)): # 패턴과 일치하는 문자는 따로 처리
        skip[ord(pat[pp])] = len(pat) - 1 - pp    
        # 표의 목적이 문자 비교가 틀렸을 때 사용하게 되는 표라는 것을 기억
        # len-1(총 인덱스) - pp =>해당 문자가 패턴 내에서 뒤에서 몇 번 째인지 판단.
        # 나중에 사용할때 pt에 이 값들 더해줌으로써 
        # 해당 문자를 패턴과 txt에서 위치를 맞출 수 있음       
    
    pt = len(pat)-1 # 처음 비교 시작 위치
    # 검색하기
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        
        # 나쁜 문자 선택법에서 txt의 비교길이가 pat보다 짧아지는 현상이 발생을 이유로
        # pt 에 더하는 값을 선택해야한다.   
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
            else (len(pat)-1) - pp +1 
        # 인덱스 - 현재 위치 +1 -> pt에 더하면 시작 당시 pt의 한 칸 뒤
        # 더하는 값이 비교 시작당시의 pt와 현재 pt의 차이 +1 보다 작으면
        # 즉, 더하고 난 후 pt를 비교 시작당시 pt의 값이하로 만든다면
        # 비교하는 txt 앞의 길이가 pat의 길이보다 짧아지는 문제가 발생한다.
        # 따라서 이 경우 pt를 비교 시작 당시의 한 칸 뒤로 민다. 
              
    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴 문자열

    idx = bm_match(s1, s2)  

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치하고 IDX = {idx}입니다.')
```

__cf) 문자 코드를 다루는 ord() 함수와 chr()함수__  
내장 함수 ord()는 단일한 문자를 전달받아 그 문자의 유니코드 코드 포인트를 정수로 반환한다. 예를 들어 ord('a')는 정수 97을 반환한다.  
또 이 함수의 변환을 거꾸로 수행하는 내장 함수는 chr()이다. 예를 들어 chr(97)은 문자 'a'를 반환한다.  

## 6. 문자열 검색 알고리즘의 시간 복잡도
---
텍스트의 길이 = n, 패턴의 길이 = m 이라고 하고 문자열 검색 알고리즘의 시간 복잡도를 알아보자.  
### 브루트 포스법
시간 복잡도는 O(mn)이지만 일부러 꾸며 낸 패턴이 아니라면 O(n)이 된다고 알려져 있다. 단순한 알고리즘이지만 실제로는 아주 빠르게 동작한다.

### KMP법
시간 복잡도는 최악의 경우 O(n)이다. 다만 처리하기 복잡하고 패턴 안에 반복이 없으면 효율이 좋지 않다. 그러나 검색 과정에서 주목하는 곳을 앞으로 되돌릴 필요가 전혀 없으므로 파일을 차례로 읽어 들이면서 검색할 때 사용하면 좋다.

### 보이어 무어법
시간 복잡도는 최악의 경우에는 O(n)이고 평균 O(n / m)이다.  
<br>

일반적으로 파이썬에서 문자열 검색을 하려면 표준 라이브러리를 사용한다. 만약 표준 라이브러리를 사용하지 않는다면 보이어 무어법이나 상황에 따라서 브루트 포스법을 사용하는 경우가 많다.  




<br>
  
---
__본 포스팅은 '자료구조와 함께 배우는 알고리즘 입문'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
