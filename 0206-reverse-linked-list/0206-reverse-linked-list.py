class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = newHead
            newHead = cur
            cur = tmp
        return newHead
    
        