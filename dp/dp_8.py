"""
    2579 계단 오르기
"""

n = int(input())
arr = []
dp = [0] * 300

for _ in range(n):
    arr.append(int(input()))

if n >= 1:
    dp[0] = arr[0]

if n >= 2:
    dp[1] = arr[0] + arr[1]
    for i in range(1, len(arr)):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[n-1])
