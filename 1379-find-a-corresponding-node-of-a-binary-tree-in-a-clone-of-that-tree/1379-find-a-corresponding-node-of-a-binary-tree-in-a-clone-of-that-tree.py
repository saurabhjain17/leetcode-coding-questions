# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, ori: TreeNode, clo: TreeNode, target: TreeNode) -> TreeNode:
        st1=[]
        st2=[]
       
            
        
        while ori or st1:
            if ori:
                if ori==target:
                    return clo
                st1.append(ori)
                st2.append(clo)
                ori=ori.left
                clo=clo.left
            else:
                ori=st1.pop(-1)
                clo=st2.pop(-1)
                if ori ==target:
                    return clo
                ori=ori.right
                clo=clo.right
        