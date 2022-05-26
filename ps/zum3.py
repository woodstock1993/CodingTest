import math
data = [[1, 0, 5],[2, 2, 2],[3, 3, 1],[4, 4, 1],[5, 10, 2]]

def div_data(string):
    arr = string.split(',')
    return arr


def trim_data(data):
    dic = {}
    for i in range(len(data)):
        arr = data[i]
        if arr[0] not in dic:
            dic[arr[0]] = [arr[1], arr[2]]
    return dic


def is_printing(elem, time):
    spend_time = elem[2]
    if time <= spend_time:
        return True
    return False


def return_waiting_list_and_data(data, time, waiting_list):
    for i in range(len(data)):
        if data[i][1] == time:
            waiting_list.append(data[i][0])
            if len(data) > 0:
                data.remove(data[0])
    return waiting_list, data


def is_print_finished(elem, time):
    spend_time = elem[2]
    if spend_time >= time:
        return False
    return True


def get_least_page_document(waiting_list, trim_datas):
    doc = None
    arr = []
    print_page = math.inf
    for doc_num in waiting_list:
        if trim_datas[doc_num][1] < print_page:
            # print(trim_datas[doc_num][1])
            print_page = trim_datas[doc_num][1]
            doc = doc_num
            print(doc)
        elif trim_datas[doc_num][1] == print_page:
            arr.append(doc)
            arr.append(doc_num)

    return list(set(arr))


def update_waiting_list():
    pass


def solution(data):
    answer = []
    total_time = data[-1][1]
    time = 0
    first_print = data[0]
    while time <= total_time:
        if is_printing(first_print, time):
            time += 1
            continue
        if len(data) > 0:
            data.remove(data[0])

