# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def comp(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val == root2.val:
                return comp(root1.left, root2.left) and comp(root1.right, root2.right)
            else:
                return False
        
        def search(root):
            nonlocal subRoot
            if not root: return False
            if root.val == subRoot.val:
                if comp(root, subRoot):
                    return True
            return search(root.left) or search(root.right)
        
        return search(root)