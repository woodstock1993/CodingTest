class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        len_1 = len(nums1)
        len_2 = len(nums2)
        half = (len_1 + len_2) / 2 - (len_1+len_2)//2
        state = ''

        if math.ceil(half) is 0:
            state = 'even'
        else:
            state = 'odd'
        index = int((len_1+len_2)//2)

        i, j = 0, 0

        while i < len_1 or j < len_2:
            if i == len_1 or j == len_2:
                if i == len_1 and j == len_2:
                    break
                elif i == len_1:
                    res.append(nums2[j])
                    j += 1
                elif j == len_2:
                    res.append(nums1[i])
                    i += 1
            elif nums1[i] >= nums2[j]:
                res.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            if i == index+1 or j == index+1:
                break

        if state == 'even':
            return (res[index-1] + res[index])/2
        elif state == 'odd':
            return res[index]
        return