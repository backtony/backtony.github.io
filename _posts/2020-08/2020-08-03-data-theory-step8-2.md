---
layout: post
title:  수식 트리(Tree)
subtitle: 수식 트리(Tree)
categories: data
tags: theory book datastructure tree 트리
comments: true
# header-img:
---
+ __목차__
  - [1. 수식 트리의 이해](#1-수식-트리의-이해)
  - [2. 수식 트리 구성 방법](#2-수식-트리-구성-방법)
  - [3. 수식 트리의 구현](#3-수식-트리의-구현)

## 1. 수식 트리의 이해
---
![그림1](https://backtony.github.io/assets/img/post/data/step8/11.PNG)

+ 중위 표기법의 수식은 사람이 인식하기 좋으나 컴퓨터의 인식에는 어려움이 있다.
+ 그래서 컴파일러는 중위 표기법의 수식을 '수식 트리'로 재구성한다.
+ 수식 트리는 해석이 쉽고 연산의 과정에서 우선순위를 고려하지 않아도 된다.
+ 중위 표기법을 바로 수식 트리로 표현하는 것은 쉽지 않으나 후위 표기법의 수식으로 변경한 후 수식 트리로 표현하는 것은 어렵지 않다.

## 2. 수식 트리 구성 방법
---
![그림2](https://backtony.github.io/assets/img/post/data/step8/12.PNG)

피연산자는 노드에 넣은 후 스택으로 옮기로 연산자가 나오면 스택에 저장해 놓은 피연산자의 노드 주소값 두 개를 꺼내서 먼저 꺼낸 것이 오른쪽 나중에 꺼낸 것이 왼쪽으로 트리를 구성한다.  

![그림3](https://backtony.github.io/assets/img/post/data/step8/13.PNG)

형성된 트리는 다시 스택으로 옮기고 반복하면 최종 결과는 스택에 형성된다.


## 3. 수식 트리의 구현
---
### 관련 헤더 파일
트리 만드는 도구를 기반으로 함수를 정의한다.  
+ BTreeNode * MakeExpTree(char *exp);
    - 수식 트리 구성
    - 후위 표기법의 수식을 인자로 받아 수식 트리 구성 후 루트 노드의 주소값 반환
+ int EvaluateExpTree(BTreeNode *bt);
    - MakeExpTree가 구성한 수식 트리의 수식 계산 결과 반환
+ void ShowPrefixTypeExp(BTreeNode *bt);
    - 전위 표기법 기반 출력
+ void ShowInfixTypeExp(BTreeNode *bt);
    - 중위 표기법 기반 출력
+ void ShowPostfixTypeExp(BTreeNode *bt);
    - 후위 표기법 기반 출력

### 앞서 필요한 헤더, 소스파일
__ListBaseStack.h__  
```
#ifndef __LB_STACK_H__
#define __LB_STACK_H__

#include "BinaryTree.h"

#define TRUE	1
#define FALSE	0

// typedef int Data;
typedef BTreeNode* Data;

typedef struct _node
{
	Data data;
	struct _node* next;
} Node;

typedef struct _listStack
{
	Node* head;
} ListStack;


typedef ListStack Stack;

void StackInit(Stack* pstack);
int SIsEmpty(Stack* pstack);

void SPush(Stack* pstack, Data data);
Data SPop(Stack* pstack);
Data SPeek(Stack* pstack);

#endif
```
__ListBaseStack.c__  
```
#include <stdio.h>
#include <stdlib.h>
#include "ListBaseStack.h"

void StackInit(Stack* pstack)
{
	pstack->head = NULL;
}

int SIsEmpty(Stack* pstack)
{
	if (pstack->head == NULL)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack* pstack, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));

	newNode->data = data;
	newNode->next = pstack->head;

	pstack->head = newNode;
}

Data SPop(Stack* pstack)
{
	Data rdata;
	Node* rnode;

	if (SIsEmpty(pstack)) {
		printf("Stack Memory Error!");
		exit(-1);
	}

	rdata = pstack->head->data;
	rnode = pstack->head;

	pstack->head = pstack->head->next;
	free(rnode);

	return rdata;
}

Data SPeek(Stack* pstack)
{
	if (SIsEmpty(pstack)) {
		printf("Stack Memory Error!");
		exit(-1);
	}

	return pstack->head->data;
}
```
__BinaryTree.h__  
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
__BinaryTree.c__  
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
<br>

### 구현
__ExpressionTree.h__  
```
#ifndef __EXPRESSION_TREE_H__
#define __EXPRESSION_TREE_H__

#include "ListBaseStack.h"

BTreeNode* MakeExpTree(char* exp);
int EvaluateExpTree(BTreeNode* bt);

void ShowPrefixTypeExp(BTreeNode* bt);
void ShowInfixTypeExp(BTreeNode* bt);
void ShowPostfixTypeExp(BTreeNode* bt);

#endif
```
__ExpressionTree.c__  
```
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include "BinaryTree.h"
#include "ListBaseStack.h"

BTreeNode* MakeExpTree(char *exp)
{

	Stack stack;
	int Len = strlen(exp);
	int i;

	BTreeNode* pnode; // 트리 노드 주소 저장할곳

	StackInit(&stack);

	for (i = 0; i < Len; i++)
	{
		pnode = MakeBTreeNode(); // 트리 노드 하나 생성
		if (isdigit(exp[i]))
		{
			SetData(pnode, exp[i] - '0'); // 피연산자를 트리 노드에 저장
		}
		else
		{
			MakeRightSubTree(pnode, SPop(&stack)); // 먼저 꺼낸게 오른쪽
			MakeLeftSubTree(pnode, SPop(&stack));  // 나중에 꺼낸게 왼쪽
			SetData(pnode, exp[i]); // 연산자를 트리 노드에 저장
		}
		SPush(&stack, pnode); // 트리 노드를 스택에 저장
	}
	return SPop(&stack); // 최종 트리 리턴
}
int EvaluateExpTree(BTreeNode* bt)
{
	// 3개씩 잘라서 보면 다 똑같음, 왼쪽 오른쪽이 노드가 아니고 서브트리면?
	// 다시 함수에 넣으면 돼! => 재귀함수
	// 껍데기만 있는 수식 트리 계산 함수 만들고
	// 왼쪽 서브 트리도 수식 트리 계산함수 쓰고
	// 오른쪽 서브 트리도 수식 트리 계산함수 쓰고
	// 맨 위에 3개만 보면 결국 왼쪽 노드 오른쪽 노드는 상수
	int op1, op2;

	// 탈출 조건이 필요함
	// 수식 트리의 맨 아래 노드 => 단말노드 => 피연산자
	if (GetLeftSubTree(bt) == NULL && GetRightSubTree(bt) == NULL)
		return GetData(bt);
	op1 = EvaluateExpTree(GetLeftSubTree(bt));
	op2 = EvaluateExpTree(GetRightSubTree(bt));
	switch (GetData(bt))
	{
	case '+': return op1 + op2;
	case '-': return op1 - op2;
	case '*': return op1 * op2;
	case '/': return op1 / op2;
	}

}

void ShowNodeData(BTData data)
{
	if (data >= 0 && data <= 9) printf("%d ", data);
	else printf("%c ", data);
}

void ShowPrefixTypeExp(BTreeNode* bt)
{
	PreorderTraverse(bt, ShowNodeData);
}
void ShowInfixTypeExp(BTreeNode* bt)
{
	InorderTraverse(bt, ShowNodeData);
}
void ShowPostfixTypeExp(BTreeNode* bt)
{
	PostorderTraverse(bt, ShowNodeData);
}
```
__ExpressionMain.c // 활용__  
```
#include <stdio.h>
#include "ExpressionTree.h"

int main(void)
{
	char exp[] = "12+7*";
	BTreeNode* eTree = MakeExpTree(exp);

	printf("전위 표기법의 수식: ");
	ShowPrefixTypeExp(eTree); printf("\n");

	printf("중위 표기법의 수식: ");
	ShowInfixTypeExp(eTree); printf("\n");

	printf("후위 표기법의 수식: ");
	ShowPostfixTypeExp(eTree); printf("\n");

	printf("연산의 결과: %d \n", EvaluateExpTree(eTree));

	return 0;
}
```


---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__