# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max = 0
        a = 0
        if not root:
            return max

        def find(root, a):
            nonlocal max
            if a > max: max = a
            if root.left:
                find(root.left, a + 1)
            if root.right:
                find(root.right, a + 1)

        find(root, a + 1)
        return max