---
layout: post
title:  연결 리스트 (Linked List) 1  
subtitle: 연결 리스트 (Linked List) 1
categories: data
tags: theory book datastructure linkedlist 연결리스트
comments: true
# header-img:
---
+ __목차__
  - [1. 더미 노드 연결 리스트](#1-더미-노드-연결-리스트)
  - [2. 더미 노드 연결 리스트 구현](#2-더미-노드-연결-리스트-구현)

## 1. 더미 노드 연결 리스트
---
### 새 노드의 추가 위치에 따른 장점과 단점
+ 새 노드를 연결리스트의 머리에 추가하는 경우
    - 장점 : 포인터 변수 tail이 불필요하다.
    - 단점 : 저장된 순서를 유지하지 않는다.

+ 새 노드를 연결리스트의 꼬리에 추가하는 경우
    - 장점 : 저장된 순서가 유지된다.
    - 단점 : 포인터 변수 tail이 필요하다.

__두 가지 다 가능한 방법이지만 코드가 복잡해질수록tail의 관리가 불편해지므로 머리에 추가하는 것을 원칙으로 하는 것이 좋습니다.__  
<br>

### 더미 노드를 추가하는 이유
더미 노드를 추가하지 않고 코딩을 할 경우 head가 NULL일때와 아닐때로 나눠서 코딩을 해야하지만 더미 노드를 추가할 경우 이 코드를 한 번에 처리할 수 있습니다.  
<br>

## 2. 더미 노드 연결 리스트 구현
---
### 정렬 기능이 추가된 리스트 자료구조의 ADT
```
void ListInit(List *plist);
- 초기화할 리스트의 주소값을 인자로 전달
- 리스트 생성 후 제일 먼저 호출되어야 하는 함수

void LInset(List *plist, LData data);
- 리스트에 데이터 저장, 매개변수에 data 전달된 값을 저장

int LFirst(List *plist, LData *pdata);
- 첫 번째 데이터가 pdata가 가리키는 주소의 메모리에 저장
- 데이터의 참조를 위한 초기화 진행
- 참고 성공시 TRUE(1), 실패시 FALSE(0) 반환

int LNext(List *plist, LData *pdata);
- 참조된 데이터의 다음 데이터가 pdata가 가리키는 메모리에 저장
- 순차적인 참조를 위해서 반복 호출이 가능
- 참조를 새로 시작하려면 먼저 LFirst 함수 호출
- 참고 성공시 TRUE(1), 실패시 FALSE(0) 반환

LData LRemove(List *plist);
- LFirst 또는 LNext 함수의 마지막 반환 데이터를 삭제
- 삭제된 데이터는 반환 => 동적할당의 경우 메모리 반환해줘야하기때문
- 마지막 반환 데이터를 삭제하므로 연이은 반복 호출 허용 X

int LCount(List *plist);
- 리스트 저장 되있는 데이터의 수 반환

/* 배열 리스트에는 없던 ADT */
void SetSortRule(List *plist,int (*comp)(LData d1, LData d2));
- 리스트에 정렬의 기준이 되는 함수를 등록한다.
```
__cf) 왜 참조를 한 번에 안하고 두 번에 나눠서 LNext, LFirst 할까?__  
데이터 참조의 초기화를 위해서 입니다. 만약 하나만 사용하게 되면 참조를 하던 도중 갑자기 처음부터 다시 참조하고 싶을때 난감하게 됩니다. 이러한 이유 때문에 두 개로 나눠서 사용합니다.  
<br>

__cf) LFirst, LNext 함수는 before을 쓰지 않는데 왜 초기화하지?__
LFirst와 LNext 이후에 나올 수 있는 LRemove함수가 호출됐을때의 노드 삭제를 위해서입니다.  
<br>

### DLinkedList.h // 헤더 파일
```
#ifndef __D_LINKED_LIST_H__
#define __D_LINKED_LIST_H__

#define TRUE	1
#define FALSE	0

typedef int LData;

typedef struct _node
{
	LData data;
	struct _node * next; // Node * next 사용 불가!!
} Node;                // 이제야 Node 처리했음!

typedef struct _linkedList
{
	Node * head;    // 더미 노드를 가리키는 멤버
	Node * cur;     // 참조 및 삭제를 돕는 멤버
	Node * before;   // 삭제를 돕는 멤버
	int numOfData;    // 저장 데이터 수 기록 멤버
	int (*comp)(LData d1, LData d2);  // 정렬 기준 등록을 위한 멤버
} LinkedList;


typedef LinkedList List;

void ListInit(List * plist);
void LInsert(List * plist, LData data);

int LFirst(List * plist, LData * pdata);
int LNext(List * plist, LData * pdata);

LData LRemove(List * plist);
int LCount(List * plist);

/* 배열 리스트와 다른 점*/
void SetSortRule(List * plist, int (*comp)(LData d1, LData d2));

#endif
```
<br>

