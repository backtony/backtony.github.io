---
layout: post
title:  단순한 정렬 알고리즘
subtitle: 단순한 정렬 알고리즘
categories: data
tags: theory book datastructure sorting 정렬
comments: true
# header-img:
---
+ __목차__
  - [1. 우선순위 큐의 이해](#1-우선순위-큐의-이해)
  - [2. 힙의 구현](#2-힙의-구현)
  - [3. 우선순위 큐의 완성](#3-우선순위-큐의-완성)

## 1. 버블 정렬
---
### 버블 정렬의 이해
![그림1](https://backtony.github.io/assets/img/post/data/step10/1.PNG)

그림은 이제 4의 위치를 확정했다. 이제 다시 앞의 3개의 공간을 다시 정렬해야 한다. 따라서 그림과 같은 방법으로 n-1번 반복하여 비교연산을 통해 정렬하는 방법이다. 최종결과는 1 2 3 4 이다.  

### 버블 정렬 구현
```
#include<stdio.h>

void BubbleSort(int* arr, int n)
{
	int i, j,tmp;
	// 비교, 이동의 최종적인 정렬과정을 총 n-1번 해야함
	for (i = 0; i < n - 1; i++) // 전체적인 과정을 몇 번 진행
	{
		for (j = 0; j < n - 1 - i; j++) // 비교 과정 진행
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = tmp;
			}
		}
	}
}

int main()
{
	int arr[4] = { 3,2,4,1 };
	int i;
	BubbleSort(arr, sizeof(arr) / sizeof(arr[0]));

	for (i = 0; i < 4; i++)
		printf("%d ", arr[i]);
	return 0;
}
```
### 성능 평가
```
if(arr[j] > arr[j+1])
```
최악의 경우 비교 횟수와 이동 횟수가 일치한다. 비교 횟수가 (n-1) + (n-2) + ... +2 +1 이므로 빅오는 O($$n^2$$) 이다.

## 2. 선택 정렬
---
### 선택 정렬의 이해
![그림2](https://backtony.github.io/assets/img/post/data/step10/2.PNG)

하나씩 선택해서 정렬 결과를 완성해 나간다. 하지만 별도의 메로리 공간이 요구된다는 단점이 있다. 이 단점을 개선한 방법이 아래 사진이다.

[그림3](https://backtony.github.io/assets/img/post/data/step10/3.PNG)

하나씩 비워 가면서 이동시키는 방법이다.  

### 선택 정렬 구현
```
#include<stdio.h>

void SelSort(int* arr, int n)
{
	int i, j,maxidx,tmp;
	// 비교, 이동의 최종적인 정렬과정을 총 n-1번 해야함
	for (i = 0; i < n - 1; i++) // 전체적인 과정을 몇 번 진행
	{
		maxidx = i;
		for (j = i+1; j < n ; j++) // 비교 과정 진행
		{
			// 우선순위가 제일 높은 것은 maxidx에 대입
			if (arr[j] < arr[maxidx])
			{
				maxidx = j;
			}
		}
		tmp = arr[i];
		arr[i] = arr[maxidx];
		arr[maxidx] = tmp;
	}
}

int main()
{
	int arr[4] = { 3,2,4,1 };
	int i;
	SelSort(arr, sizeof(arr) / sizeof(arr[0]));

	for (i = 0; i < 4; i++)
		printf("%d ", arr[i]);
	return 0;
}
```
### 성능평가
```
if(arr[j] < arr[maxidx]>) 
```
최악의 경우와 최상의 경우 구분 없이 비교 횟수가 동일하다. 비교 횟수가 (n-1) + (n-2) + ... +2 +1 이므로 빅오는 O($$n^2$$) 이다.


