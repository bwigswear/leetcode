# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        layer = 0
        direction = 0
        a = {}

        def search(root, layer, a):
            if not root: return
            if layer not in a: 
                a[layer] = root.val
            if root.right: search(root.right, layer + 1, a)
            if root.left: search(root.left, layer + 1, a)
        
        search(root, 0, a)
        ret = []
        i = 0
        while i in a:
            ret.append(a[i])
            i+=1
        return ret