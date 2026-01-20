class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nh, t, c = None, None, head
        while c:
            t = c.next
            c.next = nh
            nh = c
            c = t
        return nh
    
        