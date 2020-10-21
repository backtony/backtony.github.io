---
layout: post
title:  다이나믹 프로그래밍 기출문제
subtitle:   다이나믹 프로그래밍 기출문제
categories: algorithm
tags: a-intermediate book python class
comments: true
# header-img:
---
+ __목차__
  - [1. 간단 정리](#1-간단-정리)
  - [2. 금광](#2-금광)
  - [3. 정수 삼각형](#3-정수-삼각형) 
  - [4. 퇴사](#4-퇴사)
  - [5. 병사 배치하기](#5-병사-배치하기)
  - [6. 못생긴 수](#6-못생긴-수)
  - [7. 편집 거리](#7-편집-거리)

## 1. 간단 정리
---
### 다이나믹 프로그래밍
한 번 해결된 부분 문제의 정답을 메모리에 기록하여, 한 번 계산한 답은 다시 계산하지 않도록 하는 문제 해결 기법이다. 다이나믹 프로그래밍은 점화식을 그대로 코드로 옮겨서 구현할 수 있는데, 점화식이란 인접한 항들 사이의 관계식을 의미한다.
<br>

### 피보나치 수열
피보나치 수열 문제는 다이나믹 프로그래밍으로 해결할 수 있는 대표적인 문제이다. 한 번 계산한 i번째 피보나치 수는 모두 1차원 리스트에 저장해 놓았다가 나중에 해당 i번째 피보나치 수를 구해야 할 때, 이전 단계에서 계산된 값을 바로 반환한다.  
다이나믹 프로그래밍은 그 자체로도 다양한 문제로 출제될 수 있는 유형이지만, 그래프 이론 등 다양한 알고리즘에서도 자주 사용된다. 예를 들어 플로이드 워셜 알고리즘 또한 대표적인 다이나믹 프로그래밍을 활용한 알고리즘이다.
<br>

### 탑다운과 보텀업
다이나믹 프로그래밍을 이용한 소스코드를 작성하는 방법은 2가지가 있다. 탑 다운 방식은 재귀 함수를 이용하여 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식이다. 반면에 보텀업 방식은 단순히 반복문을 이용하여 작은 문제를 먼저 해결하고, 해결된 작은 문제를 모아 큰 문제를 해결하는 방식이다.
<br>

## 2. 금광
---
n * m 크기의 금광이 있다. 금광은 1 * 1크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다. 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다. 이후에는 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하시오.  
__입력 조건__  
+ 첫째 줄에 테스트 케이스 T가 입력된다 (1<= T <=1000)
+ 매 테스트 케이스 철째 줄에 n과 m이 공백으로 구분되어 입력된다. (1<=n,m<=20) 둘째 줄에 n * m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다. (1<= 각 위치에 매장된 금의 개수 <= 100)

__출력 조건__  
+ 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력한다. 각 테스트 케이스는 줄바꿈을 이용해 구분한다.

```
입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

출력 예시
19
16
```

### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

# 테스트 케이스 횟수
t = int(input())

# 위 오른쪽 아래
dx = [-1, 0, 1]
dy = [1, 1, 1]
for _ in range(t):
    n, m = map(int, input().split())
    answer = 0  # 총 캔 금광
    # 금광 그래프와 정보
    graph = [[] for _ in range(n)]
    golds = list(map(int, input().rstrip().split()))
    cnt = 0
    # 금광 그래프 완성시키기
    for i in range(n):
        for _ in range(m):
            graph[i].append(golds[cnt])
            cnt += 1

    # max를 못쓰는게 max인 위치의 좌표를 알아야해
    # 금광 그래프의 범위가 매우 작으므로 그냥 완전 탐색해도 될듯
    x = y = 0
    max_gold = graph[0][0]
    # 첫 시작 위치
    for i in range(1, n):
        if max_gold < graph[i][0]:
            x = i
            max_gold = graph[i][0]
    answer += max_gold
    # 이동 과정
    while x < n and y < m:
        max_gold = 0
        for i in range(3):
            px = x + dx[i]
            py = y + dy[i]
            # 범위 내일 경우
            if px < n and py < m:
                if max_gold < graph[px][py]:
                    ans_x = px
                    ans_y = py
                    max_gold = graph[px][py]
        x=ans_x
        y=ans_y
        answer += max_gold
        if y == m - 1:
            break
    print(answer)    
```

### 모범답안
이 문제는 2차원 테이블을 이용한 다이나믹 프로그래밍으로 해결할 수 있다. 금광의 모든 위치에 대하여 왼쪽 위에서 오는 경우, 왼쪽 아래에서 오는 경우, 왼쪽에서 오는 경우의 3가지 경우만 존재한다. 따라서 3 가지 경우 중에서 가장 많은 금을 가지고 있는 경우를 테이블에 저장해주어 문제를 해결할 수 있다. 내가 작성한 코드는 다이나믹 프로그래밍이라기 보다는 완전 탐색에 가까웠다. 여기서는 다이나믹 프로그래밍으로 코딩한다. 모든 경우를 확인하며 그 결과값을 저장해두고 나중에 다시 사용한다. 여기서 핵심은 리스트의 범위에 따라 경우를 나눠야 한다는 점이다.  
점화식은 dp[i][j] = arry[i][j] + max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1]) 이다.  
```python
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    # 0열이 아니라 1열부터 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
```
<br>

## 3. 정수 삼각형
---
[문제 클릭](https://www.acmicpc.net/problem/1932){: target="_blank"}  

### 내가 작성한 코드
```python
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
table = [[] for _ in range(n)]

# 그래프 대입
for i in range(n):
    graph[i]=list(map(int,input().rstrip().split()))

# 탑다운 방식
table[0]=graph[0]
for i in range(1,n):
    for j in range(i+1):
        if j-1<0:
            ans = graph[i][j] + table[i - 1][j]
            table[i].append(ans)
        elif j==i:
            ans = graph[i][j] + table[i - 1][j-1]
            table[i].append(ans)
        else:
            ans = graph[i][j] + max(table[i - 1][j - 1], table[i - 1][j])
            table[i].append(ans)

print(max(table[n-1]))
```

### 모범답안
특정한 위치로 도달하기 위해서는 왼쪽 위, 바로 위 2가지 위치에서만 내려올 수 있다. 따라서 모든 위치를 기준으로 이전 위치로 가능한 2가지 위치까지의 최적의 합 중에서 더 큰 합을 가지는 경우를 선택하면 된다. 이전 문제와 마찬가지로 범위에 따라 경우를 나눠야 한다.  
점화식은 dp[i][j] = drray[i][j] + max(dp[i-1][j-1],dp[i-1][j]) 이다.
```python
n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

for _ in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍으로 2번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))
```
<br>

## 4. 퇴사
---
[문제 클릭](https://www.acmicpc.net/problem/14501){: target="_blank"}  
### 내가 작성한 코드
```python
import sys
input = sys.stdin.readline

# 일할 수 있는 기간
n = int(input())

table = [0]*(n+1)
# 각 날짜의 상담에 해당하는 정보 입력
for i in range(1,n+1):
    day_cost, pay = map(int,input().rstrip().split())
    # 이전까지 벌어온 금액 처리
    if day_cost ==1:
        table[i]=max(table[i],pay)
    # day_cost가 들어오면 table의 자기 자리를 처리하지 못해
    # 그러므로 이전에 있던 것을 가져옴
    else :
        table[i]=max(table[i-1],table[i])
    # 퇴직하기 전이라면
    if day_cost+i-1<=n:
        # 오늘 이전까지 벌어온 금액중 최댓값 + 이제 할 상담의 금액
        sum_pay = pay + table[i-1]
        table[day_cost+i-1]=max(table[day_cost+i-1],sum_pay)

print(table[n])
```


### 모범답안
이 문제는 뒤쪽 날짜부터 거꾸로 확인하는 방식으로 접근하여 해결하는 다이나믹 프로그래밍의 아이디어를 떠올릴 수 있다. 거꾸로 계산하는 방식을 떠올릴 수 있는 이유는 끝이 확실히 정해지지 않았기 때문이다. 따라서 입력받은 것을 토대로 끝을 확인한 다음 끝에서부터 시작하는 것이다.  
예시를 기준으로 생각해보자. 1일 차에 상담을 진행한다고 해보자. 이 경우 3일에 걸쳐 상담을 진행해야 한다. 결과적으로 4일부터 다시 상담을 진행할 수 있다. 그러므로 1일 차에 상담을 진행하는 경우, 최대 이익은ㅇ 1일차 부터의 상담 금액 + 4일부터의 최대 상담 금액이 된다. 따라서 이러한 원리를 이용하여 뒤쪽 날짜부터 거꾸로 계산하며 문제를 해결할 수 있다. 즉, 뒤쪽부터 매 상담에 대하여 현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤 (dp[t[i] + i])를 계산하면 된다. 이후에 계산된 각각의 값 중에서 최댓값을 출력하면 된다.  
dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익이라고 하면 점화식은 dp[i] = max(p[i] + dp[t[i]+i],max_value)가 된다. 이때 max_value는 뒤에서부터 계산할 때, 현재까지의 최대 상담 금액에 해당하는 변수이다. 
```python
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
```
<br>

## 5. 병사 배치하기
---
[문제 클릭](https://www.acmicpc.net/problem/18353){: target="_blank"}  

### 모범답안
이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같다. 가장 긴 증가하는 부분 수열 문제란 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제이다.  
예를 들어 하나의 수열 array = [10,20,10,30,20,50]이 있다고 하자. 이때 가장 긴 증가하는 부분 수열은 {10,20,30,50}이 될 것이다. d[i]=array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이라고 정의하면, 가장 긴 증가하는 부분 수열을 계산하는 점화식은 다음과 같다. 이때 __초기의 dp 테이블의 값은 자기 자신을 수열의 개수로 카운트 한다는 의미로 모두 1로 초기화한다.__ 모든 0 <= j < i 에 대하여, d[i] = max(d[i],d[j]+1) if array[j] < array[i], 풀어서 말하면, 현재 위치 i보다 작은 0부터 i-1까지의 리스트값을 비교하여 i리스트값이 더 큰 경우 dp를 max를 통해 갱신한다는 것이다. 결과적으로 테이블에 남아있는 값 중에서 가장 큰 값이 가장 긴 증가하는 부분 수열의 길이가 된다.  
이러한 방식을 문제에 적용해보자. 현재 문제는 병사를 배치할 때 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치를 하고자 한다. 따라서 이 문제를 가장 긴 감소하는 부분 수열의 길이를 계산하는 문제로 간주하고, 입력으로 주어진 원소의 순서를 뒤집은 뒤 가장 긴 증가하는 부분 수열 문제를 풀 때의 점화식을 그대로 적용하면 풀 수 있다.  
정리하자면, 문제는 감소하는 수열의 최대 길이를 구하는 것이므로 받은 입력을 뒤집어서 증가하는 수열의 최대 길이를 구하는 것과 같은 문제이다.
```python
import sys

input = sys.stdin.readline

n = int(input())
table = list(map(int,input().rstrip().split()))
table = table[::-1]
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if table[j] < table[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
```
<br>

## 6. 못생긴 수
---
못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미한다. 다시 말해 오직 2, 3, 5를 약수로 가지는 합성수를 말한다. 1은 못생긴 수라고 가정한다. 따라서 못생긴 수들은 {1,2,3,4,5,6,8,9,10,12,15..}순으로 이어지게 된다. 이때, n번째 못생긴 수를 찾는 프로그램을 작성하시오.  
__입력 조건__  
+ 첫째 줄에 n이 입력된다. (1<=n<=1000)

__출력 조건__  
+ n번째 못생긴 수를 출력한다.

```
입력 예시
10
출력예시
12
입력예시
4
출력예시
4
```


### 내가 작성한 코드
```python
import sys

input = sys.stdin.readline

# 각 수의 약수를 늘어놓고 못생긴 수에 저장되어 있는지 확인하면 될듯
# in을 집합에다가 쓰면 매우 빠르게 동작한다.
n = int(input())
ugly = {1}
i = 2
cnt = 1
while cnt <= n:
    answer = True
    for j in range(1, i):
        # 약수 판별
        # 애초에 약수중에 자신을 제외한 수가 ugly에 없다면 그건 ugly가 아님
        if i % j == 0 and j not in ugly:
            answer = False
            break

    # 자신 판별 -> 소인수로 나눠지지 않거나 나눠진 몫이 못생긴수가 아니면 ugly가아님
    if answer:
        if i%2 ==0 or i%3==0 or i%5==0:
            if i//2 in ugly or i//3 in ugly or i//5 in ugly:
                answer = True
            else :
                answer = False
        else :
            answer = False
    if answer:
        ugly.add(i)
        cnt += 1
    i += 1

# 인덱싱을 위해 list로 변환
ugly = list(ugly)
print(ugly[n - 1])
```
in을 집합자료형에서 사용할 경우 평균적으로 O(1)의 복잡도를 보이기 때문에 리스트보다는 집합자료형을 사용했다.

### 모범답안
이 문제는 못생긴 수를 앞에서부터 하나씩 찾는 방법으로 해결할 수 있다. 못생긴 수들은 끊임없이 존재하는데 이때 못생긴 수에 2,3,5를 곱한 수도 또한 못생긴 수에 해당한다는 점이 포인트이다.
```python
n = int(input())

ugly = [0] * n # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
ugly[0] = 1 # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배한 인덱스의 위치
i2 = i3 = i5 = 0
# 2,3,5를 곱한 결과값
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수들을 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    # 여기서 이해가 조금 어려웠는데 처음부터 예시를 들어보면
    # ugly[1]=2가 될 것이고 첫번째 if문이 실행되어 i2=1이 되고 next2값이 변경된다.
    # 즉, ugly의 1번 인덱스는 2배처리를 완료했다는 것이고, 다음에는 인덱스2의 값을 2배처리.. ~~ 하는 것이다.
    # 그럼 1번 인덱스는 이제 3,5배처리를 해야할텐데 그 동작은 제일 작은 것으로 선택될때 수행된다.    
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n - 1])
```
<br>

## 7. 편집 거리
---
두 개의 문자열 A와 B가 주어졌을 때, 문자열 A를 편집하여 문자열 B로 만들고자 한다. 문자열 A를 편집할 때는 다음 세 연산 중에서 한 번에 하나씩 선택하여 이용할 수 있다.  
+ 삽입 : 특정한 위치에 하나의 문자를 삽입한다.
+ 삭제 : 특정한 위치에 있는 하나의 문자를 삭제한다.
+ 교체 : 특정한 위치에 있는 하나의 문자를 다른 문자로 교체한다.

이때 편집 거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미한다. 문자열 A를 문자열 B로 만드는 최소 편집 거리를 계산하는 프로그램을 작성하세요. 예를 들어 sunday와 saturday의 최소 편집 거리는 3이다.  
__입력 조건__  
+ 두 문자열 A와 B가 한 줄에 하나씩 주어진다.
+ 각 문자열은 영문 알파벳으로만 구성되어 있으며, 각 문자열의 길이는 1보다 크거나 같고, 5,000보다 작거나 같다.

__출력 조건__  
+ 최소 편집 거리 출력

```
입력 예시
cat
cut

출력예시
1

입력예시
sunday
saturday

출력예시
3
```


### 모범답안
이 문제는 최소 편집 거리를 담을 2차원 테이블을 초기화한 뒤에, 최소 편집 거리를 계싼해 테이블에 저장하는 과정으로 문제를 해결할 수 있다. 점화식은 다음과 같다.  

```python

```
<br>

---
__본 포스팅은 '이것이 코딩 테스트다 with 파이썬'을 읽고 공부한 내용을 바탕으로 작성하였습니다.__
