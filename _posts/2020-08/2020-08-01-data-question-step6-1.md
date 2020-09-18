---
layout: post
title:  (Question 6-1) 연결 리스트를 이용한 스택의 또 다른 구현
subtitle: (Question 6-1) 연결 리스트를 이용한 스택의 또 다른 구현
categories: data
tags: question book datastructure stack 스택 linkedlist 연결리스트
comments: true
# header-img:
---
## 문제
---
여러분이 필요로하는 것이 존재하지 않을 때 여러분은 다음 두 가지 방법중 하나를 선택해야 한다.
+ 처음부터 새로 만든다.
+ 기존의 것을 활용해서 만든다.

상황에 따라서 좋은 선택은 달라지기 마련이지만 활용할 대상이 있다면 활용하는게 합리적인 판단이다. 따라서 다음 문제를 여러분에게 제시하고자 한다.   
<br>

__Chapter 05[[클릭](http://127.0.0.1:4000/data/2020/07/30/data-theory-step5-1/)]에서 구현한 원형 연결 리스트를 이용해서 스택을 구현해보자__  
<br>

원형 연결 리스트의 구현 결과인 CLinkedList.h와 CLinkedList.c를 변경하지 않고 그저 활용만해서 스택을 구현하는 것이다.  
<br>

## 풀이
---
CLinkedList.h와 CLinkedList.c는 [[클릭](http://127.0.0.1:4000/data/2020/07/30/data-theory-step5-1/)]에서 확인하세요.

### CCLBaseStack.h
```
#ifndef __CLL_STACK_H__
#define __CLL_STACK_H__

#include "CLinkedList.h"

#define TRUE	1
#define FALSE	0

typedef int Data;

typedef struct _listStack
{
	List * plist;
    // 구조체가 아니라 구조체 포인터를 사용한 이유
	// 구조체로 사용시 함수 구현과정에서 참조가 매우 복잡해짐
	// 포인터로 사용시 ->를 이용하여 간단하게 구현가능
} ListStack;


typedef ListStack Stack;

void StackInit(Stack * pstack);
int SIsEmpty(Stack * pstack);

void SPush(Stack * pstack, Data data);
Data SPop(Stack * pstack);
Data SPeek(Stack * pstack);

#endif
```
<br>

### CCLBaseStack.c
```
#include <stdio.h>
#include <stdlib.h>
#include "CLinkedList.h"
#include "CLLBaseStack.h"

void StackInit(Stack * pstack)
{
    // stack에서 list 포인터를 사용했으므로
    // 동적할당으로 주소값 연결
	pstack->plist = (List*)malloc(sizeof(List));
	ListInit(pstack->plist);
}

int SIsEmpty(Stack * pstack)
{
	if(LCount(pstack->plist)==0)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack * pstack, Data data)
{
	LInsertFront(pstack->plist, data);
}

Data SPop(Stack * pstack)
{
	Data data;
    /* 아래 확인 내용이 LFirst안에 포함되어있으므로 불필요
    if (SIsEmpty(pstack))
	{
		printf("stack memory error");
		exit(-1);
	}
    */
	LFirst(pstack->plist, &data);
	LRemove(pstack->plist);
	return data;
}

Data SPeek(Stack * pstack)
{
	Data data;
	LFirst(pstack->plist, &data);
	return data;
}
```
<br>

### CLLBaseStackMain.c // 자료구조 활용하여 구현
```
#include <stdio.h>
#include "CLLBaseStack.h"

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
	while(!SIsEmpty(&stack))
		printf("%d ", SPop(&stack)); 

	return 0;
}
```
<br>

---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__