---
layout: post
title:  (Question 4-1) 연결 리스트에 구조체 변수의 주소 값 저장하기
subtitle: (Question 4-1) 연결 리스트에 구조체 변수의 주소 값 저장하기
categories: data
tags: question book datastructure linkedlist 연결리스트
comments: true
# header-img:
---
## 문제
---
[여기](https://backtony.github.io/data/2020/07/30/data-theory-step4/)에서 구현한 연결 리스트를 기반으로 아래 구조체의 주소를 리스트에 연결한다.
```
typedef struct _point
{
    int xpos; // x좌표
    int ypos; // y좌표 
}Point;
```
정렬 기준은 다음과 같다
+ x 좌표의 값을 기준으로 오름차순 정렬이 되게 한다.
+ x 좌표의 값이 같은 경우에는 y 좌표를 대상으로 오름차순 정렬이 되게 한다.

<br>

## 풀이
---
__연결 리스트에 구조체 변수의 주소값 저장할때의 논리__  
1. Main에서 (point)구조체 포인터 선언
2. 그곳에 동적할당을 통해 할당된 (point)구조체 공간 주소값을 대입
3. 함수를 이용해 구조체 멤버 대입
4. 함수를 이용해 리스트에 대입
    - 함수는 (노드)구조체 포인터 선언
    - 동적할당으로 (노드)구조체 공간 주소값 대입
    - (노드)구조체의 멤버로 (point)구조체 포인터가 존재함
    - 그곳에 함수 인자로 받은 (point)구조체 포인터가 가리키는 주소를 대입

__cf) 포인터를 사용한 이유__  
 포인터를 안쓰면 계속 여러 변수명을 만들어야 합니다. 포인터를 쓰면 공간할당하고 주소값 다른 곳에 넘기면 다시 또 사용이 가능하기 때문에 한 개만 선언해도 돌려쓰기가 가능해집니다. 따라서 노드 구조체 포인터, point 구조체 포인터를 사용한 것입니다.  

### DLinkedList.h // 일반적인 연결 리스트 헤더
```
#ifndef __D_LINKED_LIST_H__
#define __D_LINKED_LIST_H__

#include "Point.h" // typedef에서 point구조체 사용하므로

#define TRUE	1
#define FALSE	0

typedef Point * LData; // 리스트에 구조체 주소를 대입하기 때문에

typedef struct _node
{
	LData data;
	struct _node * next;
} Node;

typedef struct _linkedList
{
	Node * head;
	Node * cur;
	Node * before;
	int numOfData;
	int (*comp)(LData d1, LData d2);
} LinkedList;

typedef LinkedList List;

void ListInit(List * plist);
void LInsert(List * plist, LData data);

int LFirst(List * plist, LData * pdata);
int LNext(List * plist, LData * pdata);

LData LRemove(List * plist);
int LCount(List * plist);

void SetSortRule(List * plist, int (*comp)(LData d1, LData d2));

#endif
```
<br>

### DLinkedList.c // 일반적인 연결 리스트 함수 소스 파일
```
#include <stdio.h>
#include <stdlib.h>
#include "DLinkedList.h"

void ListInit(List * plist)
{
	plist->head = (Node*)malloc(sizeof(Node));
	plist->head->next = NULL;
	plist->comp = NULL;
	plist->numOfData = 0;
}

void FInsert(List * plist, LData data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = plist->head->next;
    // 첫 노드에 경우도 이렇게 하나? 혼동될 수 있다.
	// 첫 노드의 경우 head->next는 NULL을 가리키므로 가능하다.
    
	plist->head->next = newNode;

	(plist->numOfData)++;
}

void SInsert(List * plist, LData data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	Node * pred = plist->head;
	newNode->data = data;

	while(pred->next != NULL &&
		plist->comp(data, pred->next->data) != 0)
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
		FInsert(plist, data);
	else
		SInsert(plist, data);
}

int LFirst(List * plist, LData * pdata)
{
	if(plist->head->next == NULL)
		return FALSE;

	plist->before = plist->head;
	plist->cur = plist->head->next;

	*pdata = plist->cur->data;
	return TRUE;
}

int LNext(List * plist, LData * pdata)
{
	if(plist->cur->next == NULL)
		return FALSE;

	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	*pdata = plist->cur->data;
	return TRUE;
}

LData LRemove(List * plist)
{
	Node * rpos = plist->cur;
	LData rdata = rpos->data;

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

void SetSortRule(List * plist, int (*comp)(LData d1, LData d2))
{
	plist->comp = comp;
}
```
<br>

