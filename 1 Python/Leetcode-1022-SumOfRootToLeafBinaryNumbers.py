# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def solve(node,cache):
            if not node:
                return 0
            cache=cache*2+node.val
            if not node.left and not node.right:
                return cache
            return solve(node.left,cache)+solve(node.right,cache)

        return solve(root,0)
