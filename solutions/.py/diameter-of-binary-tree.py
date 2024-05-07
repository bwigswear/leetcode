# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def dfs(root) -> (int, int):
            if root.left == None and root.right == None:
                return 0, 0
            elif root.right == None:
                height, diameter = dfs(root.left)
                return height + 1, max(height + 1, diameter)
            elif root.left == None:
                height, diameter = dfs(root.right)
                return height + 1, max(height + 1, diameter)
            else:
                heightleft, diameterleft = dfs(root.left)
                heightright, diameterright = dfs(root.right)
                return max(heightleft, heightright) + 1, max(heightleft + heightright + 2, max(diameterleft, diameterright))

        if not root: return 0
        height, diameter = dfs(root)
        return diameter