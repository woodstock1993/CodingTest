def calc_delta(n1, n2):
    big = max(n1, n2)
    small = min(n1, n2)

    if big == small:
        return 0
    delta_1 = big - small
    delta_2 = 10 + small - big

    if delta_1 >= delta_2:
        return delta_2
    return delta_1


def solution(p,s):
    total = 0
    for i in range(len(p)):
        a, b = int(p[i]), int(s[i])
        total += calc_delta(a, b)
    return total