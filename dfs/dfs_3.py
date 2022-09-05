"""
    감시 피하기
"""

"""
X S X X T 
T X S X X
X X X X X
X T X X X
X X T X X
"""

from itertools import combinations


def make_map_space_info():
    m = int(input())
    graph = []
    space_info = []
    for i in range(m):
        elem = input().split()
        graph.append(elem)

        for j in range(len(elem)):
            if elem[i] == 'X':
                space_info.append((i, j))

    return graph, space_info


graph, space_info = make_map_space_info()

print(graph, space_info)
