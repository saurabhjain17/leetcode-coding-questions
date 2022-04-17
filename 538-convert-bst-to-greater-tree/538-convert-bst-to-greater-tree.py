# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bst(self,root):
        global sumi
        if root is None:
            return 0
        self.bst(root.right)
        sumi+=root.val
        root.val=sumi
        self.bst(root.left)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        global sumi
        sumi=0
        self.bst(root)
        return root
    
        