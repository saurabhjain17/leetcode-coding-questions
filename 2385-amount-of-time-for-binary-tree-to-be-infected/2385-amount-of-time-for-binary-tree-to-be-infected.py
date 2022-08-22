# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        par={root:-1}
        que=deque()
        que.append(root)
        fin_nod=-1
        while que:
            nod=que.popleft()
            if nod.val==start:
                fin_nod=nod
            if nod.left:
                par[nod.left]=nod
                que.append(nod.left)
            if nod.right:
                par[nod.right]=nod
                que.append(nod.right)
        que=deque()
        que.append(fin_nod)
        time=-1
        vis=set()
        vis.add(fin_nod)
        while que:
            time+=1
            n=len(que)
            for i in range(n):
                nod=que.popleft()
                if nod.left and nod.left not in vis:
                    que.append(nod.left)
                    vis.add(nod.left)
                if nod.right and nod.right not in vis:
                    que.append(nod.right)
                    vis.add(nod.right)
                if par[nod]!=-1 and par[nod] not in vis:
                    que.append(par[nod])
                    vis.add(par[nod])
        return time             
                