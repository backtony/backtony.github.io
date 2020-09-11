---
layout: post
title:  알고리즘 정리
subtitle:   알고리즘 정리
categories: algorithm
tags: a-basics book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 개요](#1-개요)
  - [2. 서로소 집합](#2-서로소-집합)
  - [3. 신장 트리와 크루스칼 알고리즘](#3-신장-트리와-크루스칼-알고리즘) 
  - [4. 위상 정렬](#4-위상-정렬)
  - [5. 실전 문제](#5-실전-문제)


## 1. 개요
---
지금까지 포스팅한 파이썬 알고리즘을 정리하는 포스팅이다. 모든 내용을 정리하진 않고, 복습하면서 기억이 나지 않는 부분과 빠르게 정리하고 싶을 때 참고할 내용 정도만 정리했다. 자세한 내용을 확인하고 싶다면 각 제목을 클릭하도록 하자. 각 제목을 클릭하면 해당 포스팅으로 이동하도록 링크를 걸어두었다.  
<br>

## [2. 주요 라이브러리의 문법과 유의점](https://backtony.github.io/algorithm/2020/08/31/algorithm-basics-coding-1/){:target="_blank"}
---
+ itertools의 permutations와 combinations는 클래스이므로 사용시 list로 형변환해서 사용한다.
+ bisect_left, bisect_right을 이용하면 이진 탐색을 쉽게 구현할 수 있다.
+ collections 라이브러리의 Counter은 인자로 이터레이터가 들어오는데 예시로 리스트가 온 경우 a = Counter([리스트])와 같이 변수로 받아서 사용할 때는 a['찾을것']과 같이 변수 뒤에 ['찾고자하는 내용']으로 사용시 개수가 반환된다.
<br>

## [3. 복잡도](https://backtony.github.io/algorithm/2020/08/31/algorithm-basics-coding-2/){:target="_blank"}
---
#### 알고리즘 설계시 주의사항
__시간 복잡도__  
+ N의 범위가 100,000이라면 O(NlogN)으로 풀이 가능  
+ N의 범위가 10,000,000이라면 O(N)으로 풀이 가능  

__공간 복잡도__  
+ 데이터의 단위가 1,0000만 단위가 넘어가지 않도록 알고리즘 설계  

__알고리즘 소요 시간 체크__  
```python
import time
start = time.time()
end = time.time()
print(end-start)
```
<br>

## [4. 기초 기타 알고리즘](https://backtony.github.io/algorithm/2020/09/01/algorithm-basics-coding-3/){:target="_blank"}
---
### 에라토스테네스의 체
__소수 판별에 사용하는 알고리즘__  
1. N+1 크기의 리스트를 True로 초기화
  - 인덱스 0과 1은 False로 수정
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 선택
3. 남은 수 중에서 i를 제외한 i의 모든 배수 제거
4. for문을 사용하여 2부터 (n의 제곱근+1)까지 2,3과정을 반복
  - 제곱근 이후에는 2 * 8, 8 * 2처럼 중복이 발생하기 때문

<br>

### 투 포인터
리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘  

#### 특정한 합(M)을 가지는 부분 연속 수열 찾기
1. 시작점과 끝점이 첫 번째 원소의 인덱스 0을 가리키도록 한다.
2. 현재 부분합이 M과 같다면 count+=1
3. 현재 부분합이 M보다 작으면 end를 1 증가
4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가
5. start가 리스트 끝까지 갈때까지 위 과정 반복

#### 이미 정렬된 두 리스트 합치기
1. 이미 정렬된 리스트 A와 B를 받는다.
2. 리스트 A, B에서 처리되지 않은 원소 중 가장 작은 원소를 i, j
3. A[i]와 B[j] 중에서 더 작은 원소를 결과 리스트에 append
4. 처리된 리스트의 인덱스 +1
5. 리스트 A, B에 더이상 처리할 원소가 없을 때까지 위 과정 반복

#### 여러 쿼리의 구간 합 계산
몇 개 안되는 쿼리만 구한다면 단순히 계산하면 되지만 여러 개의 쿼리가 존재한다면 각 쿼리[left,right]에 대해서 구간 합을 빠르게 구하기 위해서는 리스트 맨 앞부터 특정 위치까지의 합을 미리 구해놓는 것이 좋다.  
1. N개의 수에 대하여 해당 인덱스까지의 누적 합을 계산하여 배열 P에 저장한다.
2. 매 M개의 쿼리 정보 [L,R]을 확인할 때, 구간 합은 P[R]-P[L-1]

<br>

## [5. 그리디 알고리즘](https://backtony.github.io/algorithm/2020/09/01/algorithm-basics-coding-4/){:target="_blank"}
---
현재 상황에서 나중을 고려하지 않고 지금 당장 좋은 것만 고르는 알고리즘  
문제에서 가장 큰 순서대로, 가장 작은 순서대로와 같이 간단한 기준을 제시해주며, 정렬 알고리즘과 짝지어 출제된다.  
+ 거스름돈 유형이 대표적인 그리디 알고리즘인데 이때 제시된 큰 거스름돈들은 자신보다 작은 거스름돈들(모두)의 배수여야 한다.  
+ 주어진 수 중에서 m번 더해서 가장 큰수를 만들고 연속으로 k번을 초과해서 더할 수 없는 문제
  - 일일이 다 더하기 보다는 규칙을 확인해서 한 번에 처리한다.
  - m//(k+1) 만큼 규칙적으로 묶을 수 있는 부분은 한 번에 처리하고 m%(k+1)도 한 번에 처리하는 것이 좋은 풀이
+ N이 1이 될때까지 1빼기 연산과 k로 나누기 연산하기
  - 나누기 연산을 한 번에 할 수있는 특별한 방법이 없지만 빼기 연산은 N%K를 통해 나머지를 한 번에 빼면서 처리

<br>

## [6. 완전탐색, 시뮬레이션](https://backtony.github.io/algorithm/2020/09/02/algorithm-basics-coding-5/){:target="_blank"}
---
+ 완전 탐색 : 모든 경우의 수를 다 계산하는 방법
+ 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 방법

완전 탐색과 시뮬레이션 문제는 대부분 이동에 관련된 문제가 많다.  
+ 방향 경로에 따라 dx, dy 리스트를 만들어 활용하는 것이 좋다. 필요하다면 방향도 리스트로 만들어 for문을 돌리면서 입력된 방향과 일치하는 경우 px, py로 사전에 x,y의 이동 후 경로를 확인하고 조건에 따라 이동 여부를 확인하는데 사용하는 것도 좋은 방법이다.  
+ dx와 dy 중 하나는 일정한 거리만큼 이동하는데 하나는 +a도 가능하고 -a도 가능한 경우에는 step 리스트를 따로 만들어 모든 경우의수를 step[[2,1],[2,-1]]같이 만들어서 활용하자.  


대체로 완전탐색과 시뮬레이션 문제는 문제의 길이가 긴편이고 코드도 긴 편이다. 따라서 pypy3를 선택하도록 하고 메모리 제한이 있으므로 1,000만 이상의 리스트는 사용하지 않도록 하자.  
<br>

## [6. DFS/BFS](https://backtony.github.io/algorithm/2020/09/03/algorithm-basics-coding-6/){:target="_blank"}
---

<br>

## [7. 정렬](https://backtony.github.io/algorithm/2020/09/04/algorithm-basics-coding-7/){:target="_blank"}
---

<br>

## [8. 이진 탐색](https://backtony.github.io/algorithm/2020/09/05/algorithm-basics-coding-8/){:target="_blank"}
---

<br>

## [9. 다이나믹 프로그래밍](https://backtony.github.io/algorithm/2020/09/06/algorithm-basics-coding-9/){:target="_blank"}
---

<br>

## [10. 최단 경로](https://backtony.github.io/algorithm/2020/09/07/algorithm-basics-coding-10/){:target="_blank"}
---

<br>

## [11. 그래프 이론](https://backtony.github.io/algorithm/2020/09/09/algorithm-basics-coding-11/){:target="_blank"}
---