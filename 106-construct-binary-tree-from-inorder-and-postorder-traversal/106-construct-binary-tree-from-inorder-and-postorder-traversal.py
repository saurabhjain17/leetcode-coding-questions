# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def rec(start,end):
            nonlocal post
            if start>end:
                return
            root_value=postorder[post]
            root=TreeNode(root_value)
            post-=1
            root.right=rec(inorder_map[root_value]+1,end)
            root.left=rec(start,inorder_map[root_value]-1)
            return root
        n=len(inorder)
        post=n-1
        inorder_map=dict()
        for i in range(n):
            inorder_map[inorder[i]]=i
        return rec(0,n-1)    