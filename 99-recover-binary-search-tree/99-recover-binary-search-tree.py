# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    _pre=_fir=_sec=None
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        if Solution._pre!=None and root.val<Solution._pre.val:
            if Solution._fir==None:
                Solution._fir=Solution._pre
            Solution._sec=root
        Solution._pre=root    
        self.inorder(root.right)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        Solution._pre=None
        Solution._fir=None
        Solution._sec=None
        self.inorder(root)
        t=Solution._fir.val
        Solution._fir.val=Solution._sec.val
        Solution._sec.val=t
        
        