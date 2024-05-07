# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        a = head
        while a != None:
            if a in seen: return True
            seen[a] = 1
            a = a.next
        
        return False