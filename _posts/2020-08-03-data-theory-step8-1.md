---
layout: post
title:  트리(Tree)
subtitle: 트리(Tree)
categories: data
tags: theory book datastructure tree 트리
comments: true
# header-img:
---
+ __목차__
  - [1. 트리의 개요](#1-트리의-개요)
  - [2. 이진 트리의 구현](#2-이진-트리의-구현)


## 1. 트리의 개요
---
### 트리 관련 용어의 소개
![그림1](https://backtony.github.io/assets/img/post/data/step8/1.PNG)

+ 노드 : node
    - 트리의 구성요소에 해당하는 A, B, C, D, E, F와 같은 요소
+ 간선 : edge
    - 노드와 노드를 연결하는 연결선
+ 루트 노트 : root node
    - 트리 구조에서 최상위에 존재하는 A와 같은 노드
+ 단말 노드 : terminal node
    - 아래로 또 다른 노드가 연결되어 있지 않은 E, F, C, D와 같은 노드
+ 내부 노드 : internal node
    - 단말 노드를 제외한 모든 노드로 A, B와 같은 노드

### 트리의 노드간 관계
![그림2](https://backtony.github.io/assets/img/post/data/step8/2.PNG)

+ 노드 A는 노드 B,C,D의 부모 노드이다.
+ 노드 B, C, D는 노드 A의 자식 노드이다.
+ 노드 B, C, D는 부모 노드가 같으므로 서로가 서로에게 형제 노드이다.  

### 서브 트리의 이해
![그림3](https://backtony.github.io/assets/img/post/data/step8/3.PNG)

+ 서브트리 역시 서브 트리로 이뤄져 있으며, 그 서브 트리 역시 또 다른 서브 트리로 이뤄져 있다. => 재귀적이다.  

### 이진 트리의 이해
![그림4](https://backtony.github.io/assets/img/post/data/step8/4.PNG)

+ 이진 트리의 조건
    - 루트 노드를 중심으로 두 개의 서브 트리로 나뉜다.
    - 나뉘어진 두 서브 트리도 모두 이진 트리이어야 한다.

__cf) 조건에 따르면 D와 E도 이진 트리인가?__  
![그림5](https://backtony.github.io/assets/img/post/data/step8/5.PNG)

보이지 않는 공집합 노드가 존재하기 때문에 이진 트리라고 인지한다. 하나의 노드에 두 개의 노드가 달리는 형태의 트리는 모두 이진 트리이다.  

### 레벨과 높이, 그리고 포화, 완전 이진 트리
![그림6](https://backtony.github.io/assets/img/post/data/step8/6.PNG)

+ 트리의 높이와 레벨의 최대 값은 같다.
+ 레벨은 0부터 시작한다.

![그림7](https://backtony.github.io/assets/img/post/data/step8/7.PNG)

+ 완전 이진 트리
    - 위에서 아래로, 왼쪽에서 오른쪽으로 채워진 트리를 의미한다.
    - 포화 이진 트리는 동시에 완전 이진 트리이지만 그 역은 성립하지 않는다.
    - 그림의 완전 이진 트리에서 I가 빠져도 완전 이진 트리 이다.

## 2. 이진 트리의 구현
---
### 이진 트리 구현의 두 가지 방법
![그림8](https://backtony.github.io/assets/img/post/data/step8/8.PNG)

+ 노드에 번호를 부여하고 그 번호에 해당하는 값을 배열의 인덱스 값으로 활용한다.
+ 편의상 배열의 첫 번째 요소는 사용하지 않는다.

![그림9](https://backtony.github.io/assets/img/post/data/step8/9.PNG)

+ 연결 리스트 기반에서는 트리의 구조와 리스트의 연결 구조가 일치한다.
+ 따라서 구현과 관련된 직관적인 이해가 배열 기반보다 더 좋다.

### 이진 트리 자료구조의 ADT
+ BTreeNode* MakeBTreeNode(void)
    - 이진 트리 노드를 생성하여 그 주소 값을 반환
+ BTData GetData(BTreeNode* bt);
    - 노드에 저장된 데이터 반환
+ void SetData(BTreeNode* bt, BTData data);
    - data로 전달된 값을 노드 데이터에 저장
+ BTreeNode* GetLeftSubTree(BTreeNode* bt);
    - 왼쪽 서브 트리의 주소값을 반환
+ BTreeNode* GetRightSubTree(BTreeNode* bt);
    - 오른쪽 서브 트리의 주소값을 반환
+ void MakeLeftSubTree(BTreeNode* main, BTreeNode* sub);
    - 왼쪽 서브 트리를 연결
+ void MakeRightSubTree(BTreeNode* main, BTreeNode* sub);
    - 오른쪽 서브 트리를 연결
+ void DeleteTree(BTreeNode* bt);
    - 재귀를 이용한 데이터 삭제
+ void PreorderTraverse(BTreeNode* bt, VisitFuncPtr action);
    - 방문목적에 따른 전위 순회
+ void InorderTraverse(BTreeNode* bt, VisitFuncPtr action);
    - 방문목적에 따른 중위 순회
+ void PostorderTraverse(BTreeNode* bt, VisitFuncPtr action);
    - 방문목적에 따른 후위 순회


### 순회의 재귀적 표현
![그림10](https://backtony.github.io/assets/img/post/data/step8/10.PNG)

+ 위에서부터 중위 순회, 후위 순회, 전위 순회이다.
+ 기준은 루트 노드를 언제 방문하느냐에 있다.

__어떻게 재귀적으로 코딩할까?__  
중위 순회를 예를 들어보자.  
1. 재귀함수를 사용할지 파악 => 쪼개서 봐도 계속 이진 트리가 존재
2. 그림을 크게 본다.
    - 전체가 중위 순회를 해야 한다.
    - 루트 노드의 왼쪽 서브 트리도 중위 순회 해야 한다.
    - 루트 노드의 오른쪽 서브 트리도 중위 순회 해야 한다.
3. 중위 순회 함수만들고 내부 채우기
    - 중위 순회이므로 왼쪽부터 => 왼쪽 중위 순회 함수 호출
    - 함수 인자가 NULL이면 return 으로 돌아옴
    - 노드가 딱 3개라고 했을때 지금 bt는 루트노드의 왼쪽 노드 
    - 오른쪽 중위 순회 함수 호출

```
void InorderTraverse(BTreeNode *bt)
{
    if(bt==NULL) return;
    InorderTraverse(bt->left);
    printf("%d\n",bt->data);
    InorderTraverse(bt->right);
}
```
후위 순회와 전위 순회는 그저 코딩의 위치 순서만 바꿔주면 된다.

### 노드 방문 이유 자유롭게 구성하기
바로 위에서 순회를 통해서 각 노드를 방문하고 데이터를 출력했다. 하지만 노드 방문목적은 여러개가 될 수 있다. 따라서 그 방문목적을 변경할 수 있도록 해보자.
```
typedef void (*VisitFuncPtr)(int data);
void InorderTraverse(BTreeNode *bt,VisitFuncPtr action)
{
    if(bt==NULL) return;
    InorderTraverse(bt->left);
    action(bt->data);
    InorderTraverse(bt->right);
}
```
__cf) typedef 함수 포인터__  
함수 포인터 선언시 int (*fp)(int,int) 같이 일일이 반환값 자료형과 매개변수 자료형 명시해서 선언했다. 하지만 typedef 함수포인터 선언시 포인터명을 자료형처럼 사용할 수 있다.
```
typedef int(*fp)(int,int);
int(*fp)(int,int);
int(*ps)(int,int); // 이렇게 여러번 선언해야할 것을 간소화 시켜준다.
fp another; // fp가 함수 포인터를 의미하는 자료형
fp ps; // ps, another 은 함수 포인터 변수명
```

### BinaryTree.h
```
#ifndef __BINARY_TREE_H__
#define __BINARY_TREE_H__

typedef int BTData;

typedef struct _bTreeNode
{
	BTData data;
	struct _bTreeNode* left;
	struct _bTreeNode* right;
}BTreeNode;

/*** BTreeNode 관련 연산들 ****/
BTreeNode* MakeBTreeNode(void);
BTData GetData(BTreeNode* bt);
void SetData(BTreeNode* bt, BTData data);

BTreeNode* GetLeftSubTree(BTreeNode* bt);
BTreeNode* GetRightSubTree(BTreeNode* bt);

void MakeLeftSubTree(BTreeNode* main, BTreeNode* sub);
void MakeRightSubTree(BTreeNode* main, BTreeNode* sub);

typedef void(*VisitFuncPtr)(BTData data);

void PreorderTraverse(BTreeNode* bt, VisitFuncPtr action);
void InorderTraverse(BTreeNode* bt, VisitFuncPtr action);
void PostorderTraverse(BTreeNode* bt, VisitFuncPtr action);

void DeleteTree(BTreeNode* bt);

#endif
```

### BinaryTree.c
```
#include <stdlib.h>
#include <stdio.h>
#include "BinaryTree.h"

BTreeNode* MakeBTreeNode(void)
{
	BTreeNode* newnode = (BTreeNode*)malloc(sizeof(BTreeNode));

	newnode->left = NULL;
	newnode->right = NULL;
	return newnode;
}

BTData GetData(BTreeNode* bt)
{
	return bt->data;
}
void SetData(BTreeNode* bt, BTData data)
{
	bt->data = data;
}

BTreeNode* GetLeftSubTree(BTreeNode* bt)
{
	return bt->left;
}
BTreeNode* GetRightSubTree(BTreeNode* bt)
{
	return bt->right;
}


void PreorderTraverse(BTreeNode* bt, VisitFuncPtr action)
{
	if (bt == NULL) return;
	action(bt->data);
	PreorderTraverse(bt->left, action);
	PreorderTraverse(bt->right, action);
}

void InorderTraverse(BTreeNode* bt, VisitFuncPtr action)
{
	if (bt == NULL) return;
	InorderTraverse(bt->left,action);
	action(bt->data);
	InorderTraverse(bt->right, action);
}

void PostorderTraverse(BTreeNode* bt, VisitFuncPtr action)
{
	if (bt == NULL) return;
	PostorderTraverse(bt->left, action);
	PostorderTraverse(bt->right, action);
	action(bt->data);
}

void MakeLeftSubTree(BTreeNode* main, BTreeNode* sub)
{
	if (main->left != NULL) free(main->left);	
	main->left = sub;
}
void MakeRightSubTree(BTreeNode* main, BTreeNode* sub)
{
	if (main->right != NULL) free(main->right);
	main->right = sub;
}
void DeleteTree(BTreeNode* bt)
{
	if (bt == NULL) return;
	DeleteTree(bt->left);
	DeleteTree(bt->right);	
	printf("Delete : %d\n", bt->data);
	free(bt); // 맨 마지막에 해야함. 중간에 삽입시 길을 잃음
}
```

### 활용한 메인 함수
```
#include <stdio.h>
#include "BinaryTree.h"

void ShowIntData(int data);

int main(void)
{
	BTreeNode* bt1 = MakeBTreeNode();
	BTreeNode* bt2 = MakeBTreeNode();
	BTreeNode* bt3 = MakeBTreeNode();
	BTreeNode* bt4 = MakeBTreeNode();
	BTreeNode* bt5 = MakeBTreeNode();
	BTreeNode* bt6 = MakeBTreeNode();

	SetData(bt1, 1);
	SetData(bt2, 2);
	SetData(bt3, 3);
	SetData(bt4, 4);
	SetData(bt5, 5);
	SetData(bt6, 6);

	MakeLeftSubTree(bt1, bt2);
	MakeRightSubTree(bt1, bt3);
	MakeLeftSubTree(bt2, bt4);
	MakeRightSubTree(bt2, bt5);
	MakeRightSubTree(bt3, bt6);

	PreorderTraverse(bt1, ShowIntData);
	printf("\n");
	InorderTraverse(bt1, ShowIntData);
	printf("\n");
	PostorderTraverse(bt1, ShowIntData);
	printf("\n");

	DeleteTree(bt1);
	return 0;
}

void ShowIntData(int data)
{
	printf("%d ", data);
}

```


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
