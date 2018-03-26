class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrder(self, root):
        tree = []
        def dfs(flag,deep):
            if flag == None:
                return
            if len(tree) < flag + 1:
                tree.append([])
            dfs(flag.left,deep+1)
            dfs(flag.right,deep+1)
        dfs(root,0)
        return tree