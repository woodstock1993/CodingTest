def mn_to_nm_arr(arr):
    length = len(arr)
    if length == 0:
        return 0
    new_arr = [[] for _ in range(len(arr[0]))]
    for i in range(len(new_arr)):
        for j in range(len(arr)):
            new_arr[i].append(arr[j][i])
    return new_arr


def main():
    N, K, P, L = map(int, input().split())
    circle = [1] + [i for i in range(N, 1, -1)]
    arr = []
    for _ in range(P):
        arr.append(list(map(int, input().split())))
    arr = mn_to_nm_arr(arr)

    cur_index = 0
    if circle[0] == P:
        print(1, 1)
        return

    start_l = 0
    for i in range(len(arr)):
        start_l += 1
        for j in range(len(arr[i])):
            move = arr[i][j] % N
            cur_index = (cur_index + move) % N
            print(cur_index)
            if circle[cur_index] == P:
                print(start_l, j + 1)
                return

    print(-1)
    return


if __name__ == "__main__":
    main()

