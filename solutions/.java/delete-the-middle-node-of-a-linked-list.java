/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if(head.next == null){return null;}
        if(head.next.next == null){head.next = null; return head;}
        ListNode t1 = head;
        ListNode t2 = head.next;
        while(true){
            if(t2.next == null){break;}
            if(t2.next.next == null){break;}
            t1 = t1.next;
            t2 = t2.next.next;
        }
        t1.next = t1.next.next;
        return head;

    }
}