# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack=[]
        seti=set([str(i) for i in range(10)])
        digit=""
        n=len(traversal)
        i=0
        while i<n and traversal[i] in seti:
            digit+=traversal[i]
            i+=1
            ind=i
        i=ind    
        root=TreeNode(int(digit))
        stack.append((root,0))
        tem=root
        level=0
        while i<n:
            lev=0
            while i<n and traversal[i]=="-":
                lev+=1
                i+=1
            digit=""
            while i<n and traversal[i] in seti:
                digit+=traversal[i]
                i+=1
            if lev==level+1:
                tem.left=TreeNode(int(digit))
                stack.append((tem.left,lev))
                tem=tem.left
                level=lev
            else:
                tem,level=stack.pop(-1)
                while level+1!=lev:
                    tem,level=stack.pop(-1)
                tem.right=TreeNode(int(digit))
                stack.append((tem.right,lev))
                level=lev
                tem=tem.right
        return root         
                