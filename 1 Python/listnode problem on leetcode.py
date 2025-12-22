import bisect as b

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ansList = []
        
        for l in lists:
            while l:
                b.insort(ansList,l.val)
                l = l.next
        finalAns = ListNode()
        binT = finalAns
        for j in range(len(ansList)):
            binT.next = ListNode(ansList[j])
            binT = binT.next
        
        return finalAns.next