import itertools


def solution(numbers):
    numbers = list(map(str, numbers))
    permutation = list(itertools.permutations(numbers, len(numbers)))
    print(permutation)
    res = []
    for elem in permutation:
        res.append(''.join(elem))
    res = list(set(map(int, res)))
    return str(max(res))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))