# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        if head.next == None and n == 1: return None
        length = 0
        find = head
        while find != None:
            length+=1
            find = find.next

        target = length - n + 1
        if target == 1: return head.next
        index = 0
        find = head
        while find != None:
            index+=1
            if index == target - 1:
                find.next = find.next.next
                return head
            find = find.next
        return head