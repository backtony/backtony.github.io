---
layout: post
title:  스택(Stack) - 계산기 프로그램 구현
subtitle: 스택(Stack) - 계산기 프로그램 구현
categories: data
tags: theory book datastructure stack 스택
comments: true
# header-img:
---
+ __목차__
  - [1. 스택의 ADT 정의](#1-스택의-adt-정의)
  - [2. 스택의 배열 기반 구현](#2-스택의-배열-기반-구현)
  - [3. 스택의 연결 리스트 기반 구현](#3-스택의-연결-리스트-기반-구현)

## 1. 세 가지 수식의 표기법
---
+ 중위 표기법 : 수식 내에 연산의 순서에 대한 정보가 담겨 있지 않다. 그래서 소괄호와 연산자의 우선순위라는 것을 정의하여 이를 기반으로 연산의 순서를 명시한다. ex) 5 + 2 / 7
+ 전위 표기법 : 수식 내에 연산의 순서에 대한 정보가 담겨 있다. 그래서 소괄호가 필요 없고 연산의 우선순위를 결정할 필요도 없다. ex) + 5 / 2 7
+ 후위 표기법 : 전위 표기법과 마찬가지로 수식 내에 연산의 순서에 대한 정보가 담겨 있다. 그래서 소괄호가 필요 없고 연산의 우선순위를 결정할 필요도 없다. ex) 5 2 7 / +

<br>

## 2. 중위 -> 후위
---
### 소괄호 고려하지 않고
소괄호의 연산자의 우선순위를 인식하게 하여 중위 표기법의 수식을 직접 계산하게 프로그래밍 하는 것보다 후위 표기법의 수식을 계산하도록 프로그래밍 하는 것이 더 쉽기에 이에 대한 방법을 알아봅시다.  

![그림1](https://backtony.github.io/assets/img/post/data/step7/3.PNG)

왼쪽 상자 안에 있는 피연산자는 왼쪽부터 차례로 오른쪽 상자로 옮기고 연산자는 쟁반 위로 옮깁니다. 

![그림2](https://backtony.github.io/assets/img/post/data/step7/4.PNG)

이후에는 쟁반에서 연산자를 위에서부터 오른쪽 상자로 옮깁니다.

![그림3](https://backtony.github.io/assets/img/post/data/step7/5.PNG)

__연산자를 쟁반에 옮길때 행동 방식__  
+ 쟁반에 위치한 연산자의 우선 순위가 높다면 쟁반에 위치한 연산자를 꺼내서 오른쪽 상자로 옮기고 새 연산자를 쟁반으로 옮긴다.
+ 쟁반에 위치한 연산자의 우선순위가 낮다면 쟁반에 위치한 연산자의 위에 새 연산자를 쌓는다.
+ 우선순위가 같다면 쟁반에 위치한 연산자를 오른쪽 상자로 옮기고 새 연산자를 쟁반으로 옮긴다.
+ 이미 쟁반에 연산자가 쌓여있다면 위에서부터 차례대로 위의 내용을 참고하여 1:1로 비교한다.

### 소괄호
![그림4](https://backtony.github.io/assets/img/post/data/step7/6.PNG)

소괄호도 쟁반위에 옮기고 `(`는 연산자보다 우선순위를 낮게 잡습니다. 그리고 `)`를 만나면 쟁반에서 `(` 위에 올려져 있는 연산자를 모두 아래 상자로 옮깁니다.

![그림5](https://backtony.github.io/assets/img/post/data/step7/7.PNG)

조금 달리 설명하면 `(`연산자는 쟁반의 또 다른 바닥입니다. 그리고 `)` 연산자는 변환이 되어야 하는 작은 수식의 끝을 의미합니다. 따라서 `)`연산자를 만나면 `(`연산자를 만날 때까지 연산자를 이동 시켜야 합니다.  
<br>

## 3. 프로그램 구현
---
연결 리스트 기반으로 구현한 스택 사용  
### ListBaseStack.h
```
#ifndef __ARRAY_BASE_STACK__
#define __ARRAY_BASE_STACK__

#define TRUE 1
#define FALSE 0

typedef int Data;

typedef struct __node
{
	Data data;
	struct __node* next;
}Node;
typedef struct __stack
{
	Node* head;
}ArrayStack;

typedef ArrayStack Stack;

void StackInit(Stack* pstack);
int SIsEmpty(Stack* pstack);
void SPush(Stack* pstack, Data data);
Data SPop(Stack* pstack);
Data SPeek(Stack* pstack);

#endif
```
<br>

### ListBaseStack.c
```
#include <stdio.h>
#include <stdlib.h>
#include "ListBaseStack.h"

void StackInit(Stack* pstack)
{
	Node* head = NULL;
}
int SIsEmpty(Stack* pstack)
{
	if (pstack->head == NULL) return TRUE;
	return FALSE;
}
void SPush(Stack* pstack, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = pstack->head;
	pstack->head = newNode;
	
}
Data SPop(Stack* pstack)
{
	if (SIsEmpty(pstack))
	{
		printf("stack memory error");
		exit(-1);
	}
	
	Data remv = pstack->head->data; // 반환값 저장
	Node* rnode = pstack->head;     // 삭제노드 주소값 저장
	
	pstack->head = pstack->head->next;
	free(rnode);
	return remv;
	
}
Data SPeek(Stack* pstack)
{
	if (SIsEmpty(pstack))
	{
		printf("stack memory error");
		exit(-1);
	}
	return pstack->head->data;
}

```
<br>

### 