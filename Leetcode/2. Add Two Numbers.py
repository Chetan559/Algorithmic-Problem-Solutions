# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        carry = 0

        while l1 and l2:
            if carry == 0:
                digit_sum = l1.val + l2.val
            else:
                digit_sum = l1.val + l2.val + 1
                carry = 0
            
            if digit_sum >= 10: 
                digit_sum = digit_sum % 10
                carry = 1

            l1, l2 = l1.next, l2.next
            curr.next = ListNode(digit_sum)
            curr = curr.next
        
        if not l1:
            while l2:
                digit_sum = l2.val + carry
                if digit_sum >= 10: 
                    digit_sum = digit_sum % 10
                    carry = 1
                else:
                    carry = 0
                l2 = l2.next
                curr.next = ListNode(digit_sum)
                curr = curr.next
        else:
            while l1:
                digit_sum = l1.val + carry
                if digit_sum >= 10: 
                    digit_sum = digit_sum % 10
                    carry = 1
                else:
                    carry = 0
                l1 = l1.next
                curr.next = ListNode(digit_sum)
                curr = curr.next
        
        if carry == 1:
            curr.next = ListNode(1)
            
        return dummy.next