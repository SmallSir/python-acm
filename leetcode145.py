class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dp = []
        def dfs(x):
            if x == None:
                return
            else:
                dfs(x.left)
                dfs(x.right)
                dp.append(x.val)
        dfs(root)
        return dp