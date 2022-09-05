class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        maxs = 0
        startIndex = None
        length = len(nums)

        for i in range(length):
            if nums[i] >= 0:
                startIndex = i
                break

        if startIndex == None:
            return max(nums)

        for i in range(startIndex, length):
            sums += nums[i]
            if sums > maxs:
                maxs = sums

            if sums < 0:
                sums = 0

        return maxs
