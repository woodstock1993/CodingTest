# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if visited[node] == False:
            dfs(graph, node, visited)


dfs(graph, 1, visited)
