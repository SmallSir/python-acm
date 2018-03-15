class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        for i in range(len(nums)):
            if i == 0 and nums[i] >target:
                return i
            elif i == len(nums) - 1 and nums[i] < target:
                return len(nums)
            else:
                if nums[i] >= target and nums[i - 1] < target:
                    return i
