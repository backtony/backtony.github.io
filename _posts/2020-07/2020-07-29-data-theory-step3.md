---
layout: post
title:  배열을 이용한 리스트 구현
subtitle: 배열을 이용한 리스트 구현
categories: data
tags: theory book datastructure linkedlist 연결리스트
comments: true
# header-img:
---
+ __목차__
  - [1. 추상 자료형(ADT)의 이해](#1-추상-자료형adt의-이해)
  - [2. 배열을 이용한 리스트 구현](#2-배열을-이용한-리스트-구현)

## 1. 추상 자료형(ADT)의 이해
---
### 추상 자료형(ADT)이란?
구체적인 기능의 완성을 언급하지 않고, 순수하게 기능이 무엇인지를 나열한 것입니다.  
cf) 왜 자료형인데 관계가 없을까?  
예를 들어 구조체를 기반으로 지갑을 의미하는 Wallet이라는 자료형을 정의했다고 합시다. 하지만 이 정의만으로 Wallet이라는 자료형의 정의가 완성되는 것은 아닙니다. Wallet을 기반으로 하는 연산의 종류를 결정하는 것도 자료형 정의의 일부로 보아야 하고, 이러한 연산의 종류가 결정되었을때 자료형의 정의는 완성 되는 것입니다. 결론은 자료형의 정의에 기능 또는 연산과 관련된 내용을 명시할 수 있다는 것입니다.  
<br>

### 구조체의 추상 자료형 정의
구조체를 기반으로 지갑을 의미하는 Wallet의 추상 자료형이 다음과 같다고 가정합시다.
```
int takeoutmoney(wallet *pw, int coinNum, int billNum)
- 첫 인자로 전달된 주소의 지갑에서 돈을 꺼낸다.
- 두 번째 인자로 꺼낼 동전의 수, 세 번째 인자로 꺼낼 지폐의 수
- 꺼내고자 하는 총액 반환, 그만큼 돈에서 차감
void putmoney(wallet *pw, int coinNum, int billNum)
- 첫 인자로 전달된 주소의 지갑에 돈을 넣는다.
- 두 번째 인자로 넣을 동전 수, 세 번째 인자로 넣을 지폐 수
- 넣은 만큼 동전, 지폐수 증가
```
그런데 최소한 구조체 정의는 추상 자료형(ADT)에 포함시켜야 하지 않을까요? 물론 필요하면 포함시켜도 되지만 불필요한 것을 포함시킬 필요는 없습니다. 과연 구조체 정의는 필요한 정보일까요?
```
int main()
{
  Wallet mywallet; // 지갑 구조체, 지갑 하나 장만
  putmoney(&mywallet,3,6);
  res = takeoutmoney(&mywallet,1,3);
}
// 의미만 파악하세요 생략이 많이 됐습니다.
```
결론적으로 wallet 구조체의 멤버가 어떻게 구성되있는 지는 알 필요가 없습니다. 따라서, 구조체의 정의를 추상 자료형에 포함시키는 것은 불필요합니다.  
<br>

## 2. 배열을 이용한 리스트 구현
---
### 리스트의 이해
+ 순차 리스트 : 배열을 기반으로 구현된 리스트
+ 연결 리스트 : 메모리의 동적 할당을 기반으로 구현된 리스트

cf) 구현 방법을 기준으로 한 구분이므로 두 리시트의 ADT가 동일하다고 해서 문제가 되지 않습니다.  

+ 리스트의 특징
  - 저장 형태 : 데이터를 나란히 저장한다.
  - 저장 특성 : 중복이 되는 데이터의 저장을 허용한다.

### 배열 기반 리스트의 장단점
+ 장점 : 인덱스 값 기준으로 어디든 한 번에 참조 가능
+ 단점 : 배열이 길이가 초기 결정해야하며 변경이 불가능, 삭제의 과정에서 데이터의 이동(복사)가 매우 빈번히 발생

