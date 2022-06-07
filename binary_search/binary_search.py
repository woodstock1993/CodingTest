"""
    이진탐색 구현하기
"""

def binary_search(start, end, array, target):
    if start >= end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(start, mid-1, array, target)
    else:
        return binary_search(mid+1, end, array, target)

    return mid


array = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(0, len(array)-1, array, 6))