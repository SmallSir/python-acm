class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        k = []
        for i in range(n):
            for j in range(i+1,n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        for i in range(n):
            matrix[i].reverse()
        print(matrix)
test = Solution()
print(test.rotate([[1,2,3],[4,5,6],[7,8,9]]))