---
layout: post
title:  (Question 3-1) 리스트 라이브러리의 활용
subtitle: (Question 3-1) 리스트 라이브러리의 활용
categories: data
tags: question book datastructure linkedlist 연결리스트 배열리스트
comments: true
# header-img:
---
## 문제
---
주어진 ArrayList.h, ArrayList.c 를 기반으로 다음의 순서대로 일이 진행되도록 main함수를 정의하자.
### ArrayLish.h
```
#ifndef __ARRAY_LIST_H__
#define __ARRAY_LIST_H__

#define TRUE	1
#define FALSE	0

/*** ArrayList의 정의 ****/
#define LIST_LEN	100
typedef int LData;

typedef struct __ArrayList
{
	LData arr[LIST_LEN];
	int numOfData;
	int curPosition;
} ArrayList;


/*** ArrayList와 관련된 연산들 ****/
typedef ArrayList List;

void ListInit(List * plist);
void LInsert(List * plist, LData data);

int LFirst(List * plist, LData * pdata);
int LNext(List * plist, LData * pdata);

LData LRemove(List * plist);
int LCount(List * plist);

#endif
```
### ArrayList.c
```
#include <stdio.h>
#include "ArrayList.h"

void ListInit(List * plist)
{
	(plist->numOfData) = 0;
	(plist->curPosition) = -1;
}

void LInsert(List * plist, LData data)
{
	if(plist->numOfData > LIST_LEN) 
	{
		puts("저장이 불가능합니다.");
		return;
	}

	plist->arr[plist->numOfData] = data;
	(plist->numOfData)++;
}

int LFirst(List * plist, LData * pdata)
{
	if(plist->numOfData == 0)
		return FALSE;

	(plist->curPosition) = 0;
	*pdata = plist->arr[0];
	return TRUE;
}

int LNext(List * plist, LData * pdata)
{
	if(plist->curPosition >= (plist->numOfData)-1)
		return FALSE;

	(plist->curPosition)++;
	*pdata = plist->arr[plist->curPosition];
	return TRUE;
}

LData LRemove(List * plist)
{
	int rpos = plist->curPosition;
	int num = plist->numOfData;
	int i;
	LData rdata = plist->arr[rpos];

	for(i=rpos; i<num-1; i++)
		plist->arr[i] = plist->arr[i+1];

	(plist->numOfData)--;
	(plist->curPosition)--;
	return rdata;
}

int LCount(List * plist)
{
	return plist->numOfData;
}
```
1. 리스트를 생성 및 초기화한 다음, 정수 1부터 9까지 리스트에 저장한다.
2. 리스트에 저장된 값을 순차적으로 참조하여 그 합을 계산하여 출력한다.
3. 리스트에 저장된 값들 중 2의 배수와 3의 배수에 해당하는 값을 모두 삭제한다.
4. 마지막으로 리스트에 저장된 데이터를 순서대로 출력한다.

<br>
---

## 풀이
---

### ArrayListMain.c
```
#include <stdio.h>
#include "ArrayLish.h"

int main(void)
{
	List list;
	int i,data,sum=0;
	ListInit(&list);
	for (i = 1; i < 10; i++)
	{
		LInsert(&list, i);
	}
	if (LFirst(&list, &data))
	{
		sum += data;
		while (LNext(&list, &data))
		{
			sum += data;
		}
	}
	printf("총 합 : %d\n", sum);
	if (LFirst(&list, &data))
	{
		if ((data % 2 == 0) || (data % 3 == 0))
		{
			LRemove(&list);
		}
		while (LNext(&list, &data))
		{
			if ((data % 2 == 0) || (data % 3 == 0))
			{
				LRemove(&list);
			}
		}
	}

	if (LFirst(&list, &data))
	{
		printf("%d ", data);
		while (LNext(&list, &data))
		{
			printf("%d ", data);
		}
	}
	return 0;
}
```


---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
