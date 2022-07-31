from collections import deque

m, n = map(int, input().split())
graph = []
q = []

for i in range(m):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], 0, i, j))

q.sort()
data = deque(q)

S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = data.popleft()
    if s == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                data.append((virus, s+1, nx, ny))

print(graph[X-1][Y-1])

