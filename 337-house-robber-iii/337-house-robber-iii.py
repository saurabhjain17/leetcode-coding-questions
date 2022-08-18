# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        def rec(node):
            global ans
            if node is None:
                return 0,0
            ll,lc=rec(node.left)
            rl,rc=rec(node.right)
            ans=max(ans,rl+ll+node.val,lc+rc)
            pc=max(ll+rl++node.val,lc+rc)
            pl=lc+rc
            return pl,pc
        rec(root)
        return ans