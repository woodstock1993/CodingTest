"""
    백준 연구소
    1) 비어 있는 공간 중에서 3개를 골라 벽을 설치하자 -> 성공
    2) 2가 있는 좌표를 찾아라
    3) 바이러스 시뮬레이션 함수를 만들어라
    4) 방벽을 설치한 후 바이러스 시뮬레이션을 돌리고 전파된 바이러스의 개수를 리스트에 추가한다
    5) 리스트 중 가장 작은 원소를 반환함으로써 함수를 종료한다.
"""

from itertools import combinations
import copy

a, b = map(int, input().split())
graph = []
info = []
count = 0

for _ in range(a):
    graph.append(list(map(int, input().split())))

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            info.append([i, j])

# 지도에서 0인 지역에 바리케이트를 설치하는 경우의수, ([0,0],[0,1],[0,2]) 형태를 취함
nCr = combinations(info, 3)


def find_virus_coordinate():
    answer = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 2:
                answer.append([i, j])
    return answer


# 바이러스가 적힌 좌표가 있는 구간
virus_coordinate = find_virus_coordinate()


# 특정 좌표에서 감염확산 지도를 만들어주는 함수
def dfs(graph, x, y):
    global count
    if x < 0 or x >= a or y < 0 or y >= b:
        return
    if graph[x][y] == 2 and count != 0:
        return
    if graph[x][y] == 0:
        graph[x][y] = 2
    if graph[x][y] == 1:
        return

    count += 1
    dfs(graph, x - 1, y)
    dfs(graph, x + 1, y)
    dfs(graph, x, y - 1)
    dfs(graph, x, y + 1)
    count = 0
    return True


# 바이러스 세는 함수
def count_non_virus(new_graph):
    answer = 0
    for i in range(len(new_graph)):
        for j in range(len(new_graph[i])):
            if new_graph[i][j] == 0:
                answer += 1
    return answer


def simulate_virus(new_graph):
    answer = []
    for data in virus_coordinate:
        x = data[0]
        y = data[1]
        dfs(new_graph, x, y)

    total_virus = count_non_virus(new_graph)
    return total_virus


def solution(nCr):
    answer = []
    for infos in nCr:
        x_1, y_1 = infos[0][0], infos[0][1]
        x_2, y_2 = infos[1][0], infos[1][1]
        x_3, y_3 = infos[2][0], infos[2][1]

        new_graph = copy.deepcopy(graph)
        new_graph[x_1][y_1] = 1
        new_graph[x_2][y_2] = 1
        new_graph[x_3][y_3] = 1

        total_clean = simulate_virus(new_graph)
        answer.append(total_clean)

    return max(answer)


print(solution(nCr))
