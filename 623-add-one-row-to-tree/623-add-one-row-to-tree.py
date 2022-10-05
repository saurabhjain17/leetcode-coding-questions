# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            nod=TreeNode(val)
            nod.left=root
            return nod
        q=deque()
        q.append(root)
        dph=1
        while dph<depth-1:
            n=len(q)
            for i in range(n):
                nod=q.popleft()
                if nod.left:
                    q.append(nod.left)
                if nod.right:
                    q.append(nod.right)
            dph+=1
        print(q)    
        for nod in q:
           
                new_node=TreeNode(val)
                new_node.left=nod.left
                nod.left=new_node
            # if nod.right!=None:
                new_node=TreeNode(val)
                new_node.right=nod.right
                nod.right=new_node
        return root        