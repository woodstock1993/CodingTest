n = int(input())
arr = []

for _ in range(n):
    arr.append(input())


def count_num(string):
    length = len(string)
    if length == 1:
        return 1
    if length == string.count('?'):
        return length
    if '?' not in string and length == 2 and '1' in string and '0' in string:
        return 2
    if '?' not in string and '1' in string and '0' in string and length >2:
        return 2


for i in range(len(arr)):
    print(count_num(arr[i]))

str = '1??????0'

if len(str) >= 3 and str[0] == '1' and str[-1] == 0 and len(str) -2 == str.count('?'):
    pass


