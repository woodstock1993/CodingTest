from itertools import permutations


def solution(n):
    arr_1 = []
    arr_2 = []

    arr = [i for i in range(1, n + 1)]
    for i in range(len(arr)):
        if i % 2 == 0:
            arr_2.append(arr[i])
        else:
            arr_1.append(arr[i])

    answer = 0
    for i in range(1, len(arr_1) + 1):
        answer += len(permutations(arr_1), i)
    for i in range(1, len(arr_2) + 1):
        answer += len(permutations(arr_2), i)

    return answer