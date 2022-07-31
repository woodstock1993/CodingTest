def dfs(x, y, n, m, bitmap, arr):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if bitmap[x][y] == 1:
        bitmap[x][y] = 2
        arr.append(1)
        dfs(x-1, y, n, m, bitmap, arr)
        dfs(x, y-1, n, m, bitmap, arr)
        dfs(x+1, y, n, m, bitmap, arr)
        dfs(x, y+1, n, m, bitmap, arr)
        return True
    return False


def solution(bitmap):
    answer = []
    n = len(bitmap)
    m = len(bitmap[0])
    result = []
    arr = []
    for i in range(n):
        for j in range(m):
            if dfs(i, j, n, m, bitmap, arr) == True:
                result.append(arr)
                arr = []
    for i in range(len(result)):
        answer.append(sum(result[i]))
    answer.sort()
    return answer


print(solution([[0,0,0,0,0],[0,1,0,1,0],[0,1,1,0,0],[1,1,0,0,1],[0,0,0,1,1]]))