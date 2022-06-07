"""
    금광
"""

import numpy as np


# count = int(input())
# hv = []     ## horizontal vertical -> hv :: 배열의 가로세로 정보를 담고 있음
# mine = []   ## 금광의 배열을 담고 있는 배열

# for _ in range(count):
#     hv.append(list(map(int, input().split())))
#     mine.append(list(map(int, input().split())))


# hv의 요소와 mine 의 요소를 결합시켜
def convert_arr(hv_, mine_):
    unit = hv_[1]
    new_mine_ = []
    unit_carrier = []
    cnt_unit = 0
    for i in range(len(mine_)):
        unit_carrier.append(mine_[i])
        cnt_unit += 1
        if cnt_unit == unit:
            new_mine_.append(unit_carrier)
            unit_carrier = []
            cnt_unit = 0
    return list(map(list, np.transpose(new_mine_)))


def dp(new_mine_):
    n = len(new_mine_)
    dp = [0] * n
    dp[0] = max(new_mine_[0])
    index = new_mine_[0].index(dp[0])
    print(f'index: {index}')
    max_index = len(new_mine_[0])-1
    for i in range(1, n):
        if index-1 >= 0 and index+1 <= max_index:
            max_gold = max(new_mine_[i][index - 1], new_mine_[i][index], new_mine_[i][index + 1])
            index = new_mine_[i].index(max_gold)
            print(f'index: {index}')
            dp[i] += dp[i-1]+max_gold
        elif index-1 >= 0 and index+1 > max_index:
            max_gold = max(new_mine_[i][index - 1], new_mine_[i][index])
            index = new_mine_[i].index(max_gold)
            print(f'index: {index}')
            dp[i] += dp[i-1]+max_gold
        elif index-1 < 0 and index+1 <= max_index:
            max_gold = max(new_mine_[i][index], new_mine_[i][index + 1])
            index = new_mine_[i].index(max_gold)
            print(f'index: {index}')
            dp[i] += dp[i-1] + max_gold

    return dp[n-1]


# new_mine_ = convert_arr([3, 4], [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7])
new_mine_ = convert_arr([4, 4], [1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2])
print((new_mine_))
print(dp(new_mine_))

