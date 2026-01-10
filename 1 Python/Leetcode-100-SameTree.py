# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
          #non existence of both
             return True
        
        if not p or not q:
         #non existence of either
            return False

        if p.val!= q.val:
         #inequality
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)#adjacent values checking using the same function so that final resolution of the function is clear
