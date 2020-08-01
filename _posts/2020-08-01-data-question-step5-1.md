---
layout: post
title:  (Question 5-1) 원형 연결 리스트의 활용
subtitle: (Question 5-1) 원형 연결 리스트의 활용
categories: data
tags: question book datastructure linkedlist 연결리스트
comments: true
# header-img:
---
## 문제
---
[[클릭](https://backtony.github.io/data/2020/07/30/data-theory-step5/)]에서 구현한 원형 연결 리스트를 기반으로 다음 내용을 모두 담고있는 프로그램을 작성해보자.  
+ 직원정보를 등록할 수 있다. 직원정보는 사번과 이름으로 구성된다. 직원정보를 담을 수 있는 구조체를 정의하고, 이를 기반으로 대략 네 명의 직원정보를 원형 연결 리스트에 저장한다. 네 명의 직원정보는 임의로 결정하기로 하고(사용자로부터 입력받지 않아도 된다.), 직원의 사번은 int형 변수에 담을수 있다고 가정하자. 그리고 원형 연결 리스트에는 구조체 변수의 주소값을 저장하는 것을 원칙으로 하자
+ 직원은 순서대로 돌아가면서 당직을 선다. 당직의 순서는 프로그램에 등록되는 등록 순서를 기준으로 결정된다. 예를 들면 A B C의 순으로 등록시 당직 순서도 A B C A B 이다.
+ 직원의 이름과 하나의 숫자를 이용해서 당직자를 확인한다. 함수를 하나 정의하자. 이 함수는 직원의 이름과 숫자를 인자로 전달받는다. 그러면 전달된 이름의 직원이 당직을 선 후로, 전달된 숫자에 해당하는 만큼의 날이 지나서 당직을 서게 되는 직원의 정보를 반환한다.

<br>

## 풀이
---
### CLinkedList.h // 구현했던 헤더
```
#ifndef __C_LINKED_LIST_H__
#define __C_LINKED_LIST_H__
#include "member.h"

#define TRUE	1
#define FALSE	0

typedef Member* Data;

typedef struct _node
{
	Data data;
	struct _node* next;
} Node;

typedef struct _CLL
{
	Node* tail;
	Node* cur;
	Node* before;
	int numOfData;
} CList;


typedef CList List;

void ListInit(List* plist);
void LInsert(List* plist, Data data);
void LInsertFront(List* plist, Data data);

int LFirst(List* plist, Data* pdata);
int LNext(List* plist, Data* pdata);
Data LRemove(List* plist);
int LCount(List* plist);

#endif
```
<br>

### CLinkedList.c 구현했던 헤더 함수 소스파일
```
#include <stdio.h>
#include <stdlib.h>
#include "CLinkedList.h"


void ListInit(List* plist)
{
	plist->tail = NULL;
	plist->cur = NULL;
	plist->before = NULL;
	plist->numOfData = 0;
}

void LInsertFront(List* plist, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if (plist->tail == NULL)
	{
		plist->tail = newNode;
		newNode->next = newNode;
	}
	else
	{
		newNode->next = plist->tail->next;
		plist->tail->next = newNode;
	}

	(plist->numOfData)++;
}

void LInsert(List* plist, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if (plist->tail == NULL)
	{
		plist->tail = newNode;
		newNode->next = newNode;
	}
	else
	{
		newNode->next = plist->tail->next;
		plist->tail->next = newNode;
		plist->tail = newNode;
	}

	(plist->numOfData)++;
}

int LFirst(List* plist, Data* pdata)
{
	if (plist->tail == NULL)    // 저장된 노드가 없다면
		return FALSE;

	plist->before = plist->tail;
	plist->cur = plist->tail->next;

	*pdata = plist->cur->data;
	return TRUE;
}

int LNext(List* plist, Data* pdata)
{
	if (plist->tail == NULL)    // 저장된 노드가 없다면
		return FALSE;

	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	*pdata = plist->cur->data;
	return TRUE;
}

Data LRemove(List* plist)
{
	Node* rpos = plist->cur;
	Data rdata = rpos->data;

	if (rpos == plist->tail)    // 삭제 대상을 tail이 가리킨다면
	{
		if (plist->tail == plist->tail->next)    // 그리고 마지막 남은 노드라면
			plist->tail = NULL;
		else
			plist->tail = plist->before;
	}

	plist->before->next = plist->cur->next;
	plist->cur = plist->before;

	free(rpos);
	(plist->numOfData)--;
	return rdata;
}

int LCount(List* plist)
{
	return plist->numOfData;
}
```
<br>

### member.h // 새로운 헤더
```
#ifndef __C__LINKED__MEMBER__
#define __C__LINKED__MEMBER__

// 직원 정보 저장할 구조체
typedef struct member
{
	int num;
	char name[30];
}Member;

#endif
```
<br>

### CLinkedListMain.c 자료구조 활용 구현 
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "CLinkedList.h"
#include "member.h"


Data whosnext(List* plist, char* name, int day);
void show(Data plist);

int main(void)
{
	List list;
	Member* pp;
	
	ListInit(&list);

	pp = (Member*)malloc(sizeof(Member));
	strcpy(pp->name, "이순신");
	pp->num = 111;
	LInsert(&list, pp);

	pp = (Member*)malloc(sizeof(Member));
	strcpy(pp->name, "유관순");
	pp->num = 222;
	LInsert(&list, pp);

	pp = (Member*)malloc(sizeof(Member));
	strcpy(pp->name, "장보고");
	pp->num =333;
	LInsert(&list, pp);

	pp = (Member*)malloc(sizeof(Member));
	strcpy(pp->name, "윤봉길");
	pp->num = 444;
	LInsert(&list, pp);

	pp = whosnext(&list, "이순신", 3);
	show(pp);

	pp = whosnext(&list, "윤봉길", 15);
	show(pp);

}
Data whosnext(List* plist, char* name, int day)
{
	Member* aa; 
	int i;
	int num = LCount(plist);
	if (LFirst(plist, &aa))
	{
		if (strcmp(aa->name, name) != 0)
		{
			for (i = 0; i < num - 1; i++)
			{
				LNext(plist, &aa);
				if (strcmp(aa->name, name) == 0) break;
			}
			if (i == num - 1) return FALSE;
            // = 으로 했다가 한참 찾음.. ==..
		}
	}

	for (i = 0; i < day; i++)
	{
		LNext(plist, &aa);
	}
	return aa;

}
void show(Data plist)
{
	printf("%s %d \n", plist->name, plist->num);
}
```
---


__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
