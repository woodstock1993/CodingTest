"""
    음료수 얼려먹기
"""

graph = [[0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]

def dfs(graph, i, j):
    graph[i][j] = 1
    if i-1 >= 0 and graph[i-1][j] == 0:
        i -= 1
        graph[i][j] = 1
        dfs(graph, i, j)
    if i+1 <= (len(graph)-1) and graph[i+1][j] == 0:
        i += 1
        graph[i][j] = 1
        dfs(graph, i, j)
    if j-1 >= 0 and graph[i][j-1] == 0:
        j -= 1
        graph[i][j] = 1
        dfs(graph, i, j)
    if j+1 <= len(graph[0])-1 and graph[i][j+1] == 0:
        j += 1
        graph[i][j] = 1
        dfs(graph, i, j)


for i in range(len(graph)):
    answer = 0
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            dfs(graph, i, j)
        answer += 1


print(answer)