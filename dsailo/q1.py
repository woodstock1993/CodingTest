import math


def solution(strs, t):
    dp_length = len(t)
    dp = [math.inf for _ in range(dp_length)]
    print(dp)

    for i in range(dp_length):
        current_unit = t[:i + 1]

        for unit in strs:
            if current_unit.endswith(unit):
                delta = len(current_unit) - len(unit)

                if delta == 0:
                    dp[i] = 1;
                else:
                    dp[i] = min(dp[i], dp[delta - 1] + 1)

    return dp[dp_length - 1] if dp[dp_length - 1] != math.inf else -1


solution(["ba", "na", "n", "a"], "banana")