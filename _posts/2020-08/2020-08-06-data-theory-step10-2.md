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
  - [1. 힙 정렬](#1-힙-정렬)
  - [2. 병합 정렬](#2-병합-정렬)
  - [3. 퀵 정렬](#3-퀵-정렬)
  - [4. 기수 정렬](#4-기수-정렬)

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
힙의 빅-오는 O(log(n)) 이고 n개의 데이터를 뽑아내므로 O(n log(n)) 이다.  
<br>

## 2. 병합 정렬 : Divide And Conquer
---
1. 분할 : 해결이 용이한 단계까지 문제를 분할해 나간다.
2. 정복 : 해결이 용이한 수준까지 분할된 문제를 해결한다.
3. 분할해서 해결한 결과를 결합하여 마무리한다.

### 분할 방법
![그림1](https://backtony.github.io/assets/img/post/data/step10/5.PNG)

### 재귀적 구현
구현하기 전에 재귀적 생각에 대해 다시 고민해보자. 재귀적으로 들어가는 것을 분석하려고 하면 끝도 없다. 병합 정렬의 함수를 만들고 그 안에서 병합 정렬 함수를 호출하면 그 기능을 하겠구나라고만 생각하고 사고를 끝내야한다.  
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
### 성능평가
![그림2](https://backtony.github.io/assets/img/post/data/step10/6.PNG)

정렬의 대상인 데이터의 수가 n개일 때, 각 병합의 단계마다 최대 n번의 비교연산이 진행된다. 데이터의 수 n과 그에 따른 병합 과정의 횟수는 log(n)이다. 따라서 데이터 수에 대한 비교 연산의 횟수는 n log_(n)이고 빅-오는 O(n log(n)) 이다.  
<br>

## 3. 퀵 정렬
---
### 퀵 정렬 : 이해
![그림3](https://backtony.github.io/assets/img/post/data/step10/7.PNG)

+ left : 정렬대상의 가장 왼쪽 지점
+ right : 정렬대상의 가장 오른쪽 지점
+ pivot : 중심점, 중심축의 의미를 담고 있음
+ low : 피벗을 제외한 가장 왼쪽 지점
+ high : 피벗을 제외한 가장 오른쪽 지점

피벗은 달리 결정할 수 있지만 가장 왼쪽에 위치한 데이터를 피벗으로 결정하기로 하자.

![그림4](https://backtony.github.io/assets/img/post/data/step10/8.PNG)

+ low의 오른쪽 방향 이동 : 피벗보다 큰 값을 만날 때까지 이동. 즉, 피벗보다 정렬 우선순위가 낮은 데이터를 만날 때 까지
+ high 의 왼쪽 방향 이동 : 피벗보다 작은 값을 만날 때 까지 이동. 즉, 피벗보다 정렬 우선순위가 높은 데이터를 만날 때 까지

![그림5](https://backtony.github.io/assets/img/post/data/step10/9.PNG)

교환하고 위 과정을 반복하다가 high와 low가 역전되면 high를 피벗과 교환하고 두 개의 영역으로 나누어 반복 실행 => 재귀적

![그림6](https://backtony.github.io/assets/img/post/data/step10/10.PNG)

### 구현
```
#include<stdio.h>
void Swap(int* arr, int a1, int a2)
{
	int tmp;
	tmp = arr[a1];
	arr[a1] = arr[a2];
	arr[a2] = tmp;
}

int Partition(int* arr, int left, int right)
{
	int pivot = arr[left];
	int high = right, low = left + 1;
	while (low <= high)
	{
		// >만 있으면 3 3 3 같이 같은것이 3개 있을때 무한루프를 돌게됨
		// 따라서 같아도 교환과정이 이뤄지게 해야함
		// low,high의 범위 설정, = 이 있어야 교차가 발생
		// = 이 없으면 무한루프 발생
		while (pivot >= arr[low] && low <= right)
			low++;
		while (pivot <= arr[high] && high >= left + 1)
			high--;
		if (low <= high) // 사실상 =는 없어도 됨 위에서 다 걸러짐
			Swap(arr, low, high);
	}
	Swap(arr, left, high);
	return high;
}

void QuickSort(int* arr, int left, int right)
{
	if (left <= right) 
	{
		int pivot = Partition(arr, left, right); // 둘로 나눠서
		QuickSort(arr, left, pivot - 1); // 왼쪽 영역 정렬
		QuickSort(arr, pivot + 1, right); // 오른쪽 영역 정렬
	}
}

int main(void)
{
	int arr[7] = {3, 2, 4, 1, 7, 6, 5};
	

	int len = sizeof(arr) / sizeof(int);
	int i;

	QuickSort(arr, 0, sizeof(arr) / sizeof(int) - 1);

	for (i = 0; i < len; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
```
__중간 값 고르기__  
위 코딩에서는 피벗을 자동적으로 맨 왼쪽으로 선택하도록 했다. 이때 int arr[7] = {1,2,3,4,5,6,7} 이렇게 선언될 경우 최악의 상황이 연출된다. 따라서 정렬대상의 가장 왼쪽, 가장 오른쪽, 그리고 중간에 위치한 값을 추출해서 이 중에서 중간에 해당하는 값을 피벗으로 바꿔보자.
```
#include <stdio.h>

void Swap(int arr[], int idx1, int idx2)
{
	int temp = arr[idx1];
	arr[idx1] = arr[idx2];
	arr[idx2] = temp;
}	

int MedianOfThree(int arr[], int left, int right)
{
	int samples[3] = {left, (left+right)/2, right};

	if(arr[samples[0]] > arr[samples[1]])
		Swap(samples, 0, 1);

	if(arr[samples[1]] > arr[samples[2]])
		Swap(samples, 1, 2);

	if(arr[samples[0]] > arr[samples[1]])
		Swap(samples, 0, 1);

	return samples[1];
}

int Partition(int arr[], int left, int right)
{
	int pIdx = MedianOfThree(arr, left, right);   // 피벗을 선택!
	int pivot = arr[pIdx];

	int low = left+1;
	int high = right;

	Swap(arr, left, pIdx);    // 피벗을 가장 왼쪽으로 이동

	// 이후의 코딩은 위에서 구현한 것과 같다.
```


### 성능평가
![그림7](https://backtony.github.io/assets/img/post/data/step10/11.PNG)

모든 데이터가 피벗과의 데이터 비교를 진행한다. 따라서 이 경우 약 n번의 비교 연산이 진행된다. 최선의 경우 log_n번 이루어 지므로 빅-오는 O(n log(n))이다.

![그림8](https://backtony.github.io/assets/img/post/data/step10/12.PNG)

중간에 가까운 값으로 빅-오를 선택하려는 노력을 조금만 하더라도 퀵 정렬은 최악의 경우를 만들지 않는다. 따라서 퀵 정렬의 성능은 최상의 경우를 근거로 이야기한다. 하지만 최악의 경우 있다는 것을 알아두자. 최약의 경우 둘로 나뉘는 횟수가 약 n번, 매 단계별 비교 연산의 횟수가 약 n이므로 O(n^2)이다.  
<br>

## 4. 기수 정렬
---
### 특징과 적용 범위
+ 정렬순서의 앞서고 뒤섬을 비교하지 않는다.
+ 정렬 알고리즘의 한계로 알려진 O(n log_n)을 뛰어 넘을 수 있다.
+ 적용할 수 있는 대상이 매우 제한적이다. 길이가 동일한 데이터들의 정렬에 용이하다.

### 원리
![그림9](https://backtony.github.io/assets/img/post/data/step10/13.PNG)

+ 기수(radix) : 주어진 데이터를 구성하는 기본 요소(기호)
+ 버킷(bucket) : 기수의 수에 해당하는 만큼의 버킷을 활용

그림을 보면 알겠지만 버킷의 형태는 큐와 같다.

### 기수 정렬 : LSD
List Significant Digit을 시작으로 정렬을 진행하는 방식

![그림10](https://backtony.github.io/assets/img/post/data/step10/14.PNG)

그림과 같은 과정을 일의 자리(첫 자리)부터 마지막 자리 까지 반복한다. 그림은 최고숫자가 4이기 때문에 0~4까지의 버킷을 만들었지만 일반적으로 십진수라면 0~9까지의 버킷이 만들어 진다.  

### 기수 정렬 : MSD
MSD는 정렬의 기준 선정 방향이 LSD와는 반대이다. 하지만 방향성에서만 차이를 보이는 것은 아니다.
![그림11](https://backtony.github.io/assets/img/post/data/step10/15.PNG)

위 그림은 정렬의 기준 선정 방향만 바꾸어서 기수 정렬을 진행한 결과이다. 따라서 MSD 정렬 방식에서는 기준 선정 방향이 반대일 뿐만 아니라 중간 중간에 정렬이 완료된 데이터는 더 이상의 정렬과정을 진행하지 않아야한다. 백의 자리에서 정렬을 맞췄으면 십의 자리에서는 이제 백의자리 2와 1을 구분해서 정렬을 해줘야한다는 뜻이다. LSD방식에서는 모든 데이터가 정렬의 과정을 동일하게 거치도록 구현되지만 MSD 방식에서는 선별을 거치도록 구현해야 한다. 따라서 LSD 방식 구현이 더 용이하다.  

### LSD 기준 구현
MSD와 LSD의 빅-오는 같다. 하지만 LSD의 구현이 더 용이하므로 LSD를 기준으로 기수 정렬을 구현하는 것이 일반적이다.  
십진수 3자리 숫자로 정렬을 해보자.
+ NUM으로부터 첫 번째 자리 추출 : NUM / 1 % 10
+ NUM으로부터 둘 번째 자리 추출 : NUM / 10 % 10
+ NUM으로부터 셋 번째 자리 추출 : NUM / 100 % 10 

큐는 이전에 구현한 것을 활용한다. [[클릭](http://127.0.0.1:4000/data/2020/08/02/data-theory-step7-1/)]
```
#include <stdio.h>
#include "ListBaseQueue.h"

#define BUCKET_NUM		10

void RadixSort(int arr[], int num, int maxLen)   // maxLen은 가장 긴 데이터의 길이
{
	Queue buckets[BUCKET_NUM];
	int bi;
	int pos;
	int di;
	int divfac = 1;
	int radix;

	// 총 10개의 버킷 초기화
	for(bi=0; bi<BUCKET_NUM; bi++)
		QueueInit(&buckets[bi]);

	// 가장 긴 데이터의 길이만큼 반복
	for(pos=0; pos<maxLen; pos++)
	{ 
		// 정렬 대상의 수만큼 반복
		for(di=0; di<num; di++)
		{
			// N번째 자리의 숫자 추출
			radix = (arr[di] / divfac) % 10;

			// 추출한 숫자를 근거로 데이터 버킷에 저장
			Enqueue(&buckets[radix], arr[di]);
		}

		// 버킷 수만큼 반복
		for(bi=0, di=0; bi<BUCKET_NUM; bi++)
		{
			// 버킷에 저장된 것 순서대로 다 꺼내서 다시 arr에 저장
			while(!QIsEmpty(&buckets[bi]))
				arr[di++] = Dequeue(&buckets[bi]);
		}

		// N번째 자리의 숫자 추출을 위한 피제수의 증가
		divfac *= 10;
	}	
}

int main(void)
{
	int arr[7] = {13, 212, 14, 7141, 10987, 6, 15};

	int len = sizeof(arr) / sizeof(int);
	int i;

	RadixSort(arr, len, 5);

	for(i=0; i<len; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
```
### 성능평가
삽입도 n번 추출도 n번, 이 과정이 maxLen 최대 길이만큼 발생 => 빅-오는 2n * maxLen => O(nl) 이다. (정렬 대상의 길이를 l이라고 가정)

---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__