# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, fst: Optional[ListNode], snd: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy

        while fst is not None and snd is not None:
            if fst.val < snd.val:
                curr.next = ListNode(fst.val)
                fst = fst.next
                curr = curr.next
            else:
                curr.next = ListNode(snd.val)
                snd = snd.next
                curr = curr.next

        if fst is not None:
            curr.next = fst
        else:
            curr.next = snd

               
        return dummy.next