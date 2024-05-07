# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def findheight(root):
            if not root: return 0
            return max(1 + findheight(root.left), 1 + findheight(root.right))

        def isBalanced(root):
            if not root: return True
            if abs(findheight(root.left) - findheight(root.right)) > 1:
                return False
            else:
                return isBalanced(root.right) and isBalanced(root.left)

        return isBalanced(root)