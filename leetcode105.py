class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right
class Solution:
    tree = []
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root_data = preorder[0]
        for i in range(len(inorder)):
            if root_data == inorder[i]:
                break
        left = self.buildTree(preorder[1:i+1],inorder[:i])
        right = self.buildTree(preorder[i+1:],inorder[i+1:])
        self.tree.append(root_data)
        self.tree.append(left)
        self.tree.append(right)
test = Solution()
print(test.buildTree([3,9,20,15,7],
[9,3,15,20,7]))