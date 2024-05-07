# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(root, p, q):
            a = root.val
            if a > p and a < q:
                return root
            elif a > q and a < p:
                return root
            elif a == p or a == q:
                return root
            elif a < p and a < q:
                return search(root.right, p, q)
            else:
                return search(root.left, p, q)

        return search(root, p.val, q.val)