#0 ms using list comprehension
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [order[x] for x in range(len(order)) if order[x] in friends]
        
