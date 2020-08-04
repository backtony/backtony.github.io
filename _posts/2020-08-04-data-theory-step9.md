---
layout: post
title:  우선순위 큐(Priority Queue)와 힙(Heap)
subtitle: 우선순위 큐(Priority Queue)와 힙(Heap)
categories: data
tags: theory book datastructure priorityqueue heap 힙 우선순위큐
comments: true
# header-img:
---
+ __목차__
  - [1. 우선순위 큐의 이해](#1-우선순위-큐의-이해)
  - [2. 힙의 구현](#2-힙의-구현)
  - [3. 우선순위 큐의 완성](#3-우선순위-큐의-완성)


## 1. 우선순위 큐의 이해
---
### 우선순위 큐의 구현 방법
+ 배열을 기반으로 구현하는 방법
+ 연결 리스트를 기반으로 구현하는 방법
+ 힙을 이용하는 방법

배열 기반과 연결리스트 기반을 이용하면 최악의 경우 새 데이터의 위치를 찾기 위해 기존에 저장된 모든 데이터와 비교를 진행해야 한다. 따라서 힙으로 구현하는 것이 적절하다.  
힙은 트리이다. 그럼 힙을 배열로 구현해야할까 연결 리스트로 구현해야할까? 새로운 노드를 힙의 마지막 위치에 쉽게 추가하기 위해서는 배열을 기반으로 하는 것이 더 쉽다. 따라서 배열을 기반으로 구현한다.  

## 2. 힙의 구현
---
### 힙의 소개
![그림1](https://backtony.github.io/assets/img/post/data/step9/1.PNG)

+ 힙은 완전 이진 트리이다.
+ 힙의 구현은 배열을 기반으로 인덱스가 0인 요소는 비워둔다.
+ 힙에 저장된 노드의 개수와 마지막 노드의 고유번호는 일치한다. => 마지막 노드의 인덱스 값을 쉽게 얻을 수 있다.
+ 노드의 고듀번호가 노드가 저장되는 배열의 인덱스 값이 된다.
+ 우선순위를 나타내는 정수 값이 작을수록 높은 우선순위를 나타낸다고 가정한다.


### 구현에 필요한 지식들
+ 왼쪽 자식 노드의 인덱스 값 = 부모 노드의 인덱스 값 * 2
+ 오른쪽 자식 노드의 인덱스 값 = 부모 노드의 인덱스 값 * 2 +1
+ 부모 노드의 인덱스 값 = 자식 노드의 인덱스 값 / 2 (정수형 나눗셈)


### 힙 구현
__SimpleHeap.h__  
```
#ifndef __SIMPLE_HEAP_H__
#define __SIMPLE_HEAP_H__

#define HEAP_LEN 100
#define TRUE 1
#define FALSE 0

typedef char HData;

// d1의 우선순위가 높다면 0보다 큰 값
// d2의 우선순위가 높다면 0보다 작은 값
// d1과 d2의 우선순위가 같다면 0을 반환
typedef int (*PriorityComp)(HData d1, HData d2);

typedef struct __heap
{
	HData heapArr[HEAP_LEN];
	int numOfData;
	PriorityComp comp;
}Heap;

void HeapInit(Heap* ph, PriorityComp pc);
int HIsEmpty(Heap* ph); 
void HInsert(Heap* ph, HData data);
HData HDelete(Heap* ph);


#endif
```
__SimpleHeap.c__  
```
#include "SimpleHeap.h"

void HeapInit(Heap* ph, PriorityComp pc)
{
	ph->numOfData = 0;
	ph->comp=pc;
}

int HIsEmpty(Heap* ph)
{
	if (ph->numOfData == 0) return TRUE;
	return FALSE;
}

int GetParentIDX(int idx) //부모 인덱스
{
	return idx / 2;
}

int GetLChildIDX(int idx)
{
	return idx * 2;
}

int GetRChildIDX(int idx)
{
	return idx * 2 +1;
}

int GetHiPrChildIDX(Heap* ph, int idx)
{
	if (GetLChildIDX(idx) > ph->numOfData) return 0;
	else if (GetLChildIDX(idx) == ph->numOfData) return GetLChildIDX(idx);
	else
	{
		if (ph->comp(ph->heapArr[GetLChildIDX(idx)], ph->heapArr[GetRChildIDX(idx)])<0)
			return GetRChildIDX(idx);
		else return GetLChildIDX(idx);
	}
}

void HInsert(Heap* ph, HData data)
{
	int idx = ph->numOfData + 1; // insert될 위치 인덱스
	
	while (idx !=1)
	{
		if (ph->comp(data,ph->heapArr[GetParentIDX(idx)])>0)
		{
			ph->heapArr[idx] = ph->heapArr[GetParentIDX(idx)];
			idx = GetParentIDX(idx);
		}
		else break;
	}
	ph->heapArr[idx] = data;
	(ph->numOfData)++;
	
}

// 그림상은
// 루트 노드의 data값을 지우면서 제일 마지막에 있던 노드 값을
// 루트 노드 자리에 두고 비교를 해가면서 자리를 찾아간다.

//코드상은
// 마지막 노드를 복사해두고 인덱스값만 1이라고 두고 비교한다.
HData HDelete(Heap* ph)
{
	HData rmdata = ph->heapArr[1]; // 반환값
	HData lastdata = ph->heapArr[ph->numOfData];
	int parentIdx = 1, childIdx;

	//아래 노드가 있을때 계속 반복한다는 것을 조건으로
    //중요! parentIdx 노드 아래에 노드가 없으면 멈춤
    // while(1) 로 하면 절대 안돼!! 무한반복 .. 
	while (childIdx = GetHiPrChildIDX(ph, parentIdx)) 
	{	
        //			
		if (ph->comp(lastdata, ph->heapArr[childIdx])<0)
		{
			ph->heapArr[parentIdx] = ph->heapArr[childIdx];
			parentIdx = childIdx;
		}
		else break;
	}
	ph->heapArr[parentIdx] = lastdata;
	(ph->numOfData)--;
	return rmdata;
}

```
__Main.c //활용__  
```
#include <stdio.h>
#include "SimpleHeap.h"

int DataPriorityComp(char ch1, char ch2)
{
	return ch2 - ch1;
	//	return ch1-ch2;
}

int main(void)
{
	Heap heap;
	HeapInit(&heap, DataPriorityComp);

	HInsert(&heap, 'A');
	HInsert(&heap, 'B');
	HInsert(&heap, 'C');
	printf("%c \n", HDelete(&heap));

	HInsert(&heap, 'A');
	HInsert(&heap, 'B');
	HInsert(&heap, 'C');
	printf("%c \n", HDelete(&heap));

	while (!HIsEmpty(&heap))
		printf("%c \n", HDelete(&heap));

	return 0;
}

```

## 3. 우선순위 큐의 완성
---
힙을 완성했으니 이제 우선순위 큐를 구현할 차례다. 그런데 우선순위 큐를 고려햐여 힙을 구현했기 때문에 사실상 우선순위 큐를 구현한 것이나 다름없다.

### 우선순위 큐 자료구조의 ADT
+ Void PQueueInit(PQueue *ppq,PriorityComp pc);
    - 우선순위 큐 초기화
+ int PQIsEmpty(PQueue * ppq);
    - 빈 경우 TRUE(1) , 아닐 경우 FALSE(0) 반환
+ void PEnqueue(PQueue *ppq, PQData data);
    - data를 받아 우선순위 큐에 저장
+ PQData PDequeue(PQueue * ppq);
    - 우선순위 가장 높은 데이터 삭제
    - 삭제 데이터 반환
    - 데이터 하나 이상존재가 보장되어있어야함

위에 구현한 힙을 그대로 이용하면 되므로 함수 구현 파일만 작성하겠다.  
__PriorityQueue.c__  
```
#include "PriorityQueue.h"
#include "SimpleHeap.h"

void PQueueInit(PQueue * ppq, PriorityComp pc)
{
	HeapInit(ppq, pc);
}

int PQIsEmpty(PQueue * ppq)
{
	return HIsEmpty(ppq);
}

void PEnqueue(PQueue * ppq, PQData data)
{
	HInsert(ppq, data);
}

PQData PDequeue(PQueue * ppq)
{
	return HDelete(ppq);
}
```


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__