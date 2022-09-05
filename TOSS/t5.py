def solution(text):
    new_arr = []
    arr = text.split(' ')
    for i in range(len(arr)):
        length = len(arr[i])
        if length >= 3:
            strs = ""
            for j in range(length - 1, -1, -1):
                strs += arr[i][j]
            new_arr.append(strs)
        else:
            new_arr.append(arr[i])
        new_arr.append('')

    del new_arr[-1]
    answer = ' '.join(new_arr)

    return answer


print(solution("안녕하세요저는김박산다라퐁구리입니다"))