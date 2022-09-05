class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numbers = 1
        zero_cnt = 0
        new_arr = []

        for i in range(len(nums)):
            if nums[i] != 0:
                numbers *= nums[i]
            else:
                zero_cnt += 1

        if zero_cnt == 0:
            for i in range(len(nums)):
                new_arr.append(int(numbers / nums[i]))
        elif zero_cnt == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    new_arr.append(0)
                else:
                    new_arr.append(numbers)
        elif zero_cnt > 1:
            new_arr = [0 for _ in range(len(nums))]

        return new_arr