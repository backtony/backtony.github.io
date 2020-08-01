---
layout: post
title:  스택(Stack)  
subtitle: 스택(Stack)
categories: data
tags: theory book datastructure stack 스택
comments: true
# header-img:
---
+ __목차__
  - [1. 스택의 ADT 정의](#1-스택의-adt-정의)
  - [2. 스택의 배열 기반 구현](#2-스택의-배열-기반-구현)
  - [3. 스택의 연결 리스트 기반 구현](#3-스택의-연결-리스트-기반-구현)

## 1. 스택의 ADT 정의
---
+ void StackInit(Stack* pstack);
    - 스택의 초기화를 진행한다.
    - 스택 생성 후 제일 먼저 호출되어야 하는 함수이다.
+ int SIsEmpty(Stack* pstack);
    - 스택이 빈경우 TRUE(1), 아닐 경우 FALSE(0)을 반환한다.
+ void SPush(Stack* pstack, Data data);
    - 스택에 데이터를 저장한다. 매개변수 data로 전달된 값을 저장한다.
+ Data SPop(Stack* pstack);
    - 마지막에 저장된 요소를 삭제한다.
    - 삭제된 데이터는 반환한다.
    - 본 함수의 호출을 위해서는 데이터가 하나 이상 존재함이 보장되어야 한다.
+ Data Speek(Stack* pstack);
    - 마지막에 저장된 요소를 반환하되 삭제하지 않는다.
    - 본 함수의 호출을 위해서는 데이터가 하나 이상 존재함이 보장되어야 한다.

## 2. 스택의 배열 기반 구현
---
### 구현 논리
![그림1](https://backtony.github.io/assets/img/post/data/step7/1.PNG)

인덱스가 0인 위치를 스택의 바닥으로 정의해야 배열 길이에 상관없이 바닥 인덱스 값이 동일해집니다.

### ArrayBaseStack.h 
```
#ifndef __ARRAY_BASE_STACK__
#define __ARRAY_BASE_STACK__

#define TRUE 1
#define FALSE 0
#define STACK_LEN 100

typedef int Data;
typedef struct __stack
{
	Data ary[STACK_LEN];
	int topindex;
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

### ArrayBaseStack.c
```
#include <stdio.h>
#include "ArrayBaseStack.h"

void StackInit(Stack* pstack)
{
	pstack->topindex = -1; // 비어있음
}
int SIsEmpty(Stack* pstack)
{
	if (pstack->topindex == -1) return TRUE;
	return FALSE;
}
void SPush(Stack* pstack, Data data)
{
	(pstack->topindex)++;
	pstack->ary[pstack->topindex] = data;
}
Data SPop(Stack* pstack)
{
	Data remv = pstack->topindex;

	if (SIsEmpty(pstack))
	{
		printf("stack memory error");
		exit(-1);
	}
	(pstack->topindex)--;
	return pstack->ary[remv];
}
Data SPeek(Stack* pstack)
{
	if (SIsEmpty(pstack))
	{
		printf("stack memory error");
		exit(-1);
	}
	return pstack->ary[pstack->topindex];
}

```
<br>

### ArrayBaseStackMain.c
```
#include <stdio.h>
#include "ArrayBaseStack.h"

int main(void)
{
	// Stack의 생성 및 초기화 ///////
	Stack stack;
	StackInit(&stack);

	// 데이터 넣기 ///////
	SPush(&stack, 1);  SPush(&stack, 2);
	SPush(&stack, 3);  SPush(&stack, 4);
	SPush(&stack, 5);

	// 데이터 꺼내기 ///////
	while (!SIsEmpty(&stack))
		printf("%d ", SPop(&stack));

	return 0;
}
```
<br>

## 3. 스택의 연결 리스트 기반 구현
---
![그림2](https://backtony.github.io/assets/img/post/data/step7/2.PNG)

메모리 구조만 봐서는 스택인지 구분되지 않는다. 저장된 순서의 역순으로 데이터(노드)를 참조(삭제)하는 연결 리스트가 바로 연결 기반의 스택이다.  
<br>

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

### ListBaseStackMain.c
```
#include <stdio.h>
#include "ListBaseStack.h"

int main(void)
{
	// Stack의 생성 및 초기화 ///////
	Stack stack;
	StackInit(&stack);

	// 데이터 넣기 ///////
	SPush(&stack, 1);  SPush(&stack, 2);
	SPush(&stack, 3);  SPush(&stack, 4);
	SPush(&stack, 5);

	// 데이터 꺼내기 ///////
	while (!SIsEmpty(&stack))
		printf("%d ", SPop(&stack));

	return 0;
}
```


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
