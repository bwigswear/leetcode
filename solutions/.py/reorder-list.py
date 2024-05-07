# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None: 
            return None
        length = 1
        tail = head
        while tail.next != None:
            tail = tail.next
            length+=1

        if length == 1: return head

        def traverse(head: ListNode):
            temp = head
            while temp.next.next != None:
                temp = temp.next
            temp2 = temp.next
            temp.next = None
            return temp2

        temp = head

        index = 0

        while index < length // 2:
            splice = traverse(temp)
            splice.next = temp.next
            temp.next = splice
            temp = temp.next.next
            index+=1

        return head