class Solution:
    def dominantIndex(self, nums):
        MAX = 0
        for i in range(len(nums)):
            if MAX < nums[i]:
                index = i
                MAX = nums[i]
        for i in range(len(nums)):
            if index == i:
                continue
            if MAX < nums[i] * 2:
                return -1
        return index
