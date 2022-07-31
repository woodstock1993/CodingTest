from itertools import permutations

"""
    연산자 끼워 넣기
"""

arr = []

m = int(input())
for _ in range(2):
    arr.append(list(map(int, input().split())))

sequence = arr[0]
a_op = arr[1]

l_sequence = len(sequence)


def get_a_op(a_op):
    op = ['+', '-', '*', '/']
    answer = []
    for i in range(len(op)):
        answer += [op[i] for j in range(a_op[i])]
    return answer


def sub_calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b


def calculate(seq, a_op):
    res = seq[0]
    l_seq = len(seq)
    for i in range(1, l_seq):
        res_ = sub_calculate(res, seq[i], a_op[i-1])
        res = res_
    return res


op_arr = get_a_op(a_op)
print(op_arr)
print(calculate(sequence, op_arr))

nPr = list(permutations(op_arr, l_sequence-1))

answer = []
for cal_info in nPr:
    for i in range(len(cal_info)):
        res = calculate(sequence, list(cal_info[i]))
        answer.append(res)

print(answer)



