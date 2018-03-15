class Solution:
    def uniquePaths(self, m, n):
        dp = [[0 for i in range(n)]for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == m - 1 and j == n - 1:
                    continue
                elif i == m - 1:
                    dp[i][j+1] += dp[i][j]
                elif j == n - 1:
                    dp[i+1][j] += dp[i][j]
                else:
                    dp[i][j + 1] += dp[i][j]
                    dp[i + 1][j] += dp[i][j]
        return dp[m-1][n-1]
test = Solution()
test.uniquePaths(1,2)