logs = ["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]

def split_elem(elem):
    return elem.split(' ')

def trim_logs(logs):
    dic = {}
    logs = list(set(logs))

    for i in range(len(logs)):
        name, q = split_elem(logs[i])
        if q not in dic:
            dic[q] = 1
        else:
            dic[q] += 1
    return dic


def return_q(trim_logs):
    res = []
    total = 0
    people = len(trim_logs)
    print(people)
    for k, v in trim_logs.items():
        print(v/people)
        if (v/people) >= 0.5:
            res.append(k)
    return sorted(res)


def solution(logs):
    trim = trim_logs(logs)
    answer = return_q(trim)
    return answer


trim = trim_logs(logs)
print(trim)
print(return_q(trim))

