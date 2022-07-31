# Plase note that external libraries, such as NumPy or Pandas
# are NOT available for this task

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import copy

# num의 자리수를 반환
def number_of_digits(num):
    res = 0
    while num != 0:
        num = num // 10
        res += 1
    return res


# 자리수와 문자열 형태의 정수를 인수로 받아 모자란 자리수 만큼 0을 채워서 문자열 형태로 반환하는 함수
def zero_plus_string_number(num_of_digits, string_int):
    string_int = str(string_int)
    n_delta = num_of_digits - len(string_int)
    if n_delta == 0:
        return string_int
    string_zeros = '0' * n_delta
    return string_zeros + string_int



def solution(S):
    dic = {}
    S = S.split('\n')
    temp = copy.deepcopy(S)
    for i in range(len(S)):
        S[i] = S[i].split(',')
        city = S[i][1]
        if city not in dic:
            dic[city] = []
            dic[city].append([S[i][0], S[i][2], i])
        else:
            city = S[i][1]
            dic[city].append([S[i][0], S[i][2], i])

    for k, v in dic.items():
        for i in range(len(v) - 1):
            for j in range(len(v) - 1):
                if v[j+1][1] < v[j][1]:
                    v[j], v[j+1] = v[j+1], v[j]

    for k, v in dic.items():
        num_len = len(v)
        num_of_digits = number_of_digits(num_len)
        for i in range(len(v)):
            string = ""
            string += k + zero_plus_string_number(num_of_digits, i+1) + '.' + v[i][0].split('.')[1]
            string = string.replace(" ", "")
            v[i].append(string)


    super_string = ""

    for i in range(len(temp)):
        temp[i] = temp[i].split(',')
        city = temp[i][1]
        for j in range(len(dic[city])):
            if S[i][2] == dic[city][j][1]:
                string = dic[city][j][3] + '\n'
                string = string.replace(" ", "")
                super_string += string
                break


    return super_string

