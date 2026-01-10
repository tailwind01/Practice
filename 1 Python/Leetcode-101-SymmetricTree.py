# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solver function defined in environment

def mirrorImage(l, r): 
    if not l and not r:
        # both dont exist
        return 1==1
    if (not l or not r) or (l.val != r.val):
        return 1==0
    # to make function dependent upon itself again and again before final resolve
    return mirrorImage(l.left, r.right) and mirrorImage(l.right, r.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: #trivial case dealing
            return 1==1
        else:
            l = root.left
            r = root.right
            return mirrorImage(l,r)
