---
layout: post
title:  (Question 7-1) 큐의 활용
subtitle: (Question 7-1) 큐의 활용
categories: data
tags: question book datastructure queue 큐
comments: true
# header-img:
---
## 문제
---
햄버거집 대기실 만들기
+ 점심시간 1시간 동안에 고객이 15초당 1명씩 주문
+ 치즈버거 12초, 불고기버기 15초, 더블버거 24초
+ 한 명의 고객은 하나의 버거만 주문
+ 모든 메뉴는 무작위로 선택
+ 햄버거를 만드는 사람은 1명이고 동시에 만들 수 없다.
+ 주문한 메뉴를 받을 다음 고객은 대기실에서 나온다.

<br>

## 풀이
---
[[클릭](https://backtony.github.io/data/2020/08/02/data-theory-step7/)] 에서 사용한 배열 기반 큐 사용  
헤더에서 #define QUE_LEN 100 // 추가 , 만약 10번 실행해서 5번 성공하면 대기실 100석일때는 50%  
100 대신 150 50 등등 변경해 진행시 그에 따른 확률을 구할 수 있다.

### HamburgerSim.c
```
#include <stdio.h>
#include <stdlib.h> // srand()
#include <time.h>   // time(NULL)
#include "CircularQueue.h"

#define	CUS_COME_TERM	15		// 고객의 주문 간격: 초 단위

#define CHE_BUR		0		// 치즈버거 상수 
#define BUL_BUR		1		// 불고기버거 상수
#define DUB_BUR		2		// 더블버거 상수

#define CHE_TERM	12		// 치즈버거 제작 시간: 초 단위
#define BUL_TERM	15		// 불고기버거 제작 시간: 초 단위
#define DUB_TERM	24		// 더블버거 제작 시간: 초 단위

int main(void)
{
	int makeProc=0;			// 햄버거 제작 진행상황
	int cheOrder=0, bulOrder=0, dubOrder=0;
	int sec;

	Queue que;

	QueueInit(&que);
	srand(time(NULL)); 
    // rand()는 srand에 의존적
    // srand에서 seed값을 계속 바꿔주므로 rand는 랜덤값이 나옴

	// 아래 for문의 1회 회전은 1초의 시간 흐름을 의미함
	for(sec=0; sec<3600; sec++) // 1시간 반복
	{
		if(sec % CUS_COME_TERM == 0) 
		{
			switch(rand() % 3)
			{
			case CHE_BUR:
				Enqueue(&que, CHE_TERM);
				cheOrder += 1;
				break;

			case BUL_BUR:
				Enqueue(&que, BUL_TERM);
				bulOrder += 1;
				break;

			case DUB_BUR:
				Enqueue(&que, DUB_TERM);
				dubOrder += 1;
				break;
			}
		}
        //큐가 비어있지 않으면서 새로 만들 준비가 되면
		if(makeProc<=0 && !QIsEmpty(&que))
			makeProc = Dequeue(&que);

		makeProc--;
	}

	printf("Simulation Report! \n", QUE_LEN);
	printf(" - Cheese burger: %d \n", cheOrder);
	printf(" - Bulgogi burger: %d \n", bulOrder);
	printf(" - Double burger: %d \n", dubOrder);
	printf(" - Waiting room size: %d \n", QUE_LEN);
	return 0;
}
```