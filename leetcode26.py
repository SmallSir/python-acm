class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                k+=1
                nums[k] = nums[i]
        del nums[k+1:]
        return len(nums)

