class Solution(object):
    def rob(self, nums):
        dp = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)+1):
            dp.append(0)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1,len(nums)):
            dp[i+1] = max(dp[i],dp[i-1] + nums[i])
        return dp[len(nums)]

test = Solution()
print(test.rob([2,3,2]))
"""
        :type nums: List[int]
        :rtype: int
        """
