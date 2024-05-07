# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = True

        def check(r1, r2):
            nonlocal a
            if r1 == None and r2 == None: return
            if r1 == None or r2 == None: a = False; return
            if r1.val != r2.val: a = False; return
            check(r1.left, r2.left)
            check(r1.right, r2.right)

        check(p, q)
        return a