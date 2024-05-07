# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2
        if not t1 and not t2: return None
        if not t1: return t2
        if not t2: return t1

        if t1.val < t2.val:
            head = t1
            t1 = t1.next
        else:
            head = t2
            t2 = t2.next

        temp = head

        while t1 or t2:
            if not t1 and not t2:
                return head
            elif not t1:
                temp.next = t2
                temp = temp.next
                t2 = t2.next
            elif not t2:
                temp.next = t1
                temp = temp.next
                t1 = t1.next
            else:
                if t1.val < t2.val:
                    temp.next = t1
                    temp = temp.next
                    t1 = t1.next
                else:
                    temp.next = t2
                    temp = temp.next
                    t2 = t2.next
        return head