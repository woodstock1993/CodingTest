# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import combinations


# from extratypes import Point2D  # library with types used in the task

def is_cartesian(coordinates):
    ap = coordinates[0]
    aq = coordinates[1]
    ar = coordinates[2]

    ap_x = ap[0]
    ap_y = ap[1]

    aq_x = aq[0]
    aq_y = aq[1]

    ar_x = ar[0]
    ar_y = ar[1]

    try:
        c1 = (aq_y - ap_y) / (aq_x - ap_x)
        c2 = (ar_y - aq_y) / (ar_x - aq_x)
        c3 = (ar_y - ap_y) / (ar_x - ap_x)
    except ZeroDivisionError:
        return False

    if c1 == c2 and c2 == c3 and c1 == c3:
        return True
    return False


def solution(A):
    answer = 0
    new_arr = []
    for i in combinations(A, 3):
        new_arr.append(list(i))
    for i in range(len(new_arr)):
        if is_cartesian(new_arr[i]) == True:
            answer += 1
    return answer
