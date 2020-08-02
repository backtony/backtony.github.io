---
layout: post
title:  큐(Queue)
subtitle: 큐(Queue)
categories: data
tags: theory book datastructure queue 큐
comments: true
# header-img:
---
+ __목차__
  - [1. 큐의 이해와 ADT 정의](#1-큐의-이해와-adt-정의)
  - [2. 큐의 배열 기반 구현](#2-큐의-배열-기반-구현)
  - [3. 큐의 연결 리스트 기반 구현](#3-큐의-연결-리스트-기반-구현)

## 1. 큐의 이해와 ADT 정의
---
### 큐의 이해
![그림1](https://backtony.github.io/assets/img/post/data/step77/1.PNG)
큐는 First-in, First-out의 자료구조입니다. 따라서 먼저 들어가면 먼저 나오는 일종의 줄서기에 비유할 수 있습니다.  
<br>

### ADT 정의
+ void QueuInit(Queue *pq);
    - 큐의 초기화
    - 큐 생성 후 제일 먼저 호출
+ int QIsEmpty(Queue *pq);
    - 큐가 빈 경우 TRUE(1), 아닌 경우 FALSE(0)
+ void Enqueue(Queue *pq, Data data)
    - 큐에 data로 전달된 값을 저장
+ Data Dequeue(Queue *pq)
    - 저장순서가 가장 앞선 데이터 삭제
    ` 삭제된 데이터 반환
    ` 호출을 위해서는 데이터가 하나 이상 존재함이 보장되어야함.
+ Data QPeek(Queue *pq);
    - 저장순서가 앞선 데이터를 반환하되 삭제하지 않는다.
    - ` 호출을 위해서는 데이터가 하나 이상 존재함이 보장되어야함.

<br>

## 2. 큐의 배열 기반 구현
---
![그림2](https://backtony.github.io/assets/img/post/data/step77/2.PNG)
cf) F:출구(맨 먼저 들어온) , R:입구(이제 삽입되는)  
배열 기반으로 했을 경우 배열의 끝이 존재합니다. 그런데 enqueue와 dequeue를 실행하다 보니 끝에 도달했는데 결과적으로 앞쪽의 메모리는 비어있는 즉, 낭비되는 현상이 발생합니다. 이를 보완하기 배열의 머리와 끝을 연결한 구조인 원형 큐를 사용합니다.  
[그림3](https://backtony.github.io/assets/img/post/data/step77/3.PNG)
하지만 원형 큐에서도 약간의 문제가 있습니다. 아래 그림과 같이 꽉 채워져 있는 경우와 비어있는 경우 차이를 확인할 수 없다는 점입니다.  
[그림4](https://backtony.github.io/assets/img/post/data/step77/4.PNG)
따라서 이 문제를 해결하기 위해 초기화 직후에 F와 R이 같은 빈 공간을 가리키는 상태를 Empty 상태로 인정하고 F는 항상 빈공간을 가리키게 합니다. 따라서, 저장 공간을 다 채우게 되도 F는 빈공간을 가리키게 되므로 결국 메모리의 하나를 비운 상태가 FULL 상태가 됩니다. 정리하면, F와 R이 같은 곳을 가리킬때 Empty상태가 되고 R의 다음 인덱스값이 F일때가 FULL 상태가 되는 겁니다. 구분이 가능하게 되는 것입니다.
[그림5](https://backtony.github.io/assets/img/post/data/step77/5.PNG)

<br>

### CircularQueue.h
```
#ifndef __CIRCULAR_QUEUE_H__
#define __CIRCULAR_QUEUE_H__

#define TRUE	1
#define FALSE	0
#define LEN 100

typedef int Data;

typedef struct __Queue
{
	int first;
	int rear;
	Data ary[LEN];
} Queueary;


typedef Queueary Queue;

void QueueInit(Queue* pq);
int QIsEmpty(Queue* pq);

void Enqueue(Queue* pq, Data data);
Data Dequeue(Queue* pq);
Data QPeek(Queue* pq);

#endif
```
<br>

### CircularQueue.c
```
#include <stdio.h>
#include"CircularQueue.h"

void QueueInit(Queue* pq)
{
	pq->first = 0;
	pq->rear = 0;
}
int QIsEmpty(Queue* pq)
{
	if (pq->first == pq->rear) return TRUE;
	return FALSE;
}

int Next(int rear)
{
	if (rear == LEN - 1) return 0;
	return rear + 1;
}

void Enqueue(Queue* pq, Data data)
{
	pq->rear = Next(pq->rear);
	if (pq->rear == pq->first)
	{
		printf("no memory\n");
		exit(-1);
	}
	pq->ary[pq->rear] = data;
}
Data Dequeue(Queue* pq)
{
	if (QIsEmpty(&pq))
	{
		printf("Empty\n");
		exit(-1);
	}
	pq->first = Next(pq->first);
	// Dequeue인데 왜 삭제 코드가 없나?
	// 코드를 작성하기 전에 first가 가리키는 공간은
	// 빈 공간으로 인정하고 코드를 작성했다.
	// 따라서 first가 가리키는 공간이라는 의미 자체가
	// 그 공간 안의 값은 존재하지 않는다는 뜻

	return pq->ary[pq->first];
}
Data QPeek(Queue* pq)
{
	if (QIsEmpty(&pq))
	{
		printf("Empty\n");
		exit(-1);
	}
	return pq->ary[Next(pq->first)];
}
```
<br>

### CircularQueueMain.c 
```
#include <stdio.h>
#include "CircularQueue.h"

int main()
{
	Queue queue;
	QueueInit(&queue);
	Enqueue(&queue, 1); Enqueue(&queue, 2);
	Enqueue(&queue, 3); Enqueue(&queue, 4);
	Enqueue(&queue, 5);

	while (!QIsEmpty(&queue))
	{
		printf("%d ", Dequeue(&queue));
	}
	return 0;
}
```
<br>

## 3. 큐의 연결 리스트 기반 구현
---
### ListBaseQueue.h
```
#ifndef __LB_QUEUE_H__
#define __LB_QUEUE_H__

#define TRUE	1
#define FALSE	0

typedef int Data;

typedef struct _node
{
	Data data;
	struct _node * next;
} Node;

typedef struct _lQueue
{
	Node * front;
	Node * rear;
} LQueue;

typedef LQueue Queue;

void QueueInit(Queue * pq);
int QIsEmpty(Queue * pq);

void Enqueue(Queue * pq, Data data);
Data Dequeue(Queue * pq);
Data QPeek(Queue * pq);

#endif
```
<br>

### ListBaseQueue.c
```
#include <stdio.h>
#include <stdlib.h>
#include "ListBaseQueue.h"

void QueueInit(Queue * pq)
{
	pq->front = NULL;
	pq->rear = NULL;
}

int QIsEmpty(Queue * pq)
{
    // front만 고려해도 되는 이유
    // 처음 초기화시 front와 rear 모두 NULL을 가리킴
    // 마지막 노드의 next는 NULL로 정의할 것이므로 모두 삭제시 
    // front는 NULL을 가리키게됨.
    // 따라서 비어있는 경우는 front 만으로도 판단 가능
	if(pq->front == NULL)
		return TRUE;
	else
		return FALSE;
}

void Enqueue(Queue * pq, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->next = NULL; // 반드시 NULL 초기화 필요(삭제시 이용)
	newNode->data = data;

	if(QIsEmpty(pq))
	{
		pq->front = newNode;
		pq->rear = newNode;
	}
	else
	{
		pq->rear->next = newNode;
		pq->rear = newNode;
	}
}

Data Dequeue(Queue * pq)
{
	Node * delNode;
	Data retData;

	if(QIsEmpty(pq)) // &pq가 아님 혼동 주의!
	{
		printf("Queue Memory Error!");
		exit(-1);
	}

	delNode = pq->front;
	retData = delNode->data;
	pq->front = pq->front->next;

	free(delNode);
	return retData;
}

Data QPeek(Queue * pq)
{
	if(QIsEmpty(pq)) // &pq가 아님 혼동 주의!
	{
		printf("Queue Memory Error!");
		exit(-1);
	}

	return pq->front->data;
}
```


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
