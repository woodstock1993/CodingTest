"""
    1463번 1로 만들기
"""

def dp(m):
    dp = [0]*1000001

    for i in range(2, m+1):
        dp[i] = dp[i-1]+1
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i])

    return dp[m]

