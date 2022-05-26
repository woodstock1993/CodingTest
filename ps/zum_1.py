def solution(n):
    answer = int((1/2)*(n-1)*n*(n+1))
    return answer


print(solution(3))


def func(n):
    sum = 0
    for i in range(1, n):
        sum += (i*n+i)
    return sum


for i in range(1, 100):
   if solution((i))  != func(i):
       print('diff')