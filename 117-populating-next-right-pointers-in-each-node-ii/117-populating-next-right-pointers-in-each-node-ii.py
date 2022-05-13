"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        root.next=None
        q=[root]
        while q:
            n=len(q)
            for i in range(n-1):
                q[i].next=q[i+1]
            q[-1].next=None
            for i in range(n):
                nod=q.pop(0)
                if nod.left:
                    q.append(nod.left)
                if nod.right:
                    q.append(nod.right)
        return root            
                