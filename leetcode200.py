class Solution:
    dix = [1,0,-1,0]
    diy = [0,1,0,-1]
    check = []
    def dfs(self,x,y,n,m,grid):
        self.check[x][y] = 1
        for i in range(4):
            dx = self.dix[i] + x
            dy = self.diy[i] + y
            if dx <= n - 1 and dx >=0 and dy <= m - 1 and dy >= 0 and self.check[dx][dy] == 0 and grid[dx][dy] == '1':
                self.dfs(dx,dy,n,m,grid)
        return
    def numIslands(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        sum = 0
        self.check = [[0 for i in range(m)]for j in range(n)]
        for i in range(n):
            for j in range(m):
                if self.check[i][j] == 0 and grid[i][j] == '1':
                    self.dfs(i,j,n,m,grid)
                    sum += 1
        return sum
