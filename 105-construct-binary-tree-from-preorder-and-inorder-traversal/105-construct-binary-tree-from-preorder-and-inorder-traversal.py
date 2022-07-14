# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,start,end,preorder,inorder,inorder_index_map):
        global pre
        if start>end:
            return
        # if start==end:
        #     pre+=1
        #     return TreeNode(inorder[start])
        tem_value=preorder[pre]
        tem=TreeNode(tem_value)
        pre+=1
        tem.left=self.rec(start,inorder_index_map[tem_value]-1,preorder,inorder,inorder_index_map )
        tem.right=self.rec(inorder_index_map[tem_value]+1,end,preorder,inorder,inorder_index_map )
        return tem
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        if n==1:
            return TreeNode(preorder[0])
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        global pre
        pre=0
        head=self.rec(0,n-1,preorder,inorder,inorder_index_map )
        # head=TreeNode(preorder[0])
        # pre+=1
        # mid=inorder.index(preorder[0])
        # head.left=self.rec(0,mid-1,preorder,inorder)
        # head.right=self.rec(mid+1,n-1,preorder,inorder)
        return head