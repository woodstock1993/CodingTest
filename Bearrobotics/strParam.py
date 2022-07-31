import re

def StringChallenge(strParam):
    strParam = strParam.replace('plus', '+').replace('minus', '-')
    strParam = strParam.replace('zero', '0').replace('one', '1').replace('two', '2') \
        .replace('three', '3').replace('four', '4').replace('five', '5') \
        .replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')
    sign = []

    for i in range(len(strParam)):
        if strParam[i] == '+' or strParam[i] == '-':
            sign.append(strParam[i])

    arr = re.split(r'[+-]', strParam)
    arr = list(map(int, arr))
    str_number = arr[0]
    for i in range(len(sign)):
        if sign[i] == '-':
            str_number -= arr[i + 1]
        elif sign[i] == '+':
            str_number += arr[i + 1]

    str_param = ''
    if str_number < 0:
        str_param += 'negative'
        str_number = str_number * -1

    str_param += str(str_number).replace('0', 'zero').replace('1', 'one').replace('2', 'two') \
        .replace('3', 'three').replace('4', 'four').replace('5', 'five') \
        .replace('6', 'six').replace('7', 'seven').replace('8', 'eight').replace('9', 'nine')

    return str_param


# keep this function call here
print(StringChallenge("oneminusoneminusoneminusoneminusoneminusoneminusoneminusoneminusoneminusone"))