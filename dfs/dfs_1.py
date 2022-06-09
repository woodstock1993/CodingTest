graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

v = 1
visited = [False]*9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if visited[node] == False:
            dfs(graph, node, visited)


dfs(graph, 1, visited)