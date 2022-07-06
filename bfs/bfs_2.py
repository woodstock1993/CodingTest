"""
    특정 거리의 도시 찾기
"""

from collections import deque

# draw graph
N, M, K, X = map(int, input().split())
arr = []
distance = 1
graph = [[] for _ in range(N + 1)]
distance = [-1] * (N + 1)
distance[X] = 0
queue = deque([X])

for _ in range(M):
    arr.append(list(map(int, input().split())))

for info in arr:
    graph[info[0]].append(info[1])

while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[now] += 1
            queue.append(next_node)

check = False

for i in distance:
    if i == K:
        print(i)
        check = True

if check is False:
    print(-1)
