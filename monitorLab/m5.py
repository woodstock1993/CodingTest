
answer = []


def recursive(cnt, total_index, nums, index):
    global answer
    l_r = cnt
    r_r = cnt

    if index < 0 or index >= total_index:
        return -1

    delta_index = nums[index]

    forward_index = index + delta_index
    backward_index = index - delta_index


    if l_r >= 1000 or r_r >= 1000:
        return -1

    if forward_index <= total_index:
        if delta_index == 0:
            return
        r_r += 1
        if forward_index == total_index:
            answer.append(r_r)
            return answer[0]
        recursive(r_r, total_index, nums, forward_index)

    if backward_index >= 0:
        if delta_index == 0:
            return
        l_r += 1
        recursive(l_r, total_index, nums, backward_index)





def solution(nums):
    global answer
    total_index = len(nums) - 1
    cnt = 1
    index = nums[0]

    if index == total_index:
        return cnt

    if index == 0:
        return -1

    recursive(cnt, total_index, nums, index)

    return min(answer)


print(solution([4 ,1 ,2 ,3 ,1 ,0 ,5]))