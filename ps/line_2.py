import math
ceil = math.ceil

def solution(n, times):
    d = [0]*100

    d[0] = 0
    d[1] = 0
    d[2] = d[1] + times[0]
    if n == 2:
        return d[2]
    d[3] = d[2] + times[0]
    if n == 3:
        return d[3]
    d[4] = min(d[2]+times[1], d[3]+times[0])
    if n == 4:
        return d[4]
    d[5] = min(d[2]+times[1]+times[0], d[3]+times[1], d[4]+times[0])
    if n == 5:
        return d[5]
    d[6] = min(d[3]+times[2], d[4]+times[1], d[5]+times[0])
    if n == 6:
        return d[6]

    for i in range(7, n+1):
        max = i-1
        index = ceil(n/2)
        d[i] = min(d[index]+times[index-1], d[index+1]+times[index-2], d[index+2]+times[index-3])

    answer = d[n]
    return answer