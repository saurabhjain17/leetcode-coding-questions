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
        n=1
        
        while q.empty() == False:
            
            sumi=0
            t=0
            for i in range (n):
                nod=q.get()
                sumi+=nod.val
                if nod.left:
                    q.put(nod.left)
                    t+=1
                if nod.right:
                    q.put(nod.right)
                    t+=1
            n=t       
        return sumi            