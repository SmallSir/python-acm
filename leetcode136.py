class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1,len(nums) - 1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
