# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        s = head.next
        sieve = 0

        while s:
            if s.val != 0:
                sieve += s.val
            else:
                t.val = sieve
                sieve = 0
                if s.next:
                    t.next = s
                    t = t.next    
            s = s.next
        t.next = None

        return head
