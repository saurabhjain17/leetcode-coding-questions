# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        dic={i:0 for i in range(10)}
        global ans
        ans=0
        def rec(nod):
            global ans
            # if nod is None:
            #     counti=0
            #     for i in dic:
            #         if dic[i]%2==1:
            #             counti+=1
            #     if counti<2:
            #         print(dic)
            #         ans+=1
            #     return
            if nod.left is None and nod.right is None:
                dic[nod.val]+=1
                counti=0
                for i in dic:
                    if dic[i]%2==1:
                        counti+=1
                if counti<2:
                    print(dic)
                    ans+=1
                dic[nod.val]-=1
                return
                
            dic[nod.val]+=1
            if nod.left:
                rec(nod.left)
            if nod.right:    
                rec(nod.right)
            dic[nod.val]-=1
            
            
        rec(root)     
        return ans            