---
layout: post
title:  (Question 8-1) 중위 표기법의 소괄호
subtitle: (Question 8-1) 중위 표기법의 소괄호
categories: data
tags: question book datastructure tree 트리
comments: true
# header-img:
---
## 문제
---
+ 3 + 2 * 7
+ 3 + ( 2 * 7)
+ (3 + (2 * 7 ) )

이 수식 트리에 담긴 수식을 중위 표기법의 수식으로 출력하라.(세 번째 수식 트리를 이용하자) 세 번째를 이용하는 이유는 연산자의 수와 소괄호 한쌍의 수가 일치하기 때문이다.  

## 풀이
---
[[클릭](https://backtony.github.io/data/2020/08/03/data-theory-step8-2/)]에서 보인 Expression Tree.c의 ShowInfixTypeExp 함수를 수정하여 소괄호를 포함하는 중위 표기법의 수식을 출력하면 된다.  
```
void InorderTraverse(BTreeNode* bt, VisitFuncPtr action)
{
	if (bt == NULL) return;

	//왼쪽이나 오른쪽 노드가 존재하면 현재 노드는 연산자가 있는 노드임
	//연산자의 갯수와 괄호쌍의 갯수가 같음
	//괄호는 루트노트가 들어올때부터 생성 
	if (bt->left != NULL || bt->right != NULL) printf("( ");
	InorderTraverse(bt->left,action);
	action(bt->data);
	InorderTraverse(bt->right, action);
	// 다 끝났으면 괄호 닫아줘야지
	if (bt->left != NULL || bt->right != NULL) printf(") ");

}
```

---
__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__