# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        pointer1 = head
        pointer2 = head.next
        pointer3 = head.next.next
        pointer2.next = pointer1
        pointer1.next = None
        
        
        while pointer3 != None:
            pointer1 = pointer2
            pointer2 = pointer3
            pointer3 = pointer3.next
            pointer2.next = pointer1

        return pointer2