n = int(input())

def dp(x):
    dp = [0]*100001
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, x+1):
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    return dp[x]


for _ in range(n):
    n = int(input())
    print(dp(n))

