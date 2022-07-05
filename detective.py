
def detective(string):
    length = len(string)
    if length == 1:
        return 1
    if string == '10' or string == '00':
        return 2
    if string == '01' or string == '11':
        return 1

    # ????? 유형
    if '1' not in string and '0' not in string and '?' in string:
        return length

    # 1111100000 유형
    if '?' not in string and '1' in string and '0' in string and string[0] != '0':
        zero_index = string.find('0')
        if '0' not in string[:zero_index]:
            return 2

    # ?????0?0???000 유형
    if '1' not in string and '0' in string and '?' in string:
        index = string.find('0')
        return index + 1

    # 111???1?1?1?1????
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

    # 1111???000 모두 있는 유형
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
    new_arr = [
        '10000',
        '11',
        '?0?0???0??',
        '??',
        '110?0?0?',
        '?????1???1???1110',
        '?1000000000',
        '??100?0?',
        '1?',
        '?11?110000000?0',
        '?1?110??0??000??????',
        '111?1111?100',
        '1?11??11',
        '?0?0???0????0?',
        '??1?',
        '1?0',
        '??1?0??',
        '??100?000?0?00?000',
        '??100',
        '?00',
        '??1???1?1?11?11????1',
        '11??',
        '1?00??',
        '?0',
        '11?00',
        '111?11?1000?0??0???0',
        '?1??00',
        '110???0??0??0',
        '0000??00',
        '11?0??',
        '1',
        '1?100?000???000?0?',
        '?1111?1',
        '1?11111????00',
        '1?1?1???1000?',
        '?110',
        '?',
        '??1?000?0?0',
        '??0???0??00??00000',
        '??',
        '1??1000??????0?0',
        '?111?1?',
        '??111?1?111111',
        '??10?0??0?00?0??0?',
        '1???0????0??00?0'
    ]
