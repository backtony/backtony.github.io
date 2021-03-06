---
layout: post
title:  원형 리스트 (Linked List) 2  
subtitle: 원형 리스트 (Linked List) 2
categories: data
tags: theory book datastructure linkedlist 연결리스트
comments: true
# header-img:
---
+ __목차__
  - [1. 원형 연결 리스트의 이해](#1-원형-연결-리스트의-이해)
  - [2. 원형 연결 리스트의 대표적 장점](#2-원형-연결-리스트의-대표적-장점)
  - [3. head 대신 tail을 사용하는 이유](#3-head-대신-tail을-사용하는-이유)
  - [4. 원형 연결 리스트의 구현 범위](#4-원형-연결-리스트의-구현-범위)
  - [5. 원형 연결 리스트 구현](#5-원형-연결-리스트의-구현)

## 1. 원형 연결 리스트의 이해
---
![그림1](https://backtony.github.io/assets/img/post/data/step5/1.PNG)

단순 연결리스트의 마지막 노드는 NULL을 가리키지만 원형 연결 리스트의 마지막 노드는 첫 번째 노드를 가리킵니다. 아래에서 구현할 모델은 위 그림과 다르게 head대신 tail을 사용합니다. 이유는 아래에서 설명하겠습니다.  
<br>

## 2. 원형 연결 리스트의 대표적 장점
---
+ 단순 연결 리스트처럼 머리와 꼬리를 가리키는 포인터 변수를 각각 두지 않아도, 하나의 포인터 변수만 있어도 머리 또는 꼬리에 노드를 간단히 추가할 수 있습니다.  

## 3. head 대신 tail을 사용하는 이유
---
원형 연결 리스트의 꼬리 다음에는 당연히 머리입니다. 따라서 꼬리의 주소값을 알고 있으면 꼬리의 next를 이용해서 머리의 주소값도 알 수 있습니다. 따라서 tail을 사용하는게 좋습니다.  
<br>

## 4. 원형 연결 리스트의 구현 범위
---
이전에 구현한 연결 리스트 <[클릭](https://backtony.github.io/data/2020/07/29/data-step4/)>
+ 조회관련 LFirst : 이전에 구현한 연결 리스트와 기능 동일
+ 조회관련 LNext : 원형 연결 리스트를 계속해서 순환하는 형태로 변경
+ 삭제관련 LRmove : 이전에 구현한 연결 리스트와 동일
+ 삽입관련 : 앞과 뒤에 삽입이 가능하도록 두 개의 함수 정의
+ 정렬관련 : 정렬과 관련 내용 전부 제거
+ 이외의 부분 : 이전의 구현한 연결 리스트와 기능 동일
<br>

## 5. 원형 연결 리스트 구현
---
### CLinkedList.h // 헤더파일
```
#ifndef __C_LINKED_LIST_H__
#define __C_LINKED_LIST_H__

#define TRUE	1
#define FALSE	0

typedef int Data;

typedef struct _node
{
	Data data;
	struct _node * next;
} Node;

typedef struct _CLL
{
	Node * tail;    // 꼬리
	Node * cur;     // 현재
	Node * before;  // cur 한 칸 뒤에 노드
	int numOfData;
} CList;


typedef CList List;

void ListInit(List * plist);                // 구조체 멤버 초기화
void LInsert(List * plist, Data data);      // 꼬리에 노드 추가
void LInsertFront(List * plist, Data data); // 앞에 노드 추가

int LFirst(List * plist, Data * pdata);     // 첫 참조
int LNext(List * plist, Data * pdata);      // 이후 참조
Data LRemove(List * plist);                 // 제거
int LCount(List * plist);                   // 갯수

#endif
```
<br>

### CLinkedList.c // 함수 소스 파일
```
#include <stdio.h>
#include <stdlib.h>
#include "CLinkedList.h"

void ListInit(List * plist)
{
	plist->tail = NULL;
	plist->cur = NULL;
	plist->before = NULL;
	plist->numOfData = 0;
}

void LInsertFront(List * plist, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if(plist->tail == NULL)      // 초기화 이후 노드가 아무것도 없음
	{
		plist->tail = newNode;
		newNode->next = newNode; // 자기 자신을 대입 => 순환
	}
	else                         // 노드가 존재
	{
		newNode->next = plist->tail->next;
		plist->tail->next = newNode;
	}

	(plist->numOfData)++;
}

void LInsert(List * plist, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if(plist->tail == NULL)
	{
		plist->tail = newNode;
		newNode->next = newNode;
	}
	else
	{
		newNode->next = plist->tail->next;
		plist->tail->next = newNode;
		plist->tail = newNode; // 꼬리 추가이므로 꼬리 변경
	}

	(plist->numOfData)++;
}

int LFirst(List * plist, Data * pdata)
{
	if(plist->tail == NULL)    // 저장된 노드가 없다면
		return FALSE;

	plist->before = plist->tail;
	plist->cur = plist->tail->next;

	*pdata = plist->cur->data;
	return TRUE;
}

int LNext(List * plist, Data * pdata)
{
	if(plist->tail == NULL)    // 저장된 노드가 없다면
		return FALSE;

	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	*pdata = plist->cur->data;
	return TRUE;
}

Data LRemove(List * plist)
{
	Node * rpos = plist->cur;
	Data rdata = rpos->data;

	if(rpos == plist->tail)    // 삭제 대상을 tail이 가리킨다면
	{
		if(plist->tail == plist->tail->next)    // 그 tail이 마지막 남은 노드라면
			plist->tail = NULL;
		else
			plist->tail = plist->before;        // tail 변경
	}

	plist->before->next = plist->cur->next;
	plist->cur = plist->before;

	free(rpos);
	(plist->numOfData)--;
	return rdata;
}

int LCount(List * plist)
{
	return plist->numOfData;
}
```
<br>

### CLinkedListMain.c // 구현된 자료구조의 활용
```
#include <stdio.h>
#include "CLinkedList.h"

int main(void)
{
	// 원형 연결 리스트의 생성 및 초기화 ///////
	List list;
	int data, i, nodeNum;
	ListInit(&list);

	// 리스트에 5개의 데이터를 저장 ///////
	LInsert(&list, 3);
	LInsert(&list, 4);
	LInsert(&list, 5);
	LInsertFront(&list, 2);
	LInsertFront(&list, 1);

	// 리스트에 저장된 데이터를 연속 3회 출력 ///////
    // 단순 연결 리스트와 다르게 끝이 없어 for을 사용//
	if(LFirst(&list, &data))
	{
		printf("%d ", data);

		for(i=0; i<LCount(&list)*3-1; i++) // 첫째는 바로 위에 썼으므로 -1
		{
			if(LNext(&list, &data))
				printf("%d ", data);
		}
	}
	printf("\n");

	// 2의 배수를 찾아서 모두 삭제 ///////
	nodeNum = LCount(&list);

	if(nodeNum != 0) // 노드가 존재 할때
    // if문이 없었다면 노드가 없는데도 불필요한 계산을 하게 되므로
    // if문으로 노드가 존재하는 경우만 처리하게 함.
	{
		LFirst(&list, &data);
		if(data%2 == 0)
			LRemove(&list);

		for(i=0; i < nodeNum-1; i++)
		{
			LNext(&list, &data);
			if(data%2 == 0)
				LRemove(&list);
		}
	}

	// 전체 데이터 1회 출력 ///////
	if(LFirst(&list, &data))
	{
		printf("%d ", data);

		for(i=0; i<LCount(&list)-1; i++)
		{
			if(LNext(&list, &data))
				printf("%d ", data);
		}
	}
	return 0;
}
```

---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
