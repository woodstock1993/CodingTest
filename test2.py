
def detective(string):
    length = len(string)
    if length == 1:
        return 1
    if string == '10' or string == '00':
        return 2
    if string == '01' or string == '11':
        return 1

    if '1' not in string and '0' not in string and '?' in string:
        return length

    if '?' not in string and '1' in string and '0' in string and string[0] != '0':
        zero_index = string.find('0')
        if '0' not in string[:zero_index]:
            return 2

    if '1' not in string and '0' in string and '?' in string:
        index = string.find('0')
        return index + 1

    if '0' not in string and '?' in string and '1' in string:
        q_index = ""
        one_index = ""
        q2_index = ""
        one2_index = ""
        for i in range(length-1, -1, -1):
            if string[i] == '1' and one_index == "":
                one_index = i
            elif string[i] == '?' and q_index == "":
                q_index = i
            elif one_index != "" and one2_index == "":
                one2_index = i
            elif q_index != "" and q2_index == "":
                q2_index = i
        if '1' not in string[:i+1] and q_index < one_index:
            return 1
        elif '?' not in string[:i+1] and one_index < q_index:
            return length - one_index
        elif one_index - one2_index == 1:
            return 1


    if '0' not in string and '?' in string and string.count('1') == 1:
        return length - string.find('1')
    if string[0] == '1' and string[-1] == '0' and string.count('?') == length - 2:
        return length - 2

    zero_index = string.find('0')
    one_index = ""
    for i in range(length-1, -1, -1):
        if string[i] == '1':
            one_index = i
            break
    if one_index < zero_index:
        return zero_index - one_index + 1


def solution():
    arr = []
    for _ in range(int(input())):
        arr.append(input())

    for i in arr:
        print(detective(i))


if __name__ == '__main__':
    solution()