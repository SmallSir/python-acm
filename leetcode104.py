class Solution:
    def maxDepth(self, root):
        n = len(root)
        for i in range(1,):
            if pow(2,i+1)-1 == n:
                return i
