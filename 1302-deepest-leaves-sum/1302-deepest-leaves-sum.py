# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q= queue.Queue()
        q.put(root)
        sumi=0
        while q.empty() == False:
            n=q.qsize()
            sumi=0
            for i in range (n):
                nod=q.get()
                sumi+=nod.val
                if nod.left:
                    q.put(nod.left)
                if nod.right:
                    q.put(nod.right)
        return sumi            