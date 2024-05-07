# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        if k == 2:
            temp = head.next.next
            head.next.next = head
            ret = head.next
            head.next = temp
            return ret
        else:
            i = 0
            t1 = head
            t2 = head.next
            t3 = head.next.next
            while i < k - 2:
                t2.next = t1
                t1 = t2
                t2 = t3
                t3 = t3.next
                i+=1
            t2.next = t1
            head.next = t3
            return t2

    def check(self, head, k):
        traverse = head
        i = 0
        while i < k:
            if not traverse:
                return False
            traverse = traverse.next
            i+=1
        return True

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        if self.check(head, k):
            head = self.reverse(head, k)
            traverse = head
        else:
            return head

        for i in range(k - 1):
            traverse = traverse.next

        while self.check(traverse.next, k):
            traverse.next = self.reverse(traverse.next, k)
            for i in range(k):
                traverse = traverse.next

        return head