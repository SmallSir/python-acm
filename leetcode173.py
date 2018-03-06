class Solution:
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                print(num)
                return
s = Solution()
s.singleNumber([1])