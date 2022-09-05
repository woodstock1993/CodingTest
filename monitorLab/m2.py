block = 0

def dfs(v, x, y):
    global block

    if x <= -1 or x >= len(v) or y <= -1 or y >= len(v[0]):
        return False

    if v[x][y] == 1:
        v[x][y] = 2
        block += 1

        dfs(v,  x - 1, y)
        dfs(v, x, y - 1)
        dfs(v, x + 1, y)
        dfs(v, x, y + 1)
        return True
    return False


def solution(v):
    global block
    num_block = []
    total = 0
    for i in range(len(v)):
        for j in range(len(v[i])):
            if dfs(v, i, j) is True:
                total += 1
                num_block.append(block)
                block = 0

    max_block = max(num_block)
    return [total, max_block]
