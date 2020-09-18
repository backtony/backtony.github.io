---
layout: post
title:  양방향 리스트 (Linked List) 3  
subtitle: 양방향 리스트 (Linked List) 3
categories: data
tags: theory book datastructure linkedlist 연결리스트
comments: true
# header-img:
---
+ __목차__
  - [1.  연결 리스트의 이해](#1-원형-연결-리스트의-이해)
  - [2. 원형 연결 리스트의 대표적 장점](#2-원형-연결-리스트의-대표적-장점)


## 1. 양방향 연결 리스트의 이해
---
![그림1](https://backtony.github.io/assets/img/post/data/step6/1.PNG)

+ 양방향으로 이동이 가능하다.
+ 삭제함수를 위해 연결 리스트에서 사용했던 before을 사용하지 않아도 된다.

<br>

## 2. 양방향 연결 리스트의 구현
---
연결 리스트의 ADT를 기준으로 다음을 추가, 제거한다.
+ LRemove 함수 제거
+ 왼쪽 노드 참조 LPrevious 함수를 ADT에 추가
+ 새 노드는 머리에 추가

1번의 사진과 같은 모델은 삭제하기 위해서는 경우를 다 나눠야 하기 때문에 복잡합니다. 따라서 삭제함수까지 다룬 모델은 글 맨 아래에 링크를 두겠습니다. 
<br>

### DBLinkedlist.h // 헤더파일
```
#ifndef __DB_LINKED_LIST_H__
#define __DB_LINKED_LIST_H__

#define TRUE	1
#define FALSE	0

typedef int Data;

typedef struct _node
{
	Data data;
	struct _node* next;
	struct _node* prev;  // 이전 노드 참조
} Node;

typedef struct _dbLinkedList
{
	Node* head;
	Node* cur;
	int numOfData;
} DBLinkedList;

typedef DBLinkedList List;

void ListInit(List* plist);
void LInsert(List* plist, Data data);

int LFirst(List* plist, Data* pdata);
int LNext(List* plist, Data* pdata);
int LPrevious(List* plist, Data* pdata);

int LCount(List* plist);

#endif
```
<br>

### DBLinkedList.c // 함수 소스 파일
```
#include <stdio.h>
#include <stdlib.h>
#include "DBLinkedlist.h"

void ListInit(List* plist)
{
	plist->head = NULL;
	plist->numOfData = 0;
}

void LInsert(List* plist, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = plist->head;
  // 처음이면 NULL, 이후면 노드 주소가 들어가도록 
  // 첫 노드 생성만 생각하면 혼동될 수 있으나 두 번째부터 생각하면 쉬움
  
	if (plist->head != NULL) // 첫 노드가 아닐때만  앞 노드 prev연결
		plist->head->prev = newNode;

	newNode->prev = NULL;
	plist->head = newNode; // 머리에 추가이므로 head 변경

	(plist->numOfData)++;
}

int LFirst(List* plist, Data* pdata)
{
	if (plist->head == NULL)
		return FALSE;

	plist->cur = plist->head;
	*pdata = plist->cur->data;

	return TRUE;
}

int LNext(List* plist, Data* pdata)
{
	if (plist->cur->next == NULL)
		return FALSE;

	plist->cur = plist->cur->next;
	*pdata = plist->cur->data;

	return TRUE;
}

int LPrevious(List* plist, Data* pdata)
{
	if (plist->cur->prev == NULL)
		return FALSE;

	plist->cur = plist->cur->prev;
	*pdata = plist->cur->data;

	return TRUE;
}

int LCount(List* plist)
{
	return plist->numOfData;
}
```
<br>

### DBLinkedListMain.c // 구현된 자료구조의 활용
```
#include <stdio.h>
#include "DBLinkedlist.h"

int main(void)
{
	// 양방향 연결 리스트의 생성 및 초기화  ///////
	List list;
	int data;
	ListInit(&list);

	// 8개의 데이터 저장  ///////
	LInsert(&list, 1);  LInsert(&list, 2);
	LInsert(&list, 3);  LInsert(&list, 4);
	LInsert(&list, 5);  LInsert(&list, 6);
	LInsert(&list, 7);  LInsert(&list, 8);

	// 저장된 데이터의 조회  ///////
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
			printf("%d ", data);

		while (LPrevious(&list, &data))
			printf("%d ", data);

		printf("\n\n");
	}

	return 0;
}
```
<br>

더미 노드 기반의 양방향 연결 리스트(삭제 추가) [[클릭](https://backtony.github.io/data/2020/08/01/data-question-step5-2/)]

---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
