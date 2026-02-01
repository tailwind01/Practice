# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        rsum_v = 0
        if low<=root.val<=high:
            rsum_v+=root.val
        if root.val>low:
            rsum_v+=self.rangeSumBST(root.left, low, high) #checking leftsubarray
        if root.val<high:
            rsum_v+=self.rangeSumBST(root.right, low, high) #checking rightsubarray
        
        return rsum_v
