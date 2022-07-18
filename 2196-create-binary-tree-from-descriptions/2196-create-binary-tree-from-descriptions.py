# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic=dict()
        seti=set()
        for u,v,child in descriptions:
            if u not in dic:
                dic[u]=TreeNode(u)
            if v not in dic:
                dic[v]=TreeNode(v)
            seti.add(v)    
            if child==1:
                dic[u].left=dic[v]
            else:
                dic[u].right=dic[v]
        for u,v,child in descriptions:
            if u not in seti:
                return dic[u]