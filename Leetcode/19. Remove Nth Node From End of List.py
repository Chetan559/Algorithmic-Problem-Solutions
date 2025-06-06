# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = None
            return head
        
        fast = slow = slow_prev = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast:
            slow_prev = slow
            slow = slow.next
            fast = fast.next

        slow_prev.next = slow.next

        return head