### 리스트 자료구조의 ADT 정의해보기
```
void ListInit(List *plist);
- 초기화할 리스트의 주소값을 인자로 전달
- 리스트 생성 후 제일 먼저 호출되어야 하는 함수

void LInset(List *plist, LData data);
- 리스트에 데이터 저장, 매개변수에 data 전달된 값을 저장

int LFirst(List *plist, LData *pdata);
- 첫 번째 데이터가 pdata가 가리키는 주소의 메모리에 저장
- 데이터의 참조를 위한 초기화 진행
- 참고 성공시 TRUE(1), 실패시 FALSE(0) 반환

int LNext(List *plist, LData *pdata);
- 참조된 데이터의 다음 데이터가 pdata가 가리키는 메모리에 저장
- 순차적인 참조를 위해서 반복 호출이 가능
- 참조를 새로 시작하려면 먼저 LFirst 함수 호출
- 참고 성공시 TRUE(1), 실패시 FALSE(0) 반환

LData LRemove(List *plist);
- LFirst 또는 LNext 함수의 마지막 반환 데이터를 삭제
- 삭제된 데이터는 반환 => 동적할당의 경우 메모리 반환해줘야하기때문
- 마지막 반환 데이터를 삭제하므로 연이은 반복 호출 허용 X

int LCount(List *plist)
- 리스트 저장 되있는 데이터의 수 반환
```

#### 리스트 ADT를 기반으로 실행을 위해서
+ 리스트 자료구조의 헤더파일
+ 리스트 자료구조의 소스파일
+ 리스트 관련 메인 함수 소스파일

#### ArrayList.h // 리스트 자료구조의 구현
```
#ifndef __ARRAY_LIST_H__
#define __ARRAY_LIST_H__

#define TRUE	1
#define FALSE	0

/*** ArrayList의 정의 ****/
#define LIST_LEN	100
typedef int LData; // 저장할 대상의 자료형 변경을 위한 typedef

typedef struct __ArrayList
{
	LData arr[LIST_LEN];
	int numOfData;   // 리스트에 저장된 데이터의 수
	int curPosition;  // 마지막 참조 위치 정보 저장
} ArrayList;  // 배열 기반 리스트를 의미하는 구조체


/*** ArrayList와 관련된 연산들 ****/
typedef ArrayList List;
/* 배열 리스트의 ADT */
void ListInit(List * plist);
void LInsert(List * plist, LData data);

int LFirst(List * plist, LData * pdata);
int LNext(List * plist, LData * pdata);

LData LRemove(List * plist);
int LCount(List * plist);

#endif
```
#### ArrayList.c // 리스트 자료구조의 함수 소스
```
#include <stdio.h>
#include "ArrayList.h"

void ListInit(List * plist)
{
	(plist->numOfData) = 0;
	(plist->curPosition) = -1; // 아무런 위치도 참조하지 않았음
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
	(plist->curPosition)--; // 참조위치 되돌리기
	return rdata;  // 삭제되는 데이터는 반환의 과정으로 되돌려주는것이 옳다!
}

int LCount(List * plist)
{
	return plist->numOfData;
}
```
#### ListMain.c // 구현된 자료구조의 활용
```
#include <stdio.h>
#include "ArrayList.h"

int main(void)
{
	/*** ArrayList의 생성 및 초기화 ***/
	List list;
	int data;
	ListInit(&list);

	/*** 5개의 데이터 저장 ***/
	LInsert(&list, 11);  LInsert(&list, 11);
	LInsert(&list, 22);  LInsert(&list, 22);
	LInsert(&list, 33);

	/*** 저장된 데이터의 전체 출력 ***/
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &data))    // 첫 번째 데이터 조회
	{
		printf("%d ", data);

		while(LNext(&list, &data))    // 두 번째 이후의 데이터 조회
			printf("%d ", data);
	}
	printf("\n\n");

	/*** 숫자 22을 탐색하여 모두 삭제 ***/
	if(LFirst(&list, &data))
	{
		if(data == 22)
			LRemove(&list);

		while(LNext(&list, &data))
		{
			if(data == 22)
				LRemove(&list);
		}
	}

	/*** 삭제 후 저장된 데이터 전체 출력 ***/
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &data))
	{
		printf("%d ", data);

		while(LNext(&list, &data))
			printf("%d ", data);
	}
	printf("\n\n");
	return 0;
}
```
결론적으로 만든 리스트를 사용하기 위해서는 헤더파일을 포함하고 헤더파일에 선언된 함수의 기능만 숙지하면 됩니다. 실제 리스트가 어떻게 구현됬는지는 확인할 필요가 없습니다.  
<br>

