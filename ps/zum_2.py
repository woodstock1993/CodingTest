import itertools
logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

def div_str(string):
    arr = string.split(' ')
    return arr


# 수험생 별 문제별 점수를 기록한 자료
def trim(logs):
    dic = {}
    for i in range(len(logs)):
        arr = div_str(logs[i])
        if arr[0] not in dic:
            dic[arr[0]] = {arr[1]: arr[2]}
        else:
            if arr[1] not in dic[arr[0]]:
                dic[arr[0]].update({arr[1]: arr[2]})
            elif arr[1] in dic[arr[0]] and arr[2] < dic[arr[0]][arr[1]]:
                dic[arr[0]].update({arr[1]: arr[2]})
    return dic


# 수험생 별 문제 개수를 기록한 자료
def q_num(trim_logs, questions):
    dic = {}
    for i in range(len(trim_logs)):
        dic[questions[i]] = len(trim_logs[questions[i]])
    return dic


# 수험생 별 문제번호와 점수를 기록한 자료
def q_number(trim_logs, questions):
    arr = {}
    arr2 = {}
    for i in range(len(trim_logs)):
        for k, v in trim_logs[questions[i]].items():
            if questions[i] not in arr:
                arr[questions[i]] = []
                arr[questions[i]].append(k)
            if questions[i] not in arr2:
                arr2[questions[i]] = []
                arr2[questions[i]].append(v)
            else:
                arr[questions[i]].append(k)
                arr2[questions[i]].append(v)
    return arr, arr2


# 치팅인지 아닌지 판별하는 함수
def are_you_cheat(trim_logs, questions, p1, p2):
    question_num = q_num(trim_logs, questions)
    q_kind, q_score = q_number(trim_logs, questions)

    if question_num[p1] != question_num[p2]:
        return False
    if question_num[p1] == question_num[p2] and question_num[p1] < 5:
        return False
    if q_kind[p1].sort() != q_kind[p2].sort():
        return False
    if q_score[p1].sort() != q_score[p2].sort():
        return False
    return True


def solution(logs):
    res = []
    trim_logs = trim(logs)
    questions = list(trim_logs)
    nPr = itertools.permutations(questions, 2)
    for item in nPr:
        if are_you_cheat(trim_logs, questions, item[0], item[1]) == True:
            res.append(item[0])
            res.append(item[1])
    res = list(set(res))
    if len(res) == 0:
        return ["None"]
    return sorted(res)
