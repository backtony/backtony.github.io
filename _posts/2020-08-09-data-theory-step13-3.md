---
layout: post
title:  최소 비용 신장 트리
subtitle: 최소 비용 신장 트리
categories: data
tags: theory book datastructure graph 
comments: true
# header-img:
---
+ __목차__
  - [1. 사이클의 이해](#1-사이클-이해와)
  - [2. 크루스칼 알고리즘 1](#2-크루스칼-알고리즘-1)
  - [3. 크루스칼 알고리즘 2](#3-크루스칼-알고리즘-2)
  - [4. 구현](#4-구현)

## 1. 사이클의 이해
---
![그림1](https://backtony.github.io/assets/img/post/data/step13/7.PNG)

+ 단순 경로 : 간선을 중복 포함 하지 않고 이동하는 경로
+ 사이클 : 시작점과 끝점이 같은 단순 경로

### 신장트리
![그림2](https://backtony.github.io/assets/img/post/data/step13/8.PNG)

위 그림을 회전시켜보면 일종의 트리로 볼 수 있다. 어떠한 경로를 구성하더라도 '사이클'을 형성하지 않는 그래프를 신장 트리라고 한다.  
__특징__  
+ 그래프의 모든 정점이 간선에 의해서 하나로 연결되어 있다.
+ 그래프 내에서 사이클을 형성하지 않는다.

### 최소 비용 신장 트리 구성의 예
![그림3](https://backtony.github.io/assets/img/post/data/step13/9.PNG)

<br>

## 2. 크루스칼 알고리즘 1
---
가중치를 기준으로 간선을 정렬한 후에 MST가 될 때까지 간선을 하나씩 선택해 나가는 방식  
![그림4](https://backtony.github.io/assets/img/post/data/step13/10.PNG)

최소 비용 신장트리의 조건인 (간선의 수 +1 = 정점의 수)를 만족하면 이것으로 최소 비용 신장 트리 형성 완료!  
<br>

## 3. 크루스칼 알고리즘 2
---
높은 가중치의 간선을 하나씩 빼는 방식
![그림5](https://backtony.github.io/assets/img/post/data/step13/11.PNG)

![그림6](https://backtony.github.io/assets/img/post/data/step13/12.PNG)

가중치가 8인 간선이 없으면 정점 A와 D가 연결되지 않으므로 삭제하지 않는다. 알고리즘 1과 마찬가지로 최소 비용 신장 트리의 조건인 (간선의 수 + 1 = 정점의 수)를 만족하면 이것으로 최소 비용 신창 트리 형성 완료!

## 4. 구현
---
크루스칼 알고리즘 2를 구현해보자. 이전에 구현한 연결 리스트, 배열 기반 스택, 우선순위 큐, 우선순위 큐의 기반이 되는 힙을 활용하여 구현하자. 우선순위 큐는 가중치를 저장하는데 이용한다.  

### 이전에 구현한 것들
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
__ArrayBaseStack.h // 배열기반 스택__  
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
__ArrayBaseStack.c // 배열기반 스택__  
```
#include <stdio.h>
#include <stdlib.h>
#include "ArrayBaseStack.h"

void StackInit(Stack * pstack)
{
	pstack->topIndex = -1;
}

int SIsEmpty(Stack * pstack)
{
	if(pstack->topIndex == -1)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack * pstack, Data data)
{
	pstack->topIndex += 1;
	pstack->stackArr[pstack->topIndex] = data;
}

Data SPop(Stack * pstack)
{
	int rIdx;

	if(SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}

	rIdx = pstack->topIndex;
	pstack->topIndex -= 1;

	return pstack->stackArr[rIdx];
}

Data SPeek(Stack * pstack)
{
	if(SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}

	return pstack->stackArr[pstack->topIndex];
}
```
__UsefulHeap.h // 힙__  
```
#ifndef __USEFUL_HEAP_H__
#define __USEFUL_HEAP_H__

#include "ALEdge.h"

#define TRUE	1
#define FALSE	0

#define HEAP_LEN	100

// typedef char HData;
typedef Edge HData;

typedef int PriorityComp(HData d1, HData d2);

typedef struct _heap
{
	PriorityComp* comp;
	int numOfData;
	HData heapArr[HEAP_LEN];
} Heap;

/*** Heap 관련 연산들 ****/
void HeapInit(Heap* ph, PriorityComp pc);
int HIsEmpty(Heap* ph);

void HInsert(Heap* ph, HData data);
HData HDelete(Heap* ph);

#endif
```
__UsefulHeap.c // 힙__  
```
#include "UsefulHeap.h"

void HeapInit(Heap* ph, PriorityComp pc)
{
	ph->numOfData = 0;
	ph->comp = pc;
}

int HIsEmpty(Heap* ph)
{
	if (ph->numOfData == 0)
		return TRUE;
	else
		return FALSE;
}

int GetParentIDX(int idx)
{
	return idx / 2;
}

int GetLChildIDX(int idx)
{
	return idx * 2;
}

int GetRChildIDX(int idx)
{
	return GetLChildIDX(idx) + 1;
}

int GetHiPriChildIDX(Heap* ph, int idx)
{
	if (GetLChildIDX(idx) > ph->numOfData)
		return 0;

	else if (GetLChildIDX(idx) == ph->numOfData)
		return GetLChildIDX(idx);

	else
	{
		//	if(ph->heapArr[GetLChildIDX(idx)].pr 
		//				> ph->heapArr[GetRChildIDX(idx)].pr)
		if (ph->comp(ph->heapArr[GetLChildIDX(idx)],
			ph->heapArr[GetRChildIDX(idx)]) < 0)
			return GetRChildIDX(idx);
		else
			return GetLChildIDX(idx);
	}
}

void HInsert(Heap* ph, HData data)
{
	int idx = ph->numOfData + 1;

	while (idx != 1)
	{
		//	if(pr < (ph->heapArr[GetParentIDX(idx)].pr))
		if (ph->comp(data, ph->heapArr[GetParentIDX(idx)]) > 0)
		{
			ph->heapArr[idx] = ph->heapArr[GetParentIDX(idx)];
			idx = GetParentIDX(idx);
		}
		else
		{
			break;
		}
	}

	ph->heapArr[idx] = data;
	ph->numOfData += 1;
}

HData HDelete(Heap* ph)
{
	HData retData = ph->heapArr[1];
	HData lastElem = ph->heapArr[ph->numOfData];

	int parentIdx = 1;
	int childIdx;

	while (childIdx = GetHiPriChildIDX(ph, parentIdx))
	{
		//	if(lastElem.pr <= ph->heapArr[childIdx].pr)
		if (ph->comp(lastElem, ph->heapArr[childIdx]) >= 0)
			break;

		ph->heapArr[parentIdx] = ph->heapArr[childIdx];
		parentIdx = childIdx;
	}

	ph->heapArr[parentIdx] = lastElem;
	ph->numOfData -= 1;
	return retData;
}
```
__PriorityQueue.h // 우선순위 큐__  
```
#ifndef __PRIORITY_QUEUE_H__
#define __PRIORITY_QUEUE_H__

#include "UsefulHeap.h"

typedef Heap PQueue;
typedef HData PQData;

void PQueueInit(PQueue* ppq, PriorityComp pc);
int PQIsEmpty(PQueue* ppq);

void PEnqueue(PQueue* ppq, PQData data);
PQData PDequeue(PQueue* ppq);

#endif
```
__PriorityQueue.c // 우선순위 큐__  
```
#include "PriorityQueue.h"
#include "UsefulHeap.h"

void PQueueInit(PQueue* ppq, PriorityComp pc)
{
	HeapInit(ppq, pc);
}

int PQIsEmpty(PQueue* ppq)
{
	return HIsEmpty(ppq);
}

void PEnqueue(PQueue* ppq, PQData data)
{
	HInsert(ppq, data);
}

PQData PDequeue(PQueue* ppq)
{
	return HDelete(ppq);
}
```
<br>

### 새로 구현해야할 것들
__ALEdge.h // 가중치__  
```
#ifndef __AL_EDGE__
#define __AL_EDGE__

typedef struct _edge
{
	int v1;
	int v2;
	int weight;   // 가중치
} Edge;

#endif
```
__ALGraphKruskal.h__  
```
#ifndef __AL_GRAPH_KRUSKAL__
#define __AL_GRAPH_KRUSKAL__

#include "DLinkedList.h"
#include "PriorityQueue.h"

#include "ALEdge.h"

// 정점의 이름들을 상수화
enum { A, B, C, D, E, F, G, H, I, J };

typedef struct _ual
{
	int numV;
	int numE;
	List* adjList;
	int* visitInfo;
	PQueue pqueue;    // 간선의 가중치 정보 저장
} ALGraph;

// 그래프의 초기화
void GraphInit(ALGraph* pg, int nv);

// 그래프의 리소스 해제
void GraphDestroy(ALGraph* pg);

// 간선의 추가
void AddEdge(ALGraph* pg, int fromV, int toV, int weight);

// 간선의 정보 출력
void ShowGraphEdgeInfo(ALGraph* pg);

// Depth First Search: 정점의 정보 출력
void DFShowGraphVertex(ALGraph* pg, int startV);

// 크루스칼 최소 비용 신장 트리의 구성
void ConKruskalMST(ALGraph* pg);

// 간선의 가중치 정보 출력
void ShowGraphEdgeWeightInfo(ALGraph* pg);

#endif
```
__ALGraphKruskal.c__  
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ALGraphKruskal.h"
#include "DLinkedList.h"
#include "ArrayBaseStack.h"

int WhoIsPrecede(int data1, int data2);
int PQWeightComp(Edge d1, Edge d2);

void GraphInit(ALGraph * pg, int nv)
{
	int i;	

	pg->adjList = (List*)malloc(sizeof(List)*nv);
	pg->numV = nv;
	pg->numE = 0;

	for(i=0; i<nv; i++)
	{
		ListInit(&(pg->adjList[i]));
		SetSortRule(&(pg->adjList[i]), WhoIsPrecede); 
	}

	pg->visitInfo= (int *)malloc(sizeof(int) * pg->numV);
	memset(pg->visitInfo, 0, sizeof(int) * pg->numV);

	// 우선순위 큐의 초기화
	PQueueInit(&(pg->pqueue), PQWeightComp);
}

void GraphDestroy(ALGraph * pg)
{
	if(pg->adjList != NULL)
		free(pg->adjList);

	if(pg->visitInfo != NULL)
		free(pg->visitInfo);
}

void AddEdge(ALGraph * pg, int fromV, int toV, int weight)
{
	Edge edge = {fromV, toV, weight};     // 간선의 정보 생성

	LInsert(&(pg->adjList[fromV]), toV);
	LInsert(&(pg->adjList[toV]), fromV);
	pg->numE += 1;

	// 간선의 정보를 우선순위 큐에 저장
	PEnqueue(&(pg->pqueue), edge);
}

// ConKruskalMST Helper function
void RecoverEdge(ALGraph * pg, int fromV, int toV, int weight)
{
	LInsert(&(pg->adjList[fromV]), toV);
	LInsert(&(pg->adjList[toV]), fromV);
	(pg->numE)++;
}

// 한쪽 방향의 간선 소멸: ConKruskalMST Helper function
void RemoveWayEdge(ALGraph * pg, int fromV, int toV)
{
	int edge;

	if(LFirst(&(pg->adjList[fromV]), &edge))
	{
		if(edge == toV)
		{
			LRemove(&(pg->adjList[fromV]));
			return;
		}

		while(LNext(&(pg->adjList[fromV]), &edge))
		{
			if(edge == toV)
			{
				LRemove(&(pg->adjList[fromV]));
				return;
			}
		}
	}
}

// 간선의 소멸: ConKruskalMST Helper function
void RemoveEdge(ALGraph * pg, int fromV, int toV)
{
	RemoveWayEdge(pg, fromV, toV);
	RemoveWayEdge(pg, toV, fromV);
	(pg->numE)--;
}
 
void ShowGraphEdgeInfo(ALGraph * pg)
{
	int i;
	int vx;

	for(i=0; i<pg->numV; i++)
	{
		printf("%c와 연결된 정점: ", i + 65);
		
		if(LFirst(&(pg->adjList[i]), &vx))
		{
			printf("%c ", vx + 65);
			
			while(LNext(&(pg->adjList[i]), &vx))
				printf("%c ", vx + 65);
		}
		printf("\n");
	}
}

void ShowGraphEdgeWeightInfo(ALGraph * pg)
{
	PQueue copyPQ = pg->pqueue;
	Edge edge;

	while(!PQIsEmpty(&copyPQ))
	{
		edge = PDequeue(&copyPQ);
		printf("(%c-%c), w:%d \n", edge.v1+65, edge.v2+65, edge.weight);
	}
}

int WhoIsPrecede(int data1, int data2)
{
	if(data1 < data2)
		return 0;
	else
		return 1;
}

int PQWeightComp(Edge d1, Edge d2)
{
	return d1.weight - d2.weight;
}

int VisitVertex(ALGraph * pg, int visitV)
{
	if(pg->visitInfo[visitV] == 0)
	{
		pg->visitInfo[visitV] = 1;
	//	printf("%c ", visitV + 65);
		return TRUE;
	}
	
	return FALSE;
}


void DFShowGraphVertex(ALGraph * pg, int startV)
{
	Stack stack;
	int visitV = startV;
	int nextV;

	StackInit(&stack);
	VisitVertex(pg, visitV);
	SPush(&stack, visitV);

	while(LFirst(&(pg->adjList[visitV]), &nextV) == TRUE)
	{
		int visitFlag = FALSE;

		if(VisitVertex(pg, nextV) == TRUE)
		{
			SPush(&stack, visitV);
			visitV = nextV;
			visitFlag = TRUE;
		}
		else
		{
			while(LNext(&(pg->adjList[visitV]), &nextV) == TRUE)
			{
				if(VisitVertex(pg, nextV) == TRUE)
				{
					SPush(&stack, visitV);
					visitV = nextV;
					visitFlag = TRUE;
					break;
				}
			}
		}
		
		if(visitFlag == FALSE)
		{
			if(SIsEmpty(&stack) == TRUE)
				break;
			else
				visitV = SPop(&stack);	
		}
	}

	memset(pg->visitInfo, 0, sizeof(int) * pg->numV);
}

// 두 정점이 연결되어 있다면 TRUE, 그렇지 않다면 FALSE 반환
int IsConnVertex(ALGraph * pg, int v1, int v2)
{
	Stack stack;
	int visitV = v1;
	int nextV;

	StackInit(&stack);
	VisitVertex(pg, visitV);
	SPush(&stack, visitV);

	while(LFirst(&(pg->adjList[visitV]), &nextV) == TRUE)
	{
		int visitFlag = FALSE;

		if(nextV == v2)
		{
			memset(pg->visitInfo, 0, sizeof(int) * pg->numV);
			return TRUE;
		}

		if(VisitVertex(pg, nextV) == TRUE)
		{
			SPush(&stack, visitV);
			visitV = nextV;
			visitFlag = TRUE;
		}
		else
		{
			while(LNext(&(pg->adjList[visitV]), &nextV) == TRUE)
			{
				
				if(nextV == v2)
				{
					memset(pg->visitInfo, 0, sizeof(int) * pg->numV);
					return TRUE;
				}

				if(VisitVertex(pg, nextV) == TRUE)
				{
					SPush(&stack, visitV);
					visitV = nextV;
					visitFlag = TRUE;
					break;
				}
			}
		}
		
		if(visitFlag == FALSE)
		{
			if(SIsEmpty(&stack) == TRUE)
				break;
			else
				visitV = SPop(&stack);	
		}
	}

	memset(pg->visitInfo, 0, sizeof(int) * pg->numV);
	return FALSE;
}


// MST 간선의 수 + 1 == 정점의 수
// 크루스칼 알고리즘 기반 최소 비용 신장 트리의 구성
void ConKruskalMST(ALGraph * pg)
{
	Edge recvEdge[20];    // 복원할 간선의 정보 저장
	Edge edge;
	int eidx = 0;
	int i;

	// MST를 형성할 때까지 아래의 while문을 반복
	while(pg->numE+1 > pg->numV)
	{
		edge = PDequeue(&(pg->pqueue));
		RemoveEdge(pg, edge.v1, edge.v2);

		if(!IsConnVertex(pg, edge.v1, edge.v2))
		{
			RecoverEdge(pg, edge.v1, edge.v2, edge.weight);
			recvEdge[eidx++] = edge;
		}
	}

	// 우선순위 큐에서 삭제된 간선의 정보를 회복
	for(i=0; i<eidx; i++)
		PEnqueue(&(pg->pqueue), recvEdge[i]);

}
```
__KruskalMain.c // 활용__  
```
#include <stdio.h>
#include "ALGraphKruskal.h"

int main(void)
{
	ALGraph graph;
	GraphInit(&graph, 6);      // A, B, C, D, E, F, G의 정점 생성

	AddEdge(&graph, A, B, 9);
	AddEdge(&graph, B, C, 2);
	AddEdge(&graph, A, C, 12);
	AddEdge(&graph, A, D, 8);
	AddEdge(&graph, D, C, 6);
	AddEdge(&graph, A, F, 11);
	AddEdge(&graph, F, D, 4);
	AddEdge(&graph, D, E, 3);
	AddEdge(&graph, E, C, 7);
	AddEdge(&graph, F, E, 13);

	ConKruskalMST(&graph);
	ShowGraphEdgeInfo(&graph);
	ShowGraphEdgeWeightInfo(&graph);

	GraphDestroy(&graph);
	return 0;
}
```


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__