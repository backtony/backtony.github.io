---
layout: post
title:  (Question 3-2) 리스트 활용
subtitle: (Question 3-2) 리스트 활용
categories: data
tags: question book datastructure linkedlist 연결리스트 배열리스트
comments: true
# header-img:
---
## 문제
---
NameCard.h 에 대응하는 소스파일 NameCard.c를 작성하자. 그리고 아래 나열된 순서대로 main함수를 정의하자. [3-1](https://backtony.github.io/data/2020/07/31/data-question-step3-1/)에서 구현한 리스트를 활용해야한다.  

### NameCard.h // 주어진 헤더 
```
#ifndef __NAME_CARD_H__
#define __NAME_CARD_H__

#define NAME_LEN		30
#define PHONE_LEN		30

typedef struct __namecard
{
	char name[NAME_LEN];
	char phone[PHONE_LEN];
} NameCard;


// NameCard 구조체 변수의 동적 할당 및 초기화 후 주소 값 반환
NameCard * MakeNameCard(char * name, char * phone);
   
// NameCard 구조체 변수의 정보 출력
void ShowNameCardInfo(NameCard * pcard);
   
// 이름이 같으면 0, 다르면 0이 아닌 값 반환
int NameCompare(NameCard * pcard, char * name);
   
// 전화번호 정보를 변경
void ChangePhoneNum(NameCard * pcard, char * phone);


#endif
```

1. 총 3명의 전화번호 정보를 앞서 구현한 리스트에 저장한다.
2. 특정 이름을 대상으로 탐색을 진행하여 그 사람의 정보를 출력한다.
3. 특정 이름을 대상으로 탐색을 진행하여, 그 사람의 전화번호 정보를 변경한다.
4. 특정 이름을 대상으로 탐색을 진행하여, 그 사람의 정보를 삭제한다.
5. 끝으로 남아 있는 모든 사람의 전화번호 정보를 출력한다.

<br>

## 풀이
---
먼저 ArrayList.h 에서 변경사항이 있습니다.
문제에서 저장의 형태는 NameCard 구조체 변수의 주소값이라고 했으며, NameCard*의 정의는 NameCard.h 헤더에 있기 때문에 다음과 같이 추가/ 수정을 해줘야 합니다.
```
#include "NameCard.h"
typedef NameCard* LData;
```

### NameCard.c
```
#include <stdio.h>
#include <string.h>
#include "NameCard.h"

// NameCard 구조체 변수의 동적 할당 및 초기화 후 주소 값 반환
NameCard* MakeNameCard(char* name, char* phone)
{
	NameCard* NewNameCard;
	NewNameCard = (NameCard*)malloc (sizeof(NameCard));
	strcpy(NewNameCard->name, name);
	strcpy(NewNameCard->phone, phone);
	return NewNameCard;
}
// NameCard 구조체 변수의 정보 출력
void ShowNameCardInfo(NameCard* pcard)
{
	printf("%s\n", pcard->name);
	printf("%s\n\n", pcard->phone);
}

// 이름이 같으면 0, 다르면 0이 아닌 값 반환
int NameCompare(NameCard* pcard, char* name)
{
	return strcmp(pcard->name, name);
}

// 전화번호 정보를 변경
void ChangePhoneNum(NameCard* pcard, char* phone)
{
	strcpy(pcard->phone, phone);
}
```
<br>

### Main.c
```
#include <stdio.h>
#include "ArrayList.h"
#include "NameCard.h"
int main(void)
{
	List list;
	NameCard* pcard;

	ListInit(&list);
	
    // pcard안에 있는 주소값만 다른 포인터에 복사해서 list에 대입
    // 따라서 &pcard가 아닌 pcard를 대입
    // 함수 정의를 보면 한 번에 알 수 있긴하나 논리를 생각할것
	pcard = MakeNameCard("이순신", "111-1111-1111");
	LInsert(&list,pcard);

	pcard = MakeNameCard("유관순", "222-2222-2222");
	LInsert(&list, pcard);

	pcard = MakeNameCard("장보고", "333-3333-33333");
	LInsert(&list, pcard);
    

	if (LFirst(&list, &pcard)) 
    // pcard대입시 pcard가 가리키는 주소값 내부의 값을 바꾸는게 된다.
    // pcard가 가리키는 주소 자체를 바꿔야하므로 포인터 자체의 주소값을 주고 
    // 간접참조연산자로 포인터가 가리키는 주소를 바꿔준다.
	{
		if (!NameCompare(pcard->name,"유관순"))
		{
			ShowNameCardInfo(pcard);
		}
		else
		{
			while (LNext(&list, &pcard))
			{
				if (!NameCompare(pcard->name, "유관순"))
				{
					ShowNameCardInfo(pcard);
					break; // 찾고 출력했으면 멈추기
				}
			}
		}		
	}

	if (LFirst(&list, &pcard)) 
	{
		if (!NameCompare(pcard->name, "유관순"))
		{
			ChangePhoneNum(pcard, "5555-5555");
		}
		else
		{
			while (LNext(&list, &pcard))
			{
				if (!NameCompare(pcard->name, "유관순"))
				{
					ChangePhoneNum(pcard, "5555-5555");
					break;
				}
			}
		}
	}

	if (LFirst(&list, &pcard))
	{
		if (!NameCompare(pcard->name, "장보고"))
		{
			LRemove(&list);
		}
		else
		{
			while (LNext(&list, &pcard))
			{
				if (!NameCompare(pcard->name, "장보고"))
				{
					LRemove(&list);
					break;
				}
			}
		}
	}
	
	if (LFirst(&list, &pcard))
	{
		ShowNameCardInfo(pcard);
		while (LNext(&list, &pcard))
		{
			ShowNameCardInfo(pcard);
		}
		
	}
	return 0;
}
```

---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__