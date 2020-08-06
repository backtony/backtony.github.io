---
layout: post
title:  탐색 (Search) 1
subtitle: 탐색 (Search) 1
categories: data
tags: theory book datastructure search 탐색
comments: true
# header-img:
---
+ __목차__
  - [1. 힙 정렬](#1-힙-정렬)
  - [2. 병합 정렬](#2-병합-정렬)
  - [3. 퀵 정렬](#3-퀵-정렬)
  - [4. 기수 정렬](#4-기수-정렬)

## 1. 탐색의 이해와 보간 탐색
---
### 탐색의 이해
효율적인 탐색을 위해서는 '어떻게 찾을까'만을 고민해서는 안 된다. 그보다는 '효율적인 탐색을 위한 저장방법'을 우선 고민해야 한다. => 효율적인 탐색이 가능한 대표적인 자료구조는 __트리__ 이다.

### 보간 탐색
이진 탐색과 보간 탐색 모두 정렬이 완료된 데이터를 대상으로 탐색을 진행하는 알고리즘이다.
![그림1](https://backtony.github.io/assets/img/post/data/step11/1.PNG)

+ 이진 탐색 : 무조건 중간에 위치한 데이터를 탐색 위치로 결정
+ 보간 탐색 : 대상에 비례하여 탐색의 위치를 결정

### 보간 탐색 비례식 구성
![그림2](https://backtony.github.io/assets/img/post/data/step11/2.PNG)

인덱스 값과 데이터 간의 비례식으로 탐색 위치를 결정한다.

### 구현
```
#include <stdio.h>

int ISearch(int ar[], int first, int last, int target)
{
	int mid;
	// 이진탐색일때 탐색 대상이 없는 경우 //
/*	if(first > last)
		return -1;    */// -1의 반환은 탐색의 실패를 의미

	// 보간 탐색에서 이진탐색의 탐색 대상 없는 경우의 코드 사용시
	// 무한루프가 발생 => 보간 탐색 특징에 따라 코드 수정
	if (ar[first] > target || ar[last] < target)
		return -1;

	// 이진 탐색과의 차이점을 반영한 문장, 오차율 최소화로 double사용
	mid = ((double)(target - ar[first]) / (ar[last] - ar[first]) *
		(last - first)) + first;

	if (ar[mid] == target)
		return mid;    // 탐색된 타겟의 인덱스 값 반환
	else if (target < ar[mid])
		return ISearch(ar, first, mid - 1, target);
	else
		return ISearch(ar, mid + 1, last, target);
}


int main(void)
{
	int arr[] = { 1, 3, 5, 7, 9 };
	int idx;

	idx = ISearch(arr, 0, sizeof(arr) / sizeof(int) - 1, 7);
	if (idx == -1)
		printf("탐색 실패 \n");
	else
		printf("타겟 저장 인덱스: %d \n", idx);

	idx = ISearch(arr, 0, sizeof(arr) / sizeof(int) - 1, 2);
	if (idx == -1)
		printf("탐색 실패 \n");
	else
		printf("타겟 저장 인덱스: %d \n", idx);

	return 0;
}

```
<br>

## 2. 이진 탐색 트리
---
### 이진 탐색 트리의 이해
이진 탐색 트리 = 이진 트리 + 데이터의 저장 규칙
![그림3](https://backtony.github.io/assets/img/post/data/step11/3.PNG)

+ 이진 탐색 트리의 노드에 저장된 키(key)는 유일
+ 루트 노드의 키 > 왼쪽 서브 트리를 구성하는 키
+ 루트 노드의 키 < 오른쪽 서브 트리를 구성하는 키
+ 왼쪽과 오른쪽 서브 트리도 이진 탐색 트리

### 구현 방안
이진 탐색 트리도 이진 트리이니 이전에 구현한 이진 트리에 기능을 몇 개 추가한 뒤 활용한다.


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__