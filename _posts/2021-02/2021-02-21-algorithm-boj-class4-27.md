---
layout: post
title: (Python) 백준 11054번 가장 긴 바이토닉 부분 수열 - class 4
subtitle:   (Python) 백준 11054번 가장 긴 바이토닉 부분 수열 - class 4
categories: algorithm
tags: boj 
comments: true
# header-img:
---

[[문제 링크](https://www.acmicpc.net/problem/11054){:target="_blank"}]


## 11054번 가장 긴 바이토닉 부분 수열
---
__접근 방법__  
증가하는 수열과 감소하는 수열을 합친 문제로 다이나믹 프로그래밍을 사용해야겠다고 생각했다.  
<br>

__해결__  
1. 증가하는 부분 수열의 가장 긴 길이를 dp_up 테이블에 담는다.
2. 감소하는 부분 수열의 가장 긴 길이를 dp_down 테이블에 담는다.
    - 주어진 수열을 뒤집어서 증가하는 부분 수열의 가장 긴 길이를 구하는 로직과 똑같이 수행하면 주어진 수열의 끝에서부터 해당 값을 최대값으로 하는 감소하는 부분 수열의 가장 긴 길이를 구하는 로직이 된다.
3. 두 dp를 합산하여 최대값에서 -1를 한 값을 출력한다.
    - dp테이블은 자신을 포함한 수열을 구했으므로 합산하게 되면 자신을 2번 포함하게 된다. 따라서 중복을 한 번 제거해줘야 한다.

cf) 5000이하의 입력횟수로 sys는 사용하지 않았다.
```python
n = int(input())
a = list(map(int, input().split()))
reverse_a = a[::-1]  # 감소하는 부분 수열의 길이를 구하기 위해 뒤집기

# 수열에서 자기 자신을 포함
dp_up = [1] * n  # 증가하는 부분 수열의 최대 길이
dp_down = [1] * n  # 감소하는 부분 수열의 최대 길이
dp_ans = [0] * n  # 합산할 dp테이블

for i in range(n):
    for j in range(i):
        # i보다 앞선 인덱스 value 값보다
        # i인덱스의 value가 더 큰 경우 수열의 길이 수정
        if a[j] < a[i]:
            dp_up[i] = max(dp_up[j] + 1, dp_up[i])
        if reverse_a[j] < reverse_a[i]:
            dp_down[i] = max(dp_down[j] + 1, dp_down[i])

for i in range(n):
    # reverse는 수열을 뒤집어서 사용했으므로
    # 합산할 때 이에 따른 인덱스값을 고려해줘야 한다.
    dp_ans[i] = dp_up[i] + dp_down[n - i - 1]

# 각 dp에서 자기 자신을 포함했으므로 한 번 제거해줘야함
print(max(dp_ans) - 1)
```