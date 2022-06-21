# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A, B):
    # write your code in Python 3.6
    info = []
    for i in range(len(A)):
        info.append([A[i], B[i]])

    graph = [[] for _ in range(N + 1)]
    new_arr = []

    for i in range(len(info)):
        node = info[i][0]
        node2 = info[i][1]
        graph[node].append(node2)
        graph[node2].append(node)

    for i in range(len(graph)):
        a = len(graph[i])
        if a >= 1:
            new_arr.append(a)
    new_arr.sort(reverse=True)

    sum = 0

    for i in range(len(new_arr)):
        sum += new_arr[i] * N
        N -= 1
    return sum


solution(5, [2, 2, 1, 2], [1, 3, 4, 4])