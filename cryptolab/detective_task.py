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
    if string == '10':
        return 2
    if string == '01':
        return 1
    if string == '00':
        return 1
    if length >= 3 and str[0] == '1' and str[-1] == '0' and length - 2 == string.count('?'):
        return length


for i in range(len(arr)):
    print(count_num(arr[i]))

