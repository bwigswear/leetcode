# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists: return None

        def m(list1, list2):
            if list1 == None: 
                return list2
            elif list2 == None:
                return list1
            else:
                if list1.val > list2.val:
                    head = list2
                    list2 = list2.next
                else:
                    head = list1
                    list1 = list1.next
                traverse = head
                while list1 != None or list2 != None:
                    if list1 == None:
                        traverse.next = list2
                        list2 = list2.next
                        traverse = traverse.next
                    elif list2 == None:
                        traverse.next = list1
                        list1 = list1.next
                        traverse = traverse.next
                    elif list1.val < list2.val:
                        traverse.next = list1
                        list1 = list1.next
                        traverse = traverse.next
                    else:
                        traverse.next = list2
                        list2 = list2.next
                        traverse = traverse.next
            return head

        while len(lists) > 1:
            newlists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i > len(lists) - 2:
                    list2 = None
                else:
                    list2 = lists[i+1]
                newlists.append(m(list1, list2))
            lists = newlists
        
        return lists[0]
        
        
        
        
        
        """if not lists: return None
        if len(lists) == 1: return lists[0]

        for i in range(len(lists) - 1, -1, -1):
            if lists[i] == None:
                lists.pop(i)

        def find(heads):
            min = -1
            for i in range(len(heads)):
                if min == -1:
                    min = i
                elif heads[i].val < heads[min].val:
                    min = i

            if min == -1: return None

            ret = heads[min]
            if ret.next == None:
                heads.pop(min)
            else:
                heads[min] = ret.next
            return ret

        head = find(lists)
        traverse = head

        while(len(lists)) > 0:
            traverse.next = find(lists)
            traverse = traverse.next

        return head"""