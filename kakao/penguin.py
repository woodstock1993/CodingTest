from collections import deque
import copy

arr = [4, 7, 9]
arr2 = [5, 6, 10]
# arr = sorted(arr)
arr = deque(arr)
arr2 = deque(arr2)
arr3 = copy.deepcopy(arr2)


def measure_distance_min(arr):
    delta_1 = arr[1] - arr[0]
    delta_2 = arr[2] - arr[1]
    cnt = 0

    while not (delta_1 == 1 and delta_2 == 1):
        if delta_1 <= delta_2 and delta_1 == 1:
            coordinate = (arr[1] + arr[2]) // 2
            arr.popleft()
            arr.insert(1, coordinate)
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]
        elif delta_1 <= delta_2 and delta_2 > 0:
            coordinate = (arr[0] + arr[1]) // 2
            arr.pop()
            arr.insert(1, coordinate)
            cnt += 1
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]
        elif delta_1 > delta_2 and delta_2 == 1:
            coordinate = (arr[0] + arr[1]) // 2
            arr.pop
            arr.insert(1, coordinate)
            cnt += 1
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]
        elif delta_1 > delta_2 and delta_1 > 0:
            coordinate = (arr[1] + arr[2]) // 2
            arr.popleft()
            arr.insert(1, coordinate)
            cnt += 1
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]

    return cnt


def measure_distance_max(arr3):
    arr = arr3
    delta_1 = arr[1] - arr[0]
    delta_2 = arr[2] - arr[1]
    cnt = 0

    while not (delta_1 == 1 and delta_2 == 1):
        print(f'arr2: {arr}')
        if delta_1 == 1 and delta_2 > 1:
            coordinate = arr[2] - 1
            arr.pop()
            arr.append(coordinate)
            cnt += 1
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]
        elif delta_2 == 1 and delta_1 > 1:
            coordinate = arr[0] + 1
            arr.popleft()
            arr.insert(0, coordinate)
            cnt += 1
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]
        elif delta_1 >= delta_2 and delta_2 > 0:
            coordinate = arr[1] - 1
            arr.pop()
            arr.insert(1, coordinate)
            cnt += 1
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]

        elif delta_1 < delta_2 and delta_1 > 0:
            coordinate = arr[1] + 1
            arr.popleft()
            arr.insert(1, coordinate)
            cnt += 1
            delta_1 = arr[1] - arr[0]
            delta_2 = arr[2] - arr[1]
    return cnt


print(measure_distance_min(arr2))
# print(measure_distance_max(arr2))