### 리스트에 구조체 변수 저장하기
위에 설명한 리스트에는 단순히 정수를 저장했지만 실제로는 각종 데이터들이 저장되므로 정의한 리스트에 구조체 변수의 주소 값을 저장해 봅시다.   
#### Point.h
```
#ifndef __ARRAY_LIST_H__
#define __ARRAY_LIST_H__

typedef struct _point
{
	int xpos;
	int ypos;
} Point;

 // Point 변수의 xpos, ypos 값 설정
void SetPointPos(Point * ppos, int xpos, int ypos);
// Point 변수의 xpos, ypos 정보 출력
void ShowPointPos(Point * ppos);
// 두 Point 변수의 비교
int PointComp(Point * pos1, Point * pos2);

#endif
```

#### Point.c
```
#include <stdio.h>
#include "Point.h"

void SetPointPos(Point * ppos, int xpos, int ypos)
{
	ppos->xpos = xpos;
	ppos->ypos = ypos;
}

void ShowPointPos(Point * ppos)
{
	printf("[%d, %d] \n", ppos->xpos, ppos->ypos);
}

int PointComp(Point * pos1, Point * pos2)
{
	if(pos1->xpos == pos2->xpos && pos1->ypos == pos2->ypos)
		return 0;
	else if(pos1->xpos == pos2->xpos)
		return 1;
	else if(pos1->ypos == pos2->ypos)
		return 2;
	else
		return -1;
}
```
구조체 Point와 구조체Point 관련 함수들의 선언과 정의를 했습니다. 이제 위에서 사용했던 배열 기반 리스트의 헤더파일 ArrayList.h를 수정해주면 됩니다. 하지만 제대로 구현 됐다면 소스파일(ArrayLish.c)에서는 변경이 발생해서는 안됩니다.  
ArrayList.h에서는 배열 저장 대상이 정수이므로 typedef int LData 를 사용했지만 이제는 구조체 변수의 주소를 받아야하기 때문에 typedef Point* LData 로 바꿔줘야 합니다.  
#### PointListMain.c
```
#include <stdio.h>
#include <stdlib.h>
#include "ArrayList.h"
#include "Point.h"

int main(void)
{
	List list;        // 리스트 배열 구조체 변수 선언
	Point compPos;    
	Point * ppos;   // Point구조체 동적할당한 주소 대입할 구조체 포인터

	ListInit(&list);

	/*** 4개의 데이터 저장 ***/
	// Point 구조체크기만큼 메모리 할당한 Point 구조체 주소 반환
  ppos = (Point*)malloc(sizeof(Point));   

  // 해당 주소 Point 구조체의 멤버값 대입
	SetPointPos(ppos, 2, 1);                

  // 리스트배열에 point구조체크기만큼 메모리 할당한 Point 구조체 주소 저장
	LInsert(&list, ppos);                   

  // 또 다른 Point 구조체크기만큼 메모리 할당한 Point 구조체 주소 반환
	ppos = (Point*)malloc(sizeof(Point));  
  SetPointPos(ppos, 2, 2);
	LInsert(&list, ppos);

	ppos = (Point*)malloc(sizeof(Point));
	SetPointPos(ppos, 3, 1);
	LInsert(&list, ppos);

	ppos = (Point*)malloc(sizeof(Point));
	SetPointPos(ppos, 3, 2);
	LInsert(&list, ppos);

  // 여기까지 리스트 배열에 동적할당안 Point 구조체 주소들을 대입 완료

	/*** 저장된 데이터의 출력 ***/
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &ppos))
	{
		ShowPointPos(ppos);

		while(LNext(&list, &ppos))
			ShowPointPos(ppos);
	}
	printf("\n");

	/*** xpos가 2인 모든 데이터 삭제 ***/
	compPos.xpos=2;
	compPos.ypos=0;

	if(LFirst(&list, &ppos))
	{
		if(PointComp(ppos, &compPos)==1)
		{
      // 배열에 대입된 동적할당 주소값을 지웠을뿐 그 주소값의 메모리 공간은 사라지지 않음
      // 삭제값을 반환해야하는 이유가 여기서 나옴. 동적 메모리 공간 반환하기 위해
			ppos=LRemove(&list);          			
      free(ppos);                  
		}

		while(LNext(&list, &ppos))
		{
			if(PointComp(ppos, &compPos)==1)
			{
				ppos=LRemove(&list);
				free(ppos);
			}
		}
	}

	/*** 삭제 후 남은 데이터 전체 출력 ***/
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if(LFirst(&list, &ppos))
	{
		ShowPointPos(ppos);

		while(LNext(&list, &ppos))
			ShowPointPos(ppos);
	}
	printf("\n");

	return 0;
}
```

---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
