import bisect as b
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        aslist = []
        
        
        while l1:
                aslist.append(l1.val)
                l1 = l1.next
                
        while l2:
            b.insort(aslist,l2.val)
            l2 = l2.next
        
        ansLN = ListNode()
        holder = ansLN
        
        for m in range(len(aslist)):
            holder.next = ListNode(aslist[m])
            holder = holder.next
        return ansLN.next
        