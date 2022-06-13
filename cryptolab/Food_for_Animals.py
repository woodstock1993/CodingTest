n = int(input())
arr =[]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    a = arr[i][0]
    b = arr[i][1]
    c = arr[i][2]
    x = arr[i][3]
    y = arr[i][4]

    dog_remain = x-a

    if dog_remain < 0:
        dog_remain = 0
    cat_remain = y-b

    if cat_remain < 0:
        cat_remain = 0

    answer = dog_remain + cat_remain - c

    if answer <= 0:
        print('YES')
    else:
        print('NO')




