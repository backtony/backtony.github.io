---
layout: post
title:  (Question 5-2) 더미 노드 기반의 양방향 연결 리스트의 구현
subtitle: (Question 5-2) 더미 노드 기반의 양방향 연결 리스트의 구현
categories: data
tags: question book datastructure linkedlist 연결리스트
comments: true
# header-img:
---
## 문제
---
![그림1](https://backtony.github.io/assets/img/post/data/question/step5/1.PNG)
사진의 양뱡향 연결 리스트를 구현하시오.

위 그림에서 보이는 연결 리스트의 특징은 다음과 같다.
+ 양방향 연결 리스트이다.
+ 더미 노드가 리스트의 앞과 뒤에 각각 존재한다.
+ 포인터 변수 head와 tail이 있어서 리스트의 앞과 뒤를 각각 가리킨다.
+ 꼬리에 노드를 추가한다.

## 풀이
---
### DBDLinkedList.h 
```
#ifndef __BDB_LINKED_LIST_h__
#define __BDB_LINKED_LIST_h__

#define TRUE 1
#define FALSE 0

typedef int Data;

typedef struct node
{
	Data data;
	struct node* prev;
	struct node* next;
}Node;

typedef struct __list
{
	Node* cur;
	Node* head;
	Node* tail;
	int numOfData;
}DBList;

typedef DBList List;

void ListInit(List* plist);
void LInsert(List* plist, Data data);

int LFirst(List* plist, Data* pdata);
int LNext(List* plist, Data* pdata);

Data LRemove(List* plist);
int LCount(List* plist);


#endif
```
<br>

### DBDLinkedList.c
```
#include <stdio.h>
#include <stdlib.h>
#include "DBDLinkedList.h"

void ListInit(List* plist)
{
	plist->head = (Node*)malloc(sizeof(Node));
	plist->tail = (Node*)malloc(sizeof(Node));

	plist->head->next = plist->tail;
	plist->tail->prev = plist->head;

	plist->head->prev = NULL;
	plist->tail->next = NULL;	
	
	int numOfData = 0;
}
void LInsert(List* plist, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	
	newNode->prev = plist->tail->prev;
	plist->tail->prev->next = newNode;

	newNode->next = plist->tail;
	plist->tail->prev = newNode;
	
	(plist->numOfData)++;
}

int LFirst(List* plist, Data* pdata)
{
    // head와 tail의 사이에 노드가 없을때
	if (plist->head->next == plist->tail) return FALSE;
	plist->cur = plist->head->next;
	*pdata = plist->cur->data;
	return TRUE;
}
int LNext(List* plist, Data* pdata)
{
	if (plist->cur->next == plist->tail) return FALSE;
	plist->cur = plist->cur->next;
	*pdata = plist->cur->data;
	return TRUE;
}

Data LRemove(List* plist)
{
	Node* res;      // 제거노드 주소값 저장
	Data remv;      // 제거노드 데이터값 저장
	res = plist->cur;
	remv = plist->cur->data;
	
	plist->cur->prev->next = plist->cur->next;
	plist->cur->next->prev = plist->cur->prev;

	plist->cur = plist->cur->prev; // cur 위치 재조정
	free(res);
	return remv;
	(plist->numOfData)--;
}
int LCount(List* plist)
{
	return plist->numOfData;
}
```
<br>

### DBDLinkedListMain.c // 자료구조 활용 구현
```
#include <stdio.h>
#include "DBDLinkedList.h"

int main(void)
{
	List list;
	int data;
	ListInit(&list);

	// 8개의 데이터 저장 ///////
	LInsert(&list, 1);  LInsert(&list, 2);
	LInsert(&list, 3);  LInsert(&list, 4);
	LInsert(&list, 5);  LInsert(&list, 6);
	LInsert(&list, 7);  LInsert(&list, 8);

	// 저장된 데이터의 조회 ///////
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
			printf("%d ", data);

		printf("\n");
	}

	// 2의 배수 전부 삭제 ///////
	if (LFirst(&list, &data))
	{
		if (data % 2 == 0)
			LRemove(&list);

		while (LNext(&list, &data))
		{
			if (data % 2 == 0)
				LRemove(&list);
		}
	}

	// 저장된 데이터의 재 조회 ///////
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
			printf("%d ", data);

		printf("\n\n");
	}

	return 0;
}
```
<br>

__head와 tail에 더미 노드 추가의 장점__  
head와 tail이 더미 노드를 가리키고 있기 때문에 삭제할 경우 head, tail의 재조정이 필요 없게 되므로 코딩이 더욱 간단해진다.

---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
