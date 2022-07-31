# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
a, b = list(map(int, input().split()))


def make_box(b):
    box = []
    for _ in range(b):
        box.append(list(map(int, input().split())))
    return box


def make_map(a, b, box):
    map = [['.' for i in range(a)] for _ in range(a)]
    for i in range(a):
        for j in range(a):
            if i == j:
                map[i][j] = 'x'

    for i in range(len(box)):
        for j in range(len(box[i])):
            map[i - 1][j - 1] = 'o'
            map[j - 1][i - 1] = 'x'
    return map


def count():
    box = make_box(b)
    map = make_map(a, b, box)
    res = 0
    for i in range(len(map)):
        cnt = 0
        for j in range(len(map[i])):
            if map[i][j] == 'x' or map[i][j] == 'o':
                cnt += 1
        if cnt == len(map[i]):
            res += 1
    return res


print(count())