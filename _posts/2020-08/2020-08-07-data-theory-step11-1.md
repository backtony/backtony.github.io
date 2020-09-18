---
layout: post
title:  탐색 (Search) 1 이진 탐색 트리
subtitle: 탐색 (Search) 1 이진 탐색 트리
categories: data
tags: theory book datastructure search 탐색
comments: true
# header-img:
---
+ __목차__
  - [1. 탐색의 이해와 보간 탐색](#1-탐색의-이해와-보간-탐색)
  - [2. 이진 탐색 트리](#2-이진-탐색-트리)

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
이진 탐색 트리도 이진 트리이니 이전에 구현한 이진 트리에 기능을 몇 개 추가한 뒤 활용한다. 삽입과 탐색은 쉽기 때문에 코드에서 주석으로 설명하고 삭제만 따로 정리하겠다.
+ 삭제할 노드가 단말 노드인 경우
+ 삭제할 노드가 하나의 자식 노드(서브 트리)를 갖는 경우
+ 삭제할 노드가 두 개의 자식노드(서브 트리)를 갖는 경우

각 상황 별로 추가로 삭제할 노드가 루트 노드인 경우 구분해야 하지만 이를 피하기 위해 새로운 가상 루트 노드를 만들어 실제 루트 노드를 왼쪽이나 오른쪽 노드로 두어서 해결한다. 자세한 내용은 코드에서 주석으로 설명하겠다.  

__BinaryTree3.h 이진 트리에서 몇 가지 추가__  
```
#ifndef __BINARY_TREE3_H__
#define __BINARY_TREE3_H__

typedef int BTData;

typedef struct _bTreeNode
{
	BTData data;
	struct _bTreeNode * left;
	struct _bTreeNode * right;
} BTreeNode;

BTreeNode * MakeBTreeNode(void);
BTData GetData(BTreeNode * bt);
void SetData(BTreeNode * bt, BTData data);

BTreeNode * GetLeftSubTree(BTreeNode * bt);
BTreeNode * GetRightSubTree(BTreeNode * bt);

void MakeLeftSubTree(BTreeNode * main, BTreeNode * sub);
void MakeRightSubTree(BTreeNode * main, BTreeNode * sub);

typedef void VisitFuncPtr(BTData data);

void PreorderTraverse(BTreeNode * bt, VisitFuncPtr action);
void InorderTraverse(BTreeNode * bt, VisitFuncPtr action);
void PostorderTraverse(BTreeNode * bt, VisitFuncPtr action);

// 여기서부터 이진 탐색에서 추가한 함수//

// 왼쪽 자식 노드 제거, 제거된 노드의 주소 값이 반환된다.
BTreeNode * RemoveLeftSubTree(BTreeNode * bt);

// 오른쪽 자식 노드 제거, 제거된 노드의 주소 값이 반환된다.
BTreeNode * RemoveRightSubTree(BTreeNode * bt);

// 메모리 소멸을 수반하지 않고 main의 왼쪽 자식 노드를 변경한다. 
void ChangeLeftSubTree(BTreeNode * main, BTreeNode * sub);

// 메모리 소멸을 수반하지 않고 main의 오른쪽 자식 노드를 변경한다. 
void ChangeRightSubTree(BTreeNode * main, BTreeNode * sub);

#endif
```  
__BinaryTree3.c__  
```
#include <stdio.h>
#include <stdlib.h>
#include "BinaryTree3.h"

BTreeNode * MakeBTreeNode(void)
{
	BTreeNode * nd = (BTreeNode*)malloc(sizeof(BTreeNode));

	nd->left = NULL;
	nd->right = NULL;
	return nd;
}

BTData GetData(BTreeNode * bt)
{
	return bt->data;
}

void SetData(BTreeNode * bt, BTData data)
{
	bt->data = data;
}

BTreeNode * GetLeftSubTree(BTreeNode * bt)
{
	return bt->left;
}

BTreeNode * GetRightSubTree(BTreeNode * bt)
{
	return bt->right;
}

void MakeLeftSubTree(BTreeNode * main, BTreeNode * sub)
{
	if(main->left != NULL)
		free(main->left);

	main->left = sub;
}

void MakeRightSubTree(BTreeNode * main, BTreeNode * sub)
{
	if(main->right != NULL)
		free(main->right);

	main->right = sub;
}

void PreorderTraverse(BTreeNode * bt, VisitFuncPtr action)
{
	if(bt == NULL)
		return;

	action(bt->data);
	PreorderTraverse(bt->left, action);
	PreorderTraverse(bt->right, action);
}

void InorderTraverse(BTreeNode * bt, VisitFuncPtr action)
{
	if(bt == NULL)
		return;

	InorderTraverse(bt->left, action);
	action(bt->data);
	InorderTraverse(bt->right, action);
}

void PostorderTraverse(BTreeNode * bt, VisitFuncPtr action)
{
	if(bt == NULL)
		return;

	PostorderTraverse(bt->left, action);
	PostorderTraverse(bt->right, action);
	action(bt->data);
}

BTreeNode * RemoveLeftSubTree(BTreeNode * bt)
{
	BTreeNode * delNode;

	if(bt != NULL) {
		delNode = bt->left;
		bt->left = NULL;
	}
	return delNode;
}

BTreeNode * RemoveRightSubTree(BTreeNode * bt)
{
	BTreeNode * delNode;

	if(bt != NULL) {
		delNode = bt->right;
		bt->right = NULL;
	}
	return delNode;
}

void ChangeLeftSubTree(BTreeNode * main, BTreeNode * sub) 
{
	main->left = sub;
}
 
void ChangeRightSubTree(BTreeNode * main, BTreeNode * sub)
{
	main->right = sub;
}
```
__BinarySearchTree2.h 이진 트리 활용하여 이진 탐색 트리__  
```
#ifndef __BINARY_SEARCH_TREE2_H__
#define __BINARY_SEARCH_TREE2_H__

#include "BinaryTree3.h"

typedef BTData	BSTData;

// 이진 탐색 트리의 생성 및 초기화
void BSTMakeAndInit(BTreeNode ** pRoot);

// 노드에 저장된 데이터 반환
BSTData BSTGetNodeData(BTreeNode * bst);

// 이진 탐색 트리를 대상으로 데이터 저장(노드의 생성과정 포함)
void BSTInsert(BTreeNode ** pRoot, BSTData data);

// 이진 탐색 트리를 대상으로 데이터 탐색
BTreeNode * BSTSearch(BTreeNode * bst, BSTData target);

// 트리에서 노드를 제거하고 제거된 노드의 주소 값을 반환한다. 
BTreeNode * BSTRemove(BTreeNode ** pRoot, BSTData target);

// 이진 탐색 트리에 저장된 모든 노드의 데이터를 출력한다.
void BSTShowAll(BTreeNode * bst);

#endif
```
__BinarySearchTree2.c__  
```
#include <stdio.h>
#include <stdlib.h>
#include "BinaryTree3.h"
#include "BinarySearchTree2.h"

// 이중포인터에 대한 복습
// 포인터 안에 저장된 주소값 안의 값을 바꾸고 싶은게 아니고
// 포인터가 가리키는 주소값을 바꾸고 싶은 것이므로 이중 포인터 사용 
// 포인터가 가리키는 주소값을 바꾸고 싶다 -> 이중포인터

void BSTMakeAndInit(BTreeNode ** pRoot)
{
	*pRoot = NULL;
}

BSTData BSTGetNodeData(BTreeNode * bst)
{
	return GetData(bst);
}

void BSTInsert(BTreeNode ** pRoot, BSTData data)
{
  // cNode로 넣을 위치를 찾음에 따라 pNode를 알 수 있게 코딩
  // pNode에 nNode 연결
	BTreeNode * pNode = NULL;    // parent node
	BTreeNode * cNode = *pRoot;    // current node
	BTreeNode * nNode = NULL;    // new node

	// 새로운 노드가 추가될 위치를 찾는다.
	while(cNode != NULL)
	{
		if(data == GetData(cNode))
			return;    // 키의 중복을 허용하지 않음

		pNode = cNode;

		if(GetData(cNode) > data)
			cNode = GetLeftSubTree(cNode);
		else
			cNode = GetRightSubTree(cNode);
	}
	
	// pNode의 서브 노드에 추가할 새 노드의 생성
	nNode = MakeBTreeNode();    // 새 노드의 생성
	SetData(nNode, data);    // 새 노드에 데이터 저장

	// pNode의 서브 노드에 새 노드를 추가
	if(pNode != NULL)    // 새 노드가 루트 노드가 아니라면,
	{
		if(data < GetData(pNode))
			MakeLeftSubTree(pNode, nNode);
		else
			MakeRightSubTree(pNode, nNode);
	}
	else    // 새 노드가 루트 노드라면,
	{
		*pRoot = nNode;
	}
}

BTreeNode * BSTSearch(BTreeNode * bst, BSTData target)
{
	BTreeNode * cNode = bst;    // current node
	BSTData cd;    // current data

	while(cNode != NULL)
	{
		cd = GetData(cNode);

		if(target == cd)
			return cNode;
		else if(target < cd)
			cNode = GetLeftSubTree(cNode);
		else
			cNode = GetRightSubTree(cNode);
	}

	return NULL;
}

BTreeNode * BSTRemove(BTreeNode ** pRoot, BSTData target)
{
	// 삭제 대상이 루트 노드인 경우를 별도로 고려해야 한다.
	// 가상 루트 노드를 만들어 그 오른쪽이 실제 루트 노드가 되도록 만듦.
	// 삭제과정이 끝나고 가상 루트 노드의 오른쪽이 가리키는 주소의 데이터값과 실제 
	BTreeNode * pVRoot = MakeBTreeNode();    // 가상 루트 노드;

	BTreeNode * pNode = pVRoot;    // parent node
	BTreeNode * cNode = *pRoot;    // current node
	BTreeNode * dNode;    // delete node

	// 실제 루트 노드를 pVRoot가 가리키는 노드의 오른쪽 서브 노드가 되게 한다.
	ChangeRightSubTree(pVRoot, *pRoot);
	
	// 삭제 대상을 저장한 노드 탐색
	// NULL 이외의 조건을 넣으면서 target을 찾으면 루프 벗어남
	while(cNode != NULL && GetData(cNode) != target)
	{
		pNode = cNode;

		if(target < GetData(cNode))
			cNode = GetLeftSubTree(cNode);
		else
			cNode = GetRightSubTree(cNode);
	}

	if(cNode == NULL)    // 삭제 대상이 존재하지 않는다면,
		return NULL;

	dNode = cNode;    // 삭제 대상을 dNode가 가리키게 한다.

	// 첫 번째 경우: 삭제할 노드가 단말 노드인 경우
	if(GetLeftSubTree(dNode) == NULL && GetRightSubTree(dNode) == NULL)
	{
		if(GetLeftSubTree(pNode) == dNode)
			RemoveLeftSubTree(pNode);
		else
			RemoveRightSubTree(pNode);
	}

	// 두 번째 경우: 하나의 자식 노드를 갖는 경우
	// 첫 번째 경우에서 양쪽이 널인 경우를 제외시켜줬음
	else if(GetLeftSubTree(dNode) == NULL || GetRightSubTree(dNode) == NULL)
	{
		BTreeNode * dcNode;    // delete node의 자식 노드

		if(GetLeftSubTree(dNode) != NULL)
			dcNode = GetLeftSubTree(dNode);
		else
			dcNode = GetRightSubTree(dNode);

		if(GetLeftSubTree(pNode) == dNode)
			ChangeLeftSubTree(pNode, dcNode);
		else
			ChangeRightSubTree(pNode, dcNode);
	}

	// 세 번째 경우: 두 개의 자식 노드를 모두 갖는 경우
	else
	{
		// 삭제하는 것의 대체체는 오른쪽 서브트리의 맨 왼쪽 노드 or 왼쪽 서브트리의 제일 오른쪽 노드
		// 여기서는 오른쪽을 선택하겠다.
		BTreeNode * mNode = GetRightSubTree(dNode);    // mininum node
		BTreeNode * mpNode = dNode;    // mininum node의 부모 노드
		int delData;

		// 삭제할 노드를 대체할 노드를 찾는다.
		// 삭제노드의 오른쪽 노드로 왔으니 이제 왼쪽으로 이동하면서 제일 작은거 찾기
		while(GetLeftSubTree(mNode) != NULL)
		{
			mpNode = mNode;
			mNode = GetLeftSubTree(mNode);
		}
		
		// 삭제할 노드 위치에 대체체로 덮어씌우기
		delData = GetData(dNode);    // 대입 전 데이터 백업
		SetData(dNode, GetData(mNode));

		// 대체제 노드의 부모 노드와 대체제 자식 노드를 연결한다.
		// 이때 대체체 노드가 자식노드가 있다면 무조건 오른쪽 노드만 있음
		// 왼쪽이 있다면 최소가 아니기 때문
		if(GetLeftSubTree(mpNode) == mNode) 
			ChangeLeftSubTree(mpNode, GetRightSubTree(mNode));
		else // dNode 오른쪽 노드가 바로 대체제에 해당할때
			ChangeRightSubTree(mpNode, GetRightSubTree(mNode));

		dNode = mNode; 
		// 결국 삭제 자리의 노드에는 데이터가 덮어씌워지고 
		// 대체체의 노드가 사라지는 것
		SetData(dNode, delData);    // 백업 데이터 복원
	}

	// 삭제된 노드가 루트 노드라면 pVRoot의 오른쪽 노드 주소값이 변경되었을것임
	if(GetRightSubTree(pVRoot) != *pRoot) // 원래 가리키던 주소값이 아니라면
		*pRoot = GetRightSubTree(pVRoot); // 루트 노드의 주소값을 변경

	free(pVRoot); // 가상 루트 노드 반환
	return dNode;
}

void ShowIntData(int data)
{
	printf("%d ", data);
}

void BSTShowAll(BTreeNode * bst)
{
	InorderTraverse(bst, ShowIntData);
}
```
__BinarySearchTreeDelMain.c // 활용__  
```
#include <stdio.h>
#include <stdlib.h>
#include "BinarySearchTree2.h"

int main(void)
{
	BTreeNode * bstRoot;
	BTreeNode * sNode;    // search node

	BSTMakeAndInit(&bstRoot);

	BSTInsert(&bstRoot, 5);
	BSTInsert(&bstRoot, 8);
	BSTInsert(&bstRoot, 1);
	BSTInsert(&bstRoot, 6);
	BSTInsert(&bstRoot, 4);
	BSTInsert(&bstRoot, 9);
	BSTInsert(&bstRoot, 3);
	BSTInsert(&bstRoot, 2);
	BSTInsert(&bstRoot, 7);

	BSTShowAll(bstRoot); printf("\n");
	sNode = BSTRemove(&bstRoot, 3);
	free(sNode);

	BSTShowAll(bstRoot); printf("\n");
	sNode = BSTRemove(&bstRoot, 8);
	free(sNode);

	BSTShowAll(bstRoot); printf("\n");
	sNode = BSTRemove(&bstRoot, 1);
	free(sNode);

	BSTShowAll(bstRoot); printf("\n");
	sNode = BSTRemove(&bstRoot, 6);
	free(sNode);

	BSTShowAll(bstRoot); printf("\n");
	return 0;
}
```

---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__