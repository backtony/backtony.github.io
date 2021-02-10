---
layout: post
title: (Python) 백준 1043번 거짓말 - class 4
subtitle:   (Python) 백준 1043번 거짓말 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/1043){:target="_blank"}]


## 1043번 - 거짓말
---
__시행 착오__  
처음에는 파티의 순서에 따라 거짓말이 가능한 파티의 수가 달라질 것이라 생각해서 permutations를 사용해서 파티의 모든 순서를 고려했다. 그런데 다시 생각해보니 permutation로 딱 한번만 반복을 돌려버리면 뒤쪽에서 진실을 아는 사람이 추가되었을 때 그 사람이 만약 이미 검증을 완료한 앞의 파티도 참석했다면 거짓말이 가능한 파티 수에서 차감해줘야하는데 그 사람이 앞에 어느 파티에 속해있는지 찾으려면 다시 처음부터 돌려봐야한다. 결론적으로 파티의 순서가 의미가 없다.  
<br>

__풀이__  
모든 파티를 큐에 넣고 큐의 길이만큼 반복을 진행하면서 진실을 말해야하는 파티는 큐에서 빼주고 그 파티에 있던 사람들은 진실을 알게되니 진실을 아는 사람들만 따로 모아둔다. 큐의 길이만큼 반복이 끝나고난 뒤에 만약 큐의 길이가 그대로라면 큐에 남아있는 파티는 모두 진실을 모르는 파티만 남았다는 뜻이다. 이대로 코딩하면 된다.  
set을 사용한 이유는 중복을 제거해주고, set에서 in을 사용하면 hash를 이용해 O(1)의 복잡도를 가지기 때문이다.
```python
from collections import deque

# 사람수, 파티수
n, m = map(int, input().split())
q=deque()

real = list(map(int, input().split()))[1:] # 진실 아는 회원의 번호


for _ in range(m):
    # 파티 인원 수와 파티 참가자의 번호
    temp = list(map(int, input().split()))
    q.append(temp[1:]) # 해당 파티의 참가자 번호만 큐에 담기


while 1:
    n = len(q)
    cnt=0
    # 큐의 길이만큼 반복한다.
    # 진실을 아는 사람이 있는 파티는 큐에서 제거하고
    # 그 파티에 있던 사람들은 진실을 아는 real 리스트에 추가
    # 진실을 아는 사람이 없는 파티는 다시 큐에 추가
    while cnt<n:
        nums = q.popleft()
        key=0
        for num in nums:
            if num in set(real):
                key=1
                break
        if key:
            real.extend(nums)
            real = list(set(real))
        else:
            q.append(nums)
        cnt+=1

    # 큐의 길이에 변화가 없다면 현재 큐에 남은 파티 안에는
    # 진실을 아는사람이 없음
    if n== len(q):
        print(n)
        break
```
