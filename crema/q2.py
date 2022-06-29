def is_first_index_nine(num):
    if num[0] == '9':
        return True
    return False


def is_first_index_one(string):
    if string[0] == '1':
        return True
    return False


def find_index_nine(string):
    index = -1
    for i in range(len(string)):
        if string[i] == '9':
            index = i
            break
    return index


def find_index_one(string):
    index = -1
    for i in range(len(string)):
        if string[i] == '1':
            index = i
            break
    return index


def if_is_first_index_not_one(string):
    index = ''
    for i in range(len(string)):
        if string[i] != '1' and string[i] != '0':
            index = i
            break
    if index == '':
        min = int(string)
    else:
        replace_target2 = string[index]
        cnt = string.count(replace_target2)
        while cnt:
            string = string.replace(replace_target2, '0')
            cnt -= 1
        min = int(string)
    return min


def if_is_first_index_nine(string):
    big, small, index = '', '', ''

    for i in range(len(string)):
        if string[i] != '9':
            index = i
            break

    if index == '':
        big = int(string)
    else:
        replace_target3 = string[index]
        cnt = string.count(replace_target3)
        temp = string
        while cnt:
            temp = temp.replace(replace_target3, '9')
            cnt -= 1
        big = int(temp)

    temp2 = string
    if not is_first_index_one(temp2):
        replace_target4 = string[0]
        cnt2 = temp2.count(replace_target4)
        if cnt2 > 0:
            while cnt2:
                temp2 = temp2.replace(replace_target4, '1')
                cnt2 -= 1
            small = int(temp2)
    return big, small


def func(string):
    replace_target = string[0]
    cnt = string.count(replace_target)
    temp = string
    while cnt:
        temp = temp.replace(replace_target, '9')
        cnt -= 1
    max = int(temp)
    temp2 = string
    if is_first_index_one(temp2):
        index = ''
        for i in range(len(temp2)):
            if temp2[i] != '1' and temp2[i] != '0':
                index = i
                break
        if index == '':
            min = int(temp2)
        else:
            replace_target2 = temp2[index]
            cnt = temp2.count(replace_target2)
            while cnt:
                temp2 = temp2.replace(replace_target2, '0')
                cnt -= 1
            min = int(temp2)
    else:
        min = if_is_first_index_not_one(temp2)
    return max, min


def findRange(num):
    big = ''
    small = ''
    string = str(num)
    index = find_index_nine(string)
    if index == -1:
        big, small = func(string)
    else:
        if is_first_index_nine(string):
            big, small = if_is_first_index_nine(string)
        else:
            big, small = func(string)
    return big - small


print(findRange('9'))