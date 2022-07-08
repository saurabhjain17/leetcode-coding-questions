# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,root,target):
        global ans
        if root is None:
            return
        target-=root.val
        if target==0:
            ans+=1
        self.rec(root.left,target)
        self.rec(root.right,target)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        global ans
        ans=0
        q=deque([root])
        while q:
            nod=q.popleft()
            if nod.left:
                q.append(nod.left)
            if nod.right:
                q.append(nod.right)
            self.rec(nod,targetSum)
        return ans    