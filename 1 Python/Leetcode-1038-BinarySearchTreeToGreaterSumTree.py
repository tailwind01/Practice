# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        def movement(TreeNode):
            if not TreeNode:
                return
            movement(TreeNode.right)
            self.sum += TreeNode.val
            TreeNode.val = self.sum
            movement(TreeNode.left)
        movement(root)
        return root