---
__여기부터 일반 연결 리스트에 추가적으로 코딩해야 하는 내용__

### point.h // point 구조체 헤더
```
#ifndef __POINT_H__
#define __POINT_H__

typedef struct _point
{
	int xpos;
	int ypos;
} Point;

// Point 변수의 xpos, ypos 값 설정
void SetPointPos(Point * ppos, int xpos, int ypos);

// Point 변수의 xpos, ypos 정보 출력 
void ShowPointPos(Point * ppos);

// 두 Point 변수의 비교
int PointComp(Point * pos1, Point * pos2); 

#endif
```
<br>

### point.c // 함수 소스 파일
```
#include <stdio.h>
#include "Point.h"

void SetPointPos(Point * ppos, int xpos, int ypos)
{
	ppos->xpos = xpos;
	ppos->ypos = ypos;
}

void ShowPointPos(Point * ppos)
{
	printf("[%d, %d] \n", ppos->xpos, ppos->ypos);
}

int PointComp(Point * pos1, Point * pos2)
{
	if(pos1->xpos == pos2->xpos && pos1->ypos == pos2->ypos)
		return 0;
	else if(pos1->xpos == pos2->xpos)
		return 1;
	else if(pos1->ypos == pos2->ypos)
		return 2;
	else
		return -1;
}
```
<br>

### PointListSortMain.c // 구현된 자료구조 활용
```
#include <stdio.h>
#include <stdlib.h>
#include "DLinkedList.h"
#include "Point.h"

int WhoIsPrecede(Point * d1, Point * d2) // 정렬함수 선언
{
	if(d1->xpos < d2->xpos)
	{
		return 0;
	}
	else if(d1->xpos == d2->xpos)
	{
		if(d1->ypos < d2->ypos)
			return 0;
		else
			return 1;
	}
	else
		return 1;
}


int main(void)
{
	List list;
	Point comp;     // 해당 좌표 삭제를 위해 선언
	Point * pPoint; // 연결 리스트에 구조체 주소값을 넣기 위해서 
	ListInit(&list);

	SetSortRule(&list, WhoIsPrecede);     // 정렬기준을 등록!

	pPoint = (Point*)malloc(sizeof(Point));
	SetPointPos(pPoint, 3, 2);
	LInsert(&list, pPoint);

	pPoint = (Point*)malloc(sizeof(Point));
	SetPointPos(pPoint, 3, 1);
	LInsert(&list, pPoint);

	pPoint = (Point*)malloc(sizeof(Point));
	SetPointPos(pPoint, 2, 2);
	LInsert(&list, pPoint);

	pPoint = (Point*)malloc(sizeof(Point));
	SetPointPos(pPoint, 2, 1);
	LInsert(&list, pPoint);

	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &pPoint))
	{
		ShowPointPos(pPoint);
		
		while(LNext(&list, &pPoint))
			ShowPointPos(pPoint);
	}
	printf("\n");

	// xpos가 2인 모든 데이터 삭제  ////////
	comp.xpos = 2;
	comp.ypos = 0;

	if(LFirst(&list, &pPoint))
	{
		if(PointComp(pPoint, &comp) == 1)
		{
			pPoint = LRemove(&list);
            // 리스트 안에 저장된 구조체 주소값만 삭제
            // 그 공간은 존재하고 있으므로 메모리 반환
			free(pPoint);
		}
		
		while(LNext(&list, &pPoint))
		{
			if(PointComp(pPoint, &comp) == 1)
			{
				pPoint = LRemove(&list);
				free(pPoint);
			}
		}
	}

	// 삭제 후 저장된 데이터 출력 ////////
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &pPoint))
	{
		ShowPointPos(pPoint);
		
		while(LNext(&list, &pPoint))
			ShowPointPos(pPoint);
	}
	printf("\n");

	return 0;
}
```
---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
