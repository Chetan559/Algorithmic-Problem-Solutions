# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = new_node
            new_node = curr
            curr = next_node

        return new_node
        