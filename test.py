def solution(brown, yellow):
    width = brown + yellow
    divisor = []
    for i in range(1, width + 1):
        if width % i == 0:
            divisor.append(i)

    num = len(divisor)

    if num % 2 == 1:
        return sorted([divisor[num // 2], divisor[num // 2]], reverse=True)
    else:
        return sorted([divisor[num // 2 - 1], divisor[num // 2]], reverse=True)


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))