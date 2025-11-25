# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        carry = 0
        while l1 and l2:
            head.next = ListNode()
            sumation = l1.val + l2.val + carry
            head.next.val = sumation % 10
            carry = sumation // 10
            head = head.next
            l1, l2 = l1.next, l2.next
        while l1:
            head.next = ListNode()
            head.next.val = (l1.val + carry) % 10 
            carry = (l1.val + carry) // 10 
            head = head.next
            l1 = l1.next
        while l2:
            head.next = ListNode()
            head.next.val = (l2.val + carry) % 10 
            carry = (l2.val + carry) // 10 
            head = head.next 
            l2 = l2.next
        if carry:
            head.next = ListNode()
            head.next.val = carry
            head = head.next
        return dummy.next