### DLinkedList.c // 함수 구현 소스 파일
```
#include <stdio.h>
#include <stdlib.h>     // malloc, free 사용
#include "DLinkedList.h"

void ListInit(List * plist)
{
	plist->head = (Node*)malloc(sizeof(Node)); // 더미노드 연결
	plist->head->next = NULL;
	plist->comp = NULL;  
	plist->numOfData = 0;
  // cur과 before의 실질적 초기화는 참조에서 이뤄지므로 굳이 하지 않았음.
  // 초기화 해도 상관은 없음.
}
/* SInsert와 FInsert는 LInsert에 사용해야하므로 먼저 선언 */
/* FInser와 LInser는 ADT에 해당하는 기능 안에 구별을 위한 함수로 ADT,헤더에 포함되지 않음. */
void FInsert(List * plist, LData data)
{
	Node * newNode = (Node*)malloc(sizeof(Node)); // 새로운 노드
	newNode->data = data;

	newNode->next = plist->head->next;  // 새로운 노드에 더미노드의 next값(NULL) 연결
	plist->head->next = newNode;        // 더미노드의 next 값에 새로운 노드 연결

	(plist->numOfData)++;               // 갯수 증가
}

void SInsert(List * plist, LData data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
  // 정렬기준에 따른 비교를 위해 새로운 구조체 포인터가 필요함

	Node * pred = plist->head;
  /* 왜 더미노드를 가리키는가?
  => 2개의 대상 사이에 들어갈지 판단하기 위해서는 맨 앞의 노드 주소값을 알고 있다면
  맨 앞 노드의 next값을 통해 다음 노드의 주소도 알 수 있다.*/

	newNode->data = data;

	while(pred->next != NULL && plist->comp(data, pred->next->data) != 0)
 //다음이 끝이 아니고, 비교과정에서 받은 데이터값이 기존 값보다 head에서 더 멀리 떨어져야 할때
	{
		pred = pred->next;
	}

	newNode->next = pred->next;
	pred->next = newNode;

	(plist->numOfData)++;
}

void LInsert(List * plist, LData data)
{
	if(plist->comp == NULL)
		FInsert(plist, data); // 정렬 기준이 없을때
	else
		SInsert(plist, data); // 정렬 기준이 있을때
}

int LFirst(List * plist, LData * pdata)
{
	if(plist->head->next == NULL)
		return FALSE;

	plist->before = plist->head;    //첫 참조 => before에 더미노드 주소값 대입
	plist->cur = plist->head->next;
  // 첫 잠조 => cur에 더미노드 next 값, 실질적인 첫 번째 노드주소값 대입

	*pdata = plist->cur->data;
	return TRUE;
}

int LNext(List * plist, LData * pdata)
{
	if(plist->cur->next == NULL)    // 다음이 없으면 FALSE 반환
		return FALSE;

	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	*pdata = plist->cur->data;
	return TRUE;
}

LData LRemove(List * plist)
{
	Node * rpos = plist->cur;   // 지워야할 공간 주소값을 받을 구조체 포인터
	LData rdata = rpos->data;   // 함수 반환값 저장

	plist->before->next = plist->cur->next;
  // cur next에 연결되있는 노드 주소값을 before next에 연결

	plist->cur = plist->before; // cur을 before 로 이동
  /* before도 뒤로 이동해야하는거 아닌가?
  연결 리스트의 삭제는 참조과정에서 삭제를 진행하므로 참조 과정에서 before는
  cur을 받고 cur은 앞 노드로 이동기 때문에 before은 신경쓰지 않아도 된다. */

	free(rpos);                 // 공간 반환
	(plist->numOfData)--;
	return rdata;               // 삭제 값 반환
}

int LCount(List * plist)
{
	return plist->numOfData;
}

void SetSortRule(List * plist, int (*comp)(LData d1, LData d2))
{
	plist->comp = comp;         // 정렬기준함수 대입
}
```
<br>

### DLinkedListMain.c // 구현된 자료구조의 활용
```
#include <stdio.h>
#include "DLinkedList.h"

int WhoIsPrecede(int d1, int d2) // comp 에 대입할 함수 선언
{
	if(d1 < d2)
		return 0;    // d1이 정렬 순서상 앞선다.
	else
		return 1;    // d2가 정렬 순서상 앞서거나 같다.
}

int main(void)
{
	// List의 생성 및 초기화  ////////////
	List list;
	int data;
	ListInit(&list);

	SetSortRule(&list, WhoIsPrecede);

	// 5개의 데이터 저장  ///////////////
	LInsert(&list, 11);  LInsert(&list, 11);
	LInsert(&list, 22);  LInsert(&list, 22);
	LInsert(&list, 33);

	// 저장된 데이터의 전체 출력 ////////////
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &data)) // 참조 성공시
	{
		printf("%d ", data);

		while(LNext(&list, &data))
			printf("%d ", data);
	}
	printf("\n\n");

	// 숫자 22을 검색하여 모두 삭제 ////////////
	if(LFirst(&list, &data))
	{
		if(data == 22)
			LRemove(&list);

		while(LNext(&list, &data))
		{
			if(data == 22)
				LRemove(&list);
		}
	}

	// 삭제 후 저장된 데이터 전체 출력 ////////////
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &data))
	{
		printf("%d ", data);

		while(LNext(&list, &data))
			printf("%d ", data);
	}
	printf("\n\n");
	return 0;
}
```

---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
