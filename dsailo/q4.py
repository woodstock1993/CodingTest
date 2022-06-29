import math


def solution(strs, t):
    dp_length = len(t)
    dp = [math.inf for _ in range(dp_length)]

    for i in range(dp_length):
        cur_word = t[:i + 1]
        temp = []
        for unit in strs:
            if cur_word.endswith(unit):
                if i == 0:
                    dp[i] = 1
                elif cur_word == unit:
                    dp[i] = 1
                else:
                    temp = dp[i - len(unit)] + 1
                    dp[i] = temp if temp < dp[i] else dp[i]

    return dp[dp_length - 1] if dp[dp_length - 1] != math.inf else -1


print(solution(	["ab", "na", "n", "a", "bn"], "nabnabn"))