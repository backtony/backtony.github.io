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
  - [1. 버블 정렬](#1-버블-정렬)
  - [2. 선택 정렬](#2-선택-정렬)
  - [3. 삽입 정렬](#3-삽입-정렬)

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

![그림3](https://backtony.github.io/assets/img/post/data/step10/3.PNG)

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
if(arr[j] < arr[maxidx]) 
```
최악의 경우와 최상의 경우 구분 없이 비교 횟수가 동일하다. 비교 횟수가 (n-1) + (n-2) + ... +2 +1 이므로 빅오는 O($$n^2$$) 이다.  

## 3. 삽입 정렬
---
### 삽입 정렬의 이해
![그림4](https://backtony.github.io/assets/img/post/data/step10/4.PNG)

선택 정렬은 우선순위가 가장 높은 데이터를 선택해서 해당 자리에 가져다 놓고 그 자리에서 더이상 바뀌지 않는다. 하지만 삽입 정렬은 제일 첫 번째는 이미 정렬되어있다고 가정하고 그 이후의 정렬 안되었던 것들을 하나씩 정렬된 곳으로 옮기면서 그것의 위치를 정한다. 구현을 고려하면 정렬된 곳으로 옮길때 정렬되어있는 곳의 제일 뒤에 것부터 비교하면서 하나씩 뒤로 밀어내는 형식으로 코딩한다.  

### 삽입 정렬 구현
```
#include<stdio.h>

void InserSort(int* arr, int n)
{
	int i, j,tmp;
	// 비교, 이동의 최종적인 정렬과정을 총 n-1번 해야함
	for (i = 1; i < n ; i++) // 인덱스 0은 이미 정렬되어있다고 가정
	{
		tmp = arr[i];
		for (j = i-1; j >=0 ; j--) // 비교 과정 진행
		{
			if (tmp < arr[j])
			{
				arr[j+1] = arr[j]; // 한칸밀기
			}
			else break;
		}
		arr[j + 1] = tmp;
	}
}

int main()
{
	int arr[4] = { 3,2,4,1 };
	int i;
	InserSort(arr, sizeof(arr) / sizeof(arr[0]));

	for (i = 0; i < 4; i++)
		printf("%d ", arr[i]);
	return 0;
}
```

### 성능평가
```
if (tmp < arr[j])
```
최악의 경우 else는 한 번도 실행되지 않고 비교연산이 실행된다. 비교 횟수가 1 + 2 + .....  (n-2) + (n-1) 이므로 빅오는 O($$n^2$$) 이다.  

---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__