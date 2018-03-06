class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        del nums[k:]
        return len(nums)

test = Solution()
test.removeElement([3,2,2,3],
3)