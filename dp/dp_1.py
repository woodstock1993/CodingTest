"""
    1로 만들기  8-5
    //
"""

def func(n):
    dp = [0]*100

    if n == 1:
        return 0
    if n == 2 or n == 3 or n == 5:
        return 1

    if n-1 > 0 and (n-1) % 5 == 0:
        dp[n] = func(n-1) + 1
    elif n % 5 == 0:
        dp[n] = func(int(n//5)) + 1
    elif n % 3 == 0:
        dp[n] = func(int(n//3)) + 1
    elif n % 2 == 0:
        dp[n] = func(int(n//2)) + 1
    else:
        dp[n] = func(n-1) + 1
    return dp[n]

def func2(n):
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 1000001

    # 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
    for i in range(2, n + 1):
        # 현재의 수에서 1을 빼는 경우
        d[i] = d[i - 1] + 1
        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        # 현재의 수가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        # 현재의 수가 5로 나누어 떨어지는 경우
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[n]


def func3(n):
    dp = [0]*(n+1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 1
    if 6 <= n:
        for i in range(6, n+1):
            arr = []
            if i%2 == 0:
                arr.append(dp[i//2])
            if i%3==0:
                arr.append(dp[i//3])
            if i%5==0:
                arr.append(dp[i//5])
            arr.append(dp[i-1])
            dp[i] = min(arr) + 1

    return dp[n]


print(func3(26))
