class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dp = []
        def dfs(x):
            if x==None:
                return
            else:
                dfs(x.left)
                dp.append(x.val)
                dfs(x.right)
        dfs(root)
        return dp