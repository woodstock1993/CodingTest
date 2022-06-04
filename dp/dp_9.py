"""
    11726번 타일링
"""

n = int(input())
dp = [0]*1000

dp[0] = 1

if n >= 1:
    dp[1] = 2

if n >= 3:
    for i in range(2, n):
        dp[i] = dp[i-2]+dp[i-1]

print(dp[n-1] % 10007)
