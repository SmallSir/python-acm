class Solution:
    def calculateMinimumHP(self, dungeon):
        cost = [[]]
        n = len(dungeon)
        m = len(dungeon[0])
        if n == 1 and m == 1:
            if dungeon[0][0] <= 0:
                return abs(dungeon[0][0]) + 1
            else:
                return 1
        cost =[[0 for col in range(m+1)] for row in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                cost[i][j] = 1000000
        cost[n][m - 1] = 1
        cost[n - 1][m] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                #print(cost[i][j+1],cost[i+1][j],dungeon[i][j])
                cost[i][j] = min(cost[i][j+1], cost[i+1][j]) - dungeon[i][j]
                if cost[i][j] <= 0:
                    cost[i][j] = 1
        return cost[0][0]

test = Solution()
print(test.calculateMinimumHP([[0,-3]]))
print(test.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))