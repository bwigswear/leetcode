# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        temp1 = l1
        temp2 = l2

        digit = temp1.val + temp2.val + carry
        if digit > 9:
            carry = 1
            digit = digit % 10

        newhead = ListNode(digit)
        temp3 = newhead
        temp1 = temp1.next
        temp2 = temp2.next

        while temp1 != None or temp2 != None:
            temp3.next = ListNode()
            temp3 = temp3.next
            if temp1 == None:
                digit = temp2.val + carry
                if digit > 9:
                    carry = 1
                    digit = digit % 10
                else:
                    carry = 0
                temp3.val = digit
                temp2 = temp2.next
            elif temp2 == None:
                digit = temp1.val + carry
                if digit > 9:
                    carry = 1
                    digit = digit % 10
                else:
                    carry = 0
                temp3.val = digit
                temp1 = temp1.next
            else:
                digit = temp1.val + temp2.val + carry
                if digit > 9:
                    carry = 1
                    digit = digit % 10
                else:
                    carry = 0
                temp3.val = digit
                temp1 = temp1.next
                temp2 = temp2.next

        if carry == 1: temp3.next = ListNode(1)

        return newhead