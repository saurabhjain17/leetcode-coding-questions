# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global counti
        counti=0
        def rec(nod,maxi):
            global counti
            if nod is None:
                return
            if nod.val>=maxi:
                counti+=1
                maxi=nod.val
            rec(nod.left,maxi)
            rec(nod.right,maxi)
        rec(root,-100000)
        return counti