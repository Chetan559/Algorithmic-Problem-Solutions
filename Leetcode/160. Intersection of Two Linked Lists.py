# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        A, B = headA, headB
        flagA = flagB = 0

        while A or B:
            if A == B:
                return A
            A, B = A.next, B.next

            if not A and flagA == 0:
                A = headB
                flagA = 1
        
            if not B and flagB == 0:
                B = headA
                flagB = 1
        
        return None