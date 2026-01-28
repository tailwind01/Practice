import math as m
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traversal = head
        while traversal and traversal.next:
            a = traversal.val
            b = traversal.next.val
            computed = m.gcd(a,b)
            nn = traversal.next
            traversal.next = ListNode(computed,nn)
            traversal = nn
        
        return head
