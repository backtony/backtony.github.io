---
layout: post
title:  재귀(팩토리얼, 피보나치, 하노이 타워)
subtitle:   재귀(팩토리얼, 피보나치, 하노이 타워)
categories: data
tags: theory book datastructure 재귀 하노이타워 피보나치 팩토리얼
comments: true
# header-img:
---
+ __목차__
  - [1. 팩토리얼의 재귀적 구현](#1-팩토리얼의-재귀적-구현)
  - [2. 피보나치 수열](#2-피보나치-수열)
  - [3. 이진 탐색 알고리즘의 재귀구현](#3-이진-탐색-알고리즘의-재귀구현)
  - [4. 하노이 타워](#4-하노이-타워)

## 1. 팩토리얼의 재귀적 구현
---
```
int Factorial(int n)
{
    if (n==1) return 1;
    else return n * Factorial(n-1);
}
int main()
{
    printf("9! =%d\n", Factorial(9));
    return 0;
}
```  
<br>

## 2. 피보나치 수열
---
```
int Fibo(int n)
{
    if(n==1) return 0;
    else if(n==2) return 1;
    else return Fibo(n-1) + Fibo(n-2);
}
int main()
{
    int i;
    for(i=1; i<15; i++) printf("%d ",Fibo(i));
    return 0;
}
```
<br>

## 3. 이진 탐색 알고리즘의 재귀구현
---
```
int BSearchRecur(int ar[], int first, int last, int target)
{
    int mid;
    if (first > last) return -1;       // 역전시 반환값
    mid = (first+last)/2;
    if(ar[mid] < target)
    {
        BBSearchRecur(ar, mid+1, last, target);  // 뒷부분 대상으로 재 탐색
    }
    else if (ar[mid] > target)
    {
        BBSearchRecur(ar, first, mid -1, target); // 앞부분 대상으로 재 탐색
    }
    else return mid;
}
```
<br>

## 4. 하노이 타워
---
하노이 타워를 공부하기 앞서 기본적인 재귀를 살펴보았습니다. 위와 같은 재귀의 흐름은 간단하기 때문에 순서를 해석나가면서 그려갈 수 있지만, 하노이 타워처럼 복잡해질 경우에는 함수의 흐름을 따라가는 식으로 공부해서는 무의미합니다. 앞으로의 재귀에 관해서는 논리적 흐름만을 파악하고 코딩으로 구현해내는 정도만으로도 충분합니다.  

![그림1](https://backtony.github.io/assets/img/post/data/step2/1.PNG)

+ 제약사항
    - 원반은 한 번에 하나씩만 옮길 수 있습니다.
    - 옮기는 과정에서 작은 원반의 위에 큰 원반이 올려져서는 안됩니다.

+ 목적 : 원반 4개를 A에서 C로 이동
1. 작은 원반 3개를 A에서 B로 이동
2. 큰 원반 1개를 A에서 C로 이동
3. 작은 원반 3개를 B에서 C로 이동

작은 것 부터 1번 ~ 4번 이름을 붙이겠습니다. 단계적으로 생각해 봅시다.
1. 4번을 C에 놓기 위해서는 1~3번이 B로 이동해야합니다.
2. 그렇다면 1 ~ 3번이 B에 놓기 위해서는 3번이 제일 아래 와야하므로 먼저 1 ~ 2번이 C로 이동해야 합니다.
3. 그렇다면 1 ~ 2번이 C에 놓이기 위해서는 2번이 C의 제일 아래 와야하므로 1번이 B로 이동해야 합니다.

즉, 4개를 C로 옮기자니 먼저 위에 3개를 옮겨야하고 그 3개를 옮기자니 먼저 위에 있는 2개를 옮겨야하고 그 2개를 옮기자니 먼저 위에 있는 1개를 옮겨야하는 재귀적 논리가 생기게 됩니다.  
따라서, 모든것의 순서를 따라가기보다는 딱 처음의 4개 중 맨 아래것을 움직이기 위해서는 어떻게 해야할까 이후에는 똑같이 반복이므로 딱 처음의 경우와 탈출만을 고려해서 코딩하면 됩니다.

```
void Hanoi(int num, char from, char by, char to)
{
    if(num == 1)   // num이 1이면 위에 아무것도 없어서 치울게 없음
    {
        printf("1이 %c에서 %c로 이동",from,to);
    }
    else
    {
        Hanoi(n-1,from,to,by);  // num이 1이 아니면 위에 치울게 존재함
        printf("%d가 %c에서 %c로 이동",num,fromt,to); // 위에 다 치웠으면 아래 있던거 이동
        Hanoi(n-1,by,from,to);
        // 이번에는 위에서 맨 아래것을 움직이기 위해 치웠던것의 맨 아래것을 움직이기위한 함수
    }
}
int main()
{
    Hanoi(4,'a','b','c');
    return 0;
}
```
---

__본 포스팅은 '윤성우의 열혈 자료구조'를 읽고 공부한 내용을 바탕으로 작성하였습니다.__
