"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        newhead = Node(head.val)
        temp = head
        temp2 = newhead
        d = {}
        d[head] = newhead
        while temp.next != None:
            temp2.next = Node(temp.next.val)
            temp2 = temp2.next
            temp = temp.next
            d[temp] = temp2

        temp = head
        temp2 = newhead

        while temp.next != None:
            if temp.random != None: temp2.random = d[temp.random]
            temp = temp.next
            temp2 = temp2.next
        
        if temp.random != None: temp2.random = d[temp.random]

        return newhead