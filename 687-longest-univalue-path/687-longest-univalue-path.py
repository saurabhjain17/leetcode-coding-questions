# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        global maxi
        maxi=1
        def rec(nod):
            global maxi
            if nod is None:
                return 0
            lh=rec(nod.left)
            rh=rec(nod.right)
            if lh>0 and rh>0 and nod.val==nod.left.val and nod.right.val==nod.val:
                maxi=max(maxi,lh+rh+1)
                return max(lh,rh)+1
            if lh>0 and nod.val==nod.left.val:
                maxi=max(maxi,lh+1)
                return lh+1
            if rh>0 and nod.val==nod.right.val:
                maxi=max(maxi,rh+1)  
                return rh+1
            return 1
        rec(root)
        return maxi-1