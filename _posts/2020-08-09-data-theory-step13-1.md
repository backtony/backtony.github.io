---
layout: post
title:  그래프의 탐색(DFS) 깊이 우선 탐색
subtitle: 그래프의 탐색(DFS) 깊이 우선 탐색
categories: data
tags: theory book datastructure graph dfs 그래프
comments: true
# header-img:
---
+ __목차__
  - [1. 그래프의 이해와 종류](#1-그래프의-이해와-종류)
  - [2. 그래프의 ADT](#2-그래프의-adt)
  - [3. 그래프의 탐색(DFS)](#3-그래프의-탐색dfs)

## 1. 그래프의 이해와 종류
---
![그림1](https://backtony.github.io/assets/img/post/data/step13/1.PNG)

각 점들을 정점이라고 하고 이어진 선들을 간선이라고 한다.  

![그림2](https://backtony.github.io/assets/img/post/data/step13/2.PNG)

방향이 없는 무방향 그래프와 방향이 있는 방향 그래프가 있다.  

## 2. 그래프의 ADT
---
+ void GraphInit(UALGraph *pg, int nv)
  - 그래프의 초기화를 진행한다.
  - 두 번째 인자로 정점의 수를 전달한다.
+ void GraphDestroy(UALGraph *pg)
  - 그래프 초기화 과정에서 할당한 리소스를 반환한다.
+ void (UALGraph *pg, int fromV, int toV)
  -  매개변수 fromV와 toV로 전달된 정점을 연결하는 간선을 그래프에 추가한다.
+ void ShowGraphEdgeInfo(UALGraph *pg)
  - 그래프의 간선정보를 출력한다.

__정점의 이름을 선언하는 방법__  
![그림3](https://backtony.github.io/assets/img/post/data/step13/3.PNG)

## 3. 그래프의 탐색(DFS)
---
![그림4](https://backtony.github.io/assets/img/post/data/step13/4.PNG)

+ 한 사람에게만 연락을 한다.
+ 연락할 사람이 없으면, 자신에게 연락한 사람에게 이를 알린다.
+ 처음 연락을 시작한 사람의 위치에서 연락은 끝이 난다.

![그림5](https://backtony.github.io/assets/img/post/data/step13/5.PNG)

정점을 떠나 다른 정점으로 이동할때 이전의 정점을 스택으로 이동시키고 다른 정점으로 떠날 수 없을 때 스택에서 저장된 정보를 꺼내어 역으로 결로를 추적하다 보면 시작 위치로 이동이 가능하다.  

### 구현
__이전에 구현했던 연결 리스트와 스택을 활용한다.__  
<br>

__DLinkedList.h // 연결 리스트__  
```
#ifndef __D_LINKED_LIST_H__
#define __D_LINKED_LIST_H__

#define TRUE	1
#define FALSE	0

typedef int LData;

typedef struct _node
{
	LData data;
	struct _node* next;
} Node;

typedef struct _linkedList
{
	Node* head;
	Node* cur;
	Node* before;
	int numOfData;
	int (*comp)(LData d1, LData d2);
} LinkedList;


typedef LinkedList List;

void ListInit(List* plist);
void LInsert(List* plist, LData data);

int LFirst(List* plist, LData* pdata);
int LNext(List* plist, LData* pdata);

LData LRemove(List* plist);
int LCount(List* plist);

void SetSortRule(List* plist, int (*comp)(LData d1, LData d2));

#endif
```
__DLinkedList.c // 연결 리스트__  
```
#include <stdio.h>
#include <stdlib.h>
#include "DLinkedList.h"

void ListInit(List* plist)
{
	plist->head = (Node*)malloc(sizeof(Node));
	plist->head->next = NULL;
	plist->comp = NULL;
	plist->numOfData = 0;
}

void FInsert(List* plist, LData data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = plist->head->next;
	plist->head->next = newNode;

	(plist->numOfData)++;
}

void SInsert(List* plist, LData data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	Node* pred = plist->head;
	newNode->data = data;

	while (pred->next != NULL &&
		plist->comp(data, pred->next->data) != 0)
	{
		pred = pred->next;
	}

	newNode->next = pred->next;
	pred->next = newNode;

	(plist->numOfData)++;
}


void LInsert(List* plist, LData data)
{
	if (plist->comp == NULL)
		FInsert(plist, data);
	else
		SInsert(plist, data);
}

int LFirst(List* plist, LData* pdata)
{
	if (plist->head->next == NULL)
		return FALSE;

	plist->before = plist->head;
	plist->cur = plist->head->next;

	*pdata = plist->cur->data;
	return TRUE;
}

int LNext(List* plist, LData* pdata)
{
	if (plist->cur->next == NULL)
		return FALSE;

	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	*pdata = plist->cur->data;
	return TRUE;
}

LData LRemove(List* plist)
{
	Node* rpos = plist->cur;
	LData rdata = rpos->data;

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

void SetSortRule(List* plist, int (*comp)(LData d1, LData d2))
{
	plist->comp = comp;
}
```

__ArrayBaseStack.h // 스택__  
```
#ifndef __AB_STACK_H__
#define __AB_STACK_H__

#define TRUE	1
#define FALSE	0
#define STACK_LEN	100

typedef int Data;

typedef struct _arrayStack
{
	Data stackArr[STACK_LEN];
	int topIndex;
} ArrayStack;

typedef ArrayStack Stack;

void StackInit(Stack* pstack);
int SIsEmpty(Stack* pstack);

void SPush(Stack* pstack, Data data);
Data SPop(Stack* pstack);
Data SPeek(Stack* pstack);

#endif
```
__ArrayBaseStack.c // 스택__  
```
#include <stdio.h>
#include <stdlib.h>
#include "ArrayBaseStack.h"

void StackInit(Stack* pstack)
{
	pstack->topIndex = -1;
}

int SIsEmpty(Stack* pstack)
{
	if (pstack->topIndex == -1)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack* pstack, Data data)
{
	pstack->topIndex += 1;
	pstack->stackArr[pstack->topIndex] = data;
}

Data SPop(Stack* pstack)
{
	int rIdx;

	if (SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}

	rIdx = pstack->topIndex;
	pstack->topIndex -= 1;

	return pstack->stackArr[rIdx];
}

Data SPeek(Stack* pstack)
{
	if (SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}

	return pstack->stackArr[pstack->topIndex];
}
```

__ALGraphDFS.h // DFS__  
```
#ifndef __ALGRAPH_DFS_H__
#define __ALGRAPH_DFS_H__
#include "DLinkedList.h"

//정점의 이름들을 상수화
enum {A,B,C,D,E,F,G,H,I,J};

typedef struct __ual
{
	int numV; // 정점의수
	int numE; // 간선의 수
	List * adjList; // 간선 정보
	int* visitInfo; // 방문정보
}ALGraph;


// 그래프의 초기화
void GraphInit(ALGraph* pg, int nv);

// 그래프의 리소스 해제
void GraphDestroy(ALGraph* pg);

// 간선의 추가
void AddEdge(ALGraph* pg, int fromV, int toV);

// 유틸리티 함수: 간선의 정보 출력
void ShowGraphEdgeInfo(ALGraph* pg);

// Depth First Search: 정점의 정보 출력
void DFShowGraphVertex(ALGraph* pg, int startV);


#endif
```
__ALGraphDFS.c // DFS__  
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ALGraphDFS.h"
#include "DLinkedList.h"
#include "ArrayBaseStack.h"

int WhoIsPrecede(int data1, int data2);

// 그래프의 초기화
void GraphInit(ALGraph* pg, int nv)
{
	int i;

	pg->adjList = (List*)malloc(sizeof(List) * nv);
	pg->numV = nv;
	pg->numE = 0;     // 초기의 간선 수는 0개

	for (i = 0; i < nv; i++)
	{
		ListInit(&(pg->adjList[i]));
		SetSortRule(&(pg->adjList[i]), WhoIsPrecede);
    // 그래프와 연관성은 없으나 연결 리스트에서 요수하므로 적당한 함수 대입함
	}

	// 탐색 정보 등록을 위한 공간의 할당 및 초기화
	pg->visitInfo = (int*)malloc(sizeof(int) * pg->numV);
	memset(pg->visitInfo, 0, sizeof(int) * pg->numV);
}

// 그래프의 리소스 해제
void GraphDestroy(ALGraph* pg)
{
	if (pg->adjList != NULL)
		free(pg->adjList);

	if (pg->visitInfo != NULL)
		free(pg->visitInfo);
}

// 간선의 추가
void AddEdge(ALGraph* pg, int fromV, int toV)
{
	LInsert(&(pg->adjList[fromV]), toV);
	LInsert(&(pg->adjList[toV]), fromV);
	pg->numE += 1;
}

// 유틸리티 함수: 간선의 정보 출력
void ShowGraphEdgeInfo(ALGraph* pg)
{
	int i;
	int vx;

	for (i = 0; i < pg->numV; i++)
	{
		printf("%c와 연결된 정점: ", i + 65);

		if (LFirst(&(pg->adjList[i]), &vx))
		{
			printf("%c ", vx + 65);

			while (LNext(&(pg->adjList[i]), &vx))
				printf("%c ", vx + 65);
		}
		printf("\n");
	}
}

int WhoIsPrecede(int data1, int data2)
{
	if (data1 < data2)
		return 0;
	else
		return 1;
}


int VisitVertex(ALGraph* pg, int visitV)
{
	if (pg->visitInfo[visitV] == 0)
	{
		pg->visitInfo[visitV] = 1;
		printf("%c ", visitV + 65);     // 방문 정점 출력
		return TRUE;
	}

	return FALSE;
}

// Depth First Search: 정점의 정보 출력
void DFShowGraphVertex(ALGraph* pg, int startV)
{
	Stack stack;
	int visitV = startV;
	int nextV;

	StackInit(&stack);

	VisitVertex(pg, visitV);    // 시작 정점 방문

	while (LFirst(&(pg->adjList[visitV]), &nextV)==TRUE)
	{
		int visitFlag = FALSE;
     // 이동이 불가능한 경우를 걸러내기 위한 변수

		if (VisitVertex(pg, nextV) == TRUE)
		{
			SPush(&stack, visitV); // 전지점 스택으로 이동
			visitV = nextV;	// 현재 지점 바꾸기
			visitFlag = TRUE;	// 이동 가능
		}
		else
		{
			while (LNext(&(pg->adjList[visitV]), &nextV)==TRUE)
			{
				if (VisitVertex(pg, nextV) == TRUE)
				{
					SPush(&stack, visitV);
					visitV = nextV;
					visitFlag = TRUE;
					break;
				}
			}
		}
		if (visitFlag == FALSE) // 이동이 불가능 할때
		{
			if (SIsEmpty(&stack) == TRUE)
				break;		
			else
				visitV = SPop(&stack);
		}
	}
	// 탐색 정보 초기화
	memset(pg->visitInfo, 0, sizeof(int) * pg->numV);
}
```

__BFSMain.c // 활용__  
```
#include <stdio.h>
#include "ALGraphDFS.h"

int main(void)
{
	ALGraph graph;
	GraphInit(&graph, 7);      // A, B, C, D, E, F, G의 정점 생성

	AddEdge(&graph, A, B);
	AddEdge(&graph, A, D);
	AddEdge(&graph, B, C);
	AddEdge(&graph, D, C);
	AddEdge(&graph, D, E);
	AddEdge(&graph, E, F);
	AddEdge(&graph, E, G);

	ShowGraphEdgeInfo(&graph);

	DFShowGraphVertex(&graph, A); printf("\n");
	DFShowGraphVertex(&graph, C); printf("\n");
	DFShowGraphVertex(&graph, E); printf("\n");
	DFShowGraphVertex(&graph, G); printf("\n");

	GraphDestroy(&graph);
	return 0;
}
```


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__