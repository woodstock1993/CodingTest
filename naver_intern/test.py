def solution(N):
    largest = 0
    shift = 0
    temp = N
    for i in range(1, 30):
        index = (temp & 1)
        temp = (temp >> 1) | (index << 30)
        if (temp > largest):
            largest = temp
            shift = i
    return shift
