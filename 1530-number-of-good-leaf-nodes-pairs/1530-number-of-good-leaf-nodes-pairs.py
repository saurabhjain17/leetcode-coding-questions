# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def ino(self,root,par):
        if root is None:
            return
        if root.left:
            par[root.left]=root
        if root.right:
            par[root.right]=root
        self.ino(root.left,par) 
        self.ino(root.right,par)
    def three_level_travse(self,nod,distance,par):
        global counti
        dis=1
        vis=set()
        qu=queue.Queue()
        if par[nod]!=-1:
            qu.put((par[nod],1))
            vis.add(par[nod])
        
        vis.add(nod)
        while qu.empty() is False and dis<=distance:
            ne,dis=qu.get()
            if dis<=distance and (ne.left is None and ne.right is None):
                counti+=1
            if ne.left and ne.left not in vis:
                qu.put((ne.left,dis+1))
                vis.add(ne.left)
            if ne.right and ne.right not in vis:
                qu.put((ne.right,dis+1))
                vis.add(ne.right)   
            if par[ne]!=-1 and par[ne] not in vis:
                qu.put((par[ne],dis+1))
                vis.add(par[ne])
        
    def countPairs(self, root: TreeNode, distance: int) -> int:
        par=dict()
        par[root]=-1
        self.ino(root,par)
        global counti
        counti=0
        q=queue.Queue()
        q.put(root)
        while q.empty() is False:
            nod=q.get()
            if not( nod.left or nod.right):
                self.three_level_travse(nod,distance,par)
            if nod.left:
                q.put(nod.left)
            if nod.right:
                q.put(nod.right)
        return counti//2        