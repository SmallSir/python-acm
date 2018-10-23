# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    asd = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []
        def dfs(x):
            if x == None:
                return
            else:
                tree.append(x.val)
            dfs(x.left)
            dfs(x.right)
        dfs(root)
        return tree





