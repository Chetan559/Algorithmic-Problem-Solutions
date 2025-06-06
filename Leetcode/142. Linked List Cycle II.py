# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            
            if slow == fast:
                slow = head
                new_slow = fast

                while new_slow != slow:
                    new_slow = new_slow.next
                    slow = slow.next
        
                # The point where slow and new_slow meet is the start of the cycle
                return slow

        return None