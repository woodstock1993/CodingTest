def solution(numbers):
    numbers = list(map(str, numbers))
    arr = [[], [], [], [], [], [], [], [], [], []]
    for i in range(len(numbers)):
        if numbers[i][0] == '9':
            arr[0].append(numbers[i])
        elif numbers[i][0] == '8':
            arr[1].append(numbers[i])
        elif numbers[i][0] == '7':
            arr[2].append(numbers[i])
        elif numbers[i][0] == '6':
            arr[3].append(numbers[i])
        elif numbers[i][0] == '5':
            arr[4].append(numbers[i])
        elif numbers[i][0] == '4':
            arr[5].append(numbers[i])
        elif numbers[i][0] == '3':
            arr[6].append(numbers[i])
        elif numbers[i][0] == '2':
            arr[7].append(numbers[i])
        elif numbers[i][0] == '1':
            arr[8].append(numbers[i])
        elif numbers[i][0] == '0':
            arr[9].append(numbers[i])

    for i in range(len(arr)):
        arr[i] = sorted(arr[i], reverse=True)
        for j in range(len(arr[i])):

            if arr[i][j][-1] == '0':
                elem = arr[i][j]
                arr[i].remove(elem)
                arr[i].append(elem)
    res = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            res.append(arr[i][j])

    return ''.join(res)
