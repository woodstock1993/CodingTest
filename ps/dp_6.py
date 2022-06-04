def dp():
    m = int(input())
    dp = [0]*(m+3)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    if m == 1:
        return 0
    elif m == 2 or m == 3:
        return 1

    for i in range(4, m+1):
        dp[i] = dp[i-1]+1
        if i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        if i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1

    return dp[m]
