class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [[0 for i in range(len(triangle[j]))]for j in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    continue
                if j==0:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j+1]) + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1]) + triangle[i][j]
        k = 0
        for j in range(len(triangle[len(triangle) - 1])):
            k = max(k,dp[len(triangle) - 1][j])
        return k