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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        q=deque([root])
        length=1
        while q:
            n=length
            for _ in range(n):
                nod=q.popleft()
                length-=1
                if nod.left:
                    q.append(nod.left)
                    length+=1
                if nod.right:
                    q.append(nod.right)
                    length+=1
                   
            for ind in range(length-1):
                q[ind].next=q[ind+1]
        return root         