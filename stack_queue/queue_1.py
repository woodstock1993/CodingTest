"""
    다리를 지나는 트럭
"""

from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    finish = deque()
    progress = deque()
    times = deque()
    time = 0
    target = len(truck_weights)

    while len(finish) != target:
        print(f'reamin: {weight - sum(progress)}, length: {bridge_length-len(progress)}')
        durability_weight = weight - sum(progress)
        durability_cnt = bridge_length - len(progress)
        if len(truck_weights) > 0 and durability_weight - truck_weights[0] >= 0 and durability_cnt - 1 >= 0:
            print(f'weight: {durability_weight}, cnt: {durability_cnt}')
            progress.append(truck_weights.popleft())
            times.append(1)

        if len(times) > 0:
            if times[0] == bridge_length:
                finish.append(progress.popleft())
                times.popleft()
            for i in range(len(times)):
                times[i] += 1

        time += 1
        print(f'time: {time}, times: {times}, finish: {finish}, progress: {progress}')

    return time+1


solution(bridge_length, weight, truck_weights)