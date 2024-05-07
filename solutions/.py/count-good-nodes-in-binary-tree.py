# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        ret = 1

        def search(root, max):
            if not root: return None
            nonlocal ret
            if root.val >= max:
                ret += 1
                max = root.val
            search(root.left, max)
            search(root.right, max)

        search(root.left, root.val)
        search(root.right, root.val)

        return ret