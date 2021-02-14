---
layout: post
title: (Python) 백준 1918번 후위 표기식 - class 4
subtitle:   (Python) 백준 1918번 후위 표기식 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1918){:target="_blank"}]


## 1918번 후위 표기식
---
스택을 사용했고 연산자의 우선순위를 고려하는 것이 핵심이다. 
1. 입력 문자열에 앞뒤에 ( ) 추가 -> 마지막 괄호가 끝나면 스택에 남아있는 연산자를 처리하기 위함
2. 알파벳이 나오면 정답을 저장할 문자열(ans)에 추가
3. ( 나오면 스택에 추가
4. ) 나오면 스택에서 (가 나올 때까지 빼서 ans에 추가
5. 연산자가 나왔다면
    - 스택에 넣어두었던 연산자보다 우선순위가 높다면 스택에 추가
    - 스택에 넣어두었던 연산자보다 우선순위가 같거나 낮다면 현재 뽑은 연산자가 우선순위가 높아질 때까지 혹은 처음에 넣어둔 (가 마지막으로 남은게 확인될 때까지 스택 pop한 뒤 뽑은 연산자 스택에 추가


```python
letters = input()
ans=""
stack=[]

# 우선순위 지정
priority ={
    '*':1,
    '/':1,
    '+':2,
    '-':2
}

# 입력받은 문자열 전체를 괄호안에 넣으면서
# 마지막 )괄호가 끝나면 스택에 남아있는 연산자를 한 번에 처리하기 위함
for letter in '('+letters+')':
    # 알파벳이면
    if letter.isalpha():
        ans+=letter

    # )면 스택에서 ( 나올때까지 빼기
    elif letter==')':
        while stack:
            temp = stack.pop()
            if temp == '(':
                break
            ans+=temp

    # ( 면 스택에 추가
    elif letter == '(':
        stack.append(letter)

    # 이외의 경우 -> 연산자
    # 전에 스택에 있는 연산자보다 이번에 들어온 연산자의 우선순위가 낮거나 같으면
    # 앞선 스택에 있던 것들보다 이번에 뽑은게 우선순위가 높아질때까지
    # 또는 처음에 넣어둔 (가 나올때까지 다 pop
    else:        
        while stack[-1]!='(' and priority[letter]>=priority[stack[-1]]:
            ans+=stack.pop()
        stack.append(letter)


print(ans)
```