# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        a = [[]]
        a[0] = [root.val]
        level = 0
        def traverse(root, level):
            nonlocal a
            if len(a) < level + 1:
                a.append([root.val])
            else:
                a[level].append(root.val)
            if root.left:
                traverse(root.left, level + 1)
            if root.right:
                traverse(root.right, level + 1)
            return
        
        if root.left:
            traverse(root.left, 1)
        if root.right:
            traverse(root.right, 1)

        return a