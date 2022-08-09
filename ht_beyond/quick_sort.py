array = [i for i in range(100, -1, -1)]


def partition(arr, l, r):
    i = l-1
    pivot = arr[r]
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i, arr


def quick_sort(arr, l, r):
    if l < r:
        index, new_arr = partition(arr, l, r)

        quick_sort(new_arr, l, index - 1)
        quick_sort(new_arr, index+1, r)

    return arr


# print(quick_sort(array, 0, len(array)-1))
print(partition([9, 8, 7, 6, 4, 3, 2, 1, 5], 0, len([9, 8, 7, 6, 4, 3, 2, 1, 5])-1))
