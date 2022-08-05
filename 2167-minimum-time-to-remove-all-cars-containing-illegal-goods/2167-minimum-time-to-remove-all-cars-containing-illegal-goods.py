class Solution:
    def minimumTime(self, s: str) -> int:
        if len(s)==1:
            if s=="1":
                return 1
            return 0
        cost=s.count("1")*2
        if cost==0:
            return cost
        counti=0
        left=[]
        n=len(s)
        for i in range(n):
            if s[i]=="1":
                counti+=1
            else:
                counti-=1
            left.append(counti)
        right=[]
        counti=0
        # x=s[::-1]
        for i in range(n-1,-1,-1):
            if s[i]=="1":
                counti+=1
            else:
                counti-=1
            right.append(counti)
        for i in range(1,n):
            left[i]=max(left[i-1],left[i])
        for i in range(1,n):
            right[i]=max(right[i-1],right[i])    
        right=right[::-1]
        # print(left)
        # print(right)
        maxi=0
        for i in range(n-1):
            maxi=max(max(0,left[i])+max(0,right[i+1]),maxi)
        return cost-maxi    
#     def minimumTime(self, A: str) -> int:
#         n = len(A)
#         if n == 1: return 1 if A == '1' else 0
#         lft, rgt = [] * n, [] * n
        
#         curr = 0
#         for a in A:
#             if a == '1':
#                 curr += 1
#             else:
#                 curr -= 1
#             lft.append(curr)
            
#         curr = 0
#         for a in A[::-1]:
#             if a == '1':
#                 curr += 1
#             else:
#                 curr -= 1
#             rgt.append(curr)
#         rgt.reverse()

#         exp = 2 * A.count('1')   # MaximumCost, that is the cost of removing all cars with a cost of 2.
            
#         lmax, curr = [lft[0]], lft[0]
#         for i in range(1, n):
#             curr = max(curr, lft[i])
#             lmax.append(curr)
            
#         rmax, curr = [rgt[-1]], rgt[-1]
#         for i in range(n - 2, -1, -1):
#             curr = max(curr, rgt[i])
#             rmax.append(curr)            
#         rmax.reverse()
        
#         maxp = 0  # The maximum cost we can SAVE.
#         for i in range(n - 1):
#             maxp = max(maxp, max(0, lmax[i]) + max(0, rmax[i + 1]))

#         return exp - maxp  # The ove