---
layout: post
title:  복잡하지만 효율적인 정렬 알고리즘
subtitle: 복잡하지만 효율적인 정렬 알고리즘
categories: data
tags: theory book datastructure sorting 정렬
comments: true
# header-img:
---
+ __목차__
  - [1. 버블 정렬](#1-버블-정렬)
  - [2. 선택 정렬](#2-선택-정렬)
  - [3. 삽입 정렬](#3-삽입-정렬)

## 1. 힙 정렬
---
### 구현
[[클릭](https://backtony.github.io/data/2020/08/04/data-theory-step9/)] 에서 구현한 힙을 사용한다.
```
#include<stdio.h>
#include "heap.h"

int PriComp(int n1, int n2)
{
	// 양수면 n1이 우선순위가 높음
	return n2 - n1; // 오름차순
}

void HeapSort(int* arr, int n, PriorityComp pc)
{
	Heap heap;
	HeapInit(&heap,pc);
	int i;
	
	// 정렬대상을 가지고 힙 구성
	for (i = 0; i < n; i++)
	{
		HInsert(&heap, arr[i]);
	}

	for (i = 0; i < n; i++)
	{
		arr[i] = HDelete(&heap);
	}
	
}

int main()
{
	int arr[4] = { 3,4,2,1 };
	int i;
	HeapSort(arr, sizeof(arr) / sizeof(arr[0]), PriComp);
	for (i = 0; i < 4; i++)
		printf("%d ", arr[i]);
	return 0;
}

```
### 성능평가
힙의 빅오는 O($$\log_2 n$$) 이고 n개의 데이터 이므로 O(n$$\log_2 n$$) 이다.

## 2. 병합 정렬 : Divide And Conquer
---
1. 분할 : 해결이 용이한 단계까지 문제를 분할해 나간다.
2. 정복 : 해결이 용이한 수준까지 분할된 문제를 해결한다.
3. 분할해서 해결한 결과를 결합하여 마무리한다.

### 분할 방법
![그림1](https://backtony.github.io/assets/img/post/data/step10/5.PNG)

### 재귀적 구현
구현 전에 재귀적 생각에 대해 다시 고민해보자. 재귀적으로 들어가는 것을 분석하려고 하면 끝도 없다. 병합 정렬의 함수를 만들고 그 안에서 병합 정렬 함수를 호출하면 그 기능을 하겠구나 라고만 생각하고 사고를 끝내야한다.  
```
#include<stdlib.h>
#include<stdio.h>
void MergeTwoArea(int* arr, int left, int mid, int right)
{
	int fIdx = left, rIdx = mid + 1, i;
	// right는 index값이므로 갯수로 하려면 +1
	int* sortArr = (int*)malloc(sizeof(int) * (right+1));
	int sIdx=left;
	while (fIdx <= mid && rIdx <= right)
	{
		if (arr[fIdx] < arr[rIdx])
		{
			sortArr[sIdx++] = arr[fIdx++];
		}
		else
			sortArr[sIdx++] = arr[rIdx++];
	}
	
	if (fIdx <= mid)
	{
		// for 기본적인것을 잘못 이해하고 있었다.
		// 루프를 돌때마다 i가 계속 초기화되는 것이 아니야
		// i는 처음 들어올때 초기화 되고 끝이야
		for(i=fIdx;i<=mid;i++,sIdx++)
			sortArr[sIdx] = arr[i];
	}
	else
	{
		for (i = rIdx; i <= right; i++, sIdx++)
			sortArr[sIdx] = arr[i];
	}
	// i는 0이 아님 
	// 함수 인자 범위 내에서 정렬이 된 것을 복사하는것
	for (i = left; i <= right; i++)
		arr[i] = sortArr[i];
	free(sortArr);
}


void MergeSort(int* arr, int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		MergeSort(arr,left, mid);
		MergeSort(arr,mid+1, right);
		// 분할이 되겠네 사고과정 끝
		// 분할이 끝났으면 병합
		MergeTwoArea(arr, left, mid, right);
	}
}

int main()
{
	int arr[7] = { 3,2,4,1,7,6,5 };
	int i;
	MergeSort(arr, 0, sizeof(arr) / sizeof(int) - 1);
	for (i = 0; i < 7; i++)
		printf("%d ", arr[i]);
	return 0;
}
```