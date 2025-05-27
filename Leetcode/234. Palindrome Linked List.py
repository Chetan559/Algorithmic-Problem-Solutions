# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next or not head:
            return True
       
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # if fast.val != head.val:
        #     return False

        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
        