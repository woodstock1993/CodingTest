"""
개미 전사 8-6
"""


def get_input():
    return int(input()), list(map(int, input().split()))


def brute_force(dp, b):
    start = 0
    index = -1
    max_index = len(dp) - 1
    for i in range(len(b)):
        if (b[i] >= start) and (i - 1 >= 0 and dp[i - 1] == False) and (i + 1 <= max_index and dp[i + 1] == False) and \
                dp[i] == False:
            start = b[i]
            index = i
    if b[0] >= start and dp[0] == False and index != 0:
        dp[index] = False
        start = dp[0]
        dp[0] = True
        return (dp, start)
    if b[max_index] > start and dp[max_index] == False and index != max_index:
        dp[index] = False
        start = b[max_index]
        dp[0] = False
        dp[max_index] = True
        return (dp, start)

    dp[index] = True
    return (dp, start)


def solve(n, li):
    res = 0
    dp = [False]*n
    for i in range(n):
        dp, start = brute_force(dp, li)
        res += start
        dp = dp
    return res

def solve2(n, array):
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 100

    # 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])

    # 계산된 결과 출력
    return d[n - 1]


import random
li = [1,2,1,2,1,2,1,2,1,2, 100, 100, 100, 20, 20, 20, 20, 30, 40, 20, 13, 25, 143, 123]

print(solve(len(li), li), solve2(len(li), li))
