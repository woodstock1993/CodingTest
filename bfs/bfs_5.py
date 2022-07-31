import copy

r_string = ""


# string 문자열을 '균형잡힌 괄호 문자열'과 그 외의 '문자열'로 구분한다. 빈 문자열일 경우 빈 문자열을 반환
def func_1(string):
    s = ""
    if string == "":
        return s
    open_sign = ""
    count = 0
    for i in range(len(string)):
        if i == 0:
            open_sign = string[i]
            s += string[i]
            count += 1
        elif string[i] != open_sign:
            s += string[i]
            count -= 1
        elif string[i] == open_sign:
            s += string[i]
            count += 1
        if count == 0:
            break

    string = string.replace(s, "", 1)

    return s, string


def func_2(v):
    s = ""
    v = list(v)
    while v:
        s += v.pop()
    return s


# 올바른 괄호 문자열(2)인지 판단하는 함수
def is_right_bracelet(string):
    stack = []
    count = 0
    string = list(string)

    for i in range(len(string)):
        if i == 0:
            stack.append(string[i])
            count += 1
        elif string[i] == ')':
            if count != 0 and stack[-1] == '(':
                stack.pop()
                count -= 1
        elif string[i] == '(':
            stack.append(string[i])
            count += 1

    s = ''.join(stack)

    if s == '':
        return True
    return False


def solution(p):
    global r_string

    a, b = func_1(p)

    if is_right_bracelet(a):
        r_string += a
    else:
        r_string += func_2(a)

    if b == "":
        return r_string

    p = b
    solution(p)
    return r_string


print(solution("()))((()"))
