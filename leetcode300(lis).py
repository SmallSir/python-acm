class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = []
        for i in range(n):
            dp.append(1)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        ans = 0
        for i in range(n):
            ans = max(dp[i],ans)
        return ans
test = Solution()
print(test.lengthOfLIS([2,2]))