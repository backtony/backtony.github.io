---
layout: post
title:  덱(Deque)
subtitle: 덱(Deque)
categories: data
tags: theory book datastructure deque 덱
comments: true
# header-img:
---
+ __목차__
  - [1. 덱의 이해와 ADT 정의](#1-덱의-이해와-adt-정의)
  - [2. 덱의 구현](#2-덱의-구현)
  

## 1. 덱의 이해와 ADT 정의
---
### 덱의 이해
__"덱은 앞으로도 뒤로도 넣을 수 있고, 앞으로도 뒤로도 뺄 수 있는 자료구조 입니다"__  

![그림1](https://backtony.github.io/assets/img/post/data/step77/6.PNG)

이전에 구현했던 양방향 연결 리스트의 구조에서 tail의 존재 유무만이 차이 입니다.  
<br>

### ADT 정의
+ void DequeInit(Deque* pdeq);
    - 덱의 초기화
    - 덱 생성 후 가장 먼저 호출
+ int DQIsEmpty(Deque pdeq);
    - 덱이 빈 경우 TRUE(1) 아닌 경우 FALSE(0) 반환
+ void DQAddFirst(Deque* pdeq, Data data);
    - 덱의 머리에 data로 전달된 값 저장
+ void DQAddLast(Deque* pdeq, Data data);
    - 덱의 꼬리에 data로 전달된 값 저장
+ Data DQRemoveFirst(Deque* pdeq);
    - 덱의 머리에 위치한 데이터 반환 및 제거
+ Data DQRemoveLast(Deque* pdeq);
    - 덱의 꼬리에 위치한 데이터 반환 및 제거
+ Data DQGetFirst(Deque* pdeq);
    - 댁의 머리에 위치한 데이터 제거하지 않고 반환
+ Data DQGetLast(Deque* pdeq);
    - 댁의 꼬리에 위치한 데이터 제거하지 않고 반환

## 2. 덱의 구현
---
### Deque.h
```
#ifndef __DEQUE_H__
#define __DEQUE_H__

#define TRUE	1
#define FALSE	0

typedef int Data;

typedef struct _node
{
	Data data;
	struct _node * next;
	struct _node * prev;
} Node;

typedef struct _dlDeque
{
	Node * head;
	Node * tail;
} DLDeque;

typedef DLDeque Deque;

void DequeInit(Deque * pdeq);
int DQIsEmpty(Deque * pdeq);

void DQAddFirst(Deque * pdeq, Data data);
void DQAddLast(Deque * pdeq, Data data);

Data DQRemoveFirst(Deque * pdeq);
Data DQRemoveLast(Deque * pdeq);

Data DQGetFirst(Deque * pdeq);
Data DQGetLast(Deque * pdeq);

#endif
```
<br>

### Deque.c
```
#include <stdio.h>
#include <stdlib.h>
#include "Deque.h"

void DequeInit(Deque * pdeq)
{
	pdeq->head = NULL;
	pdeq->tail = NULL;
}

int DQIsEmpty(Deque * pdeq)
{
	if(pdeq->head == NULL)
		return TRUE;
	else
		return FALSE;
}

void DQAddFirst(Deque * pdeq, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

    // 첫 노드여도 pdeq->head 는 NULL이므로 
    // 첫 노드와 이후 노드 구분 없이 가능
	newNode->next = pdeq->head;

	if(DQIsEmpty(pdeq))
		pdeq->tail = newNode;
	else
		pdeq->head->prev = newNode;

	newNode->prev = NULL;
	pdeq->head = newNode;
}

void DQAddLast(Deque * pdeq, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

    // 첫 노드여도 pdeq->head 는 NULL이므로 
    // 첫 노드와 이후 노드 구분 없이 가능
	newNode->prev = pdeq->tail;

	if(DQIsEmpty(pdeq))
		pdeq->head = newNode;		
	else
		pdeq->tail->next = newNode;		

	newNode->next = NULL;
	pdeq->tail = newNode;
}

Data DQRemoveFirst(Deque * pdeq)
{
	Node * rnode = pdeq->head;
	Data rdata = pdeq->head->data;

	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	pdeq->head = pdeq->head->next;
	free(rnode);

    // 삭제한 노드가 마지막 노드였을때
	if(pdeq->head == NULL)
		pdeq->tail = NULL;
	else
		pdeq->head->prev = NULL;

	return rdata;
}

Data DQRemoveLast(Deque * pdeq)
{
	Node * rnode = pdeq->tail;
	Data rdata = pdeq->tail->data;

	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	pdeq->tail = pdeq->tail->prev;
	free(rnode);

    // 삭제한 노드가 마지막 노드였을때
	if(pdeq->tail == NULL)
		pdeq->head = NULL;
	else
		pdeq->tail->next = NULL;

	return rdata;
}

Data DQGetFirst(Deque * pdeq)
{
	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	return pdeq->head->data;
}

Data DQGetLast(Deque * pdeq)
{
	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	return pdeq->tail->data;
}

```
<br>

### DequeMain.c // 구현 활용  
```
#include <stdio.h>
#include "Deque.h"

int main(void)
{
	// Deque의 생성 및 초기화 ///////
	Deque deq;
	DequeInit(&deq);

	// 데이터 넣기 1차 ///////
	DQAddFirst(&deq, 3); 
	DQAddFirst(&deq, 2); 
	DQAddFirst(&deq, 1); 

	DQAddLast(&deq, 4); 
	DQAddLast(&deq, 5); 
	DQAddLast(&deq, 6);

	// 데이터 꺼내기 1차 ///////
	while(!DQIsEmpty(&deq))
		printf("%d ", DQRemoveFirst(&deq));

	printf("\n");

	// 데이터 넣기 2차 ///////
	DQAddFirst(&deq, 3); 
	DQAddFirst(&deq, 2); 
	DQAddFirst(&deq, 1);
	
	DQAddLast(&deq, 4); 
	DQAddLast(&deq, 5); 
	DQAddLast(&deq, 6);

	// 데이터 꺼내기 2차 ///////
	while(!DQIsEmpty(&deq))
		printf("%d ", DQRemoveLast(&deq));

	return 0;
}
```

---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
