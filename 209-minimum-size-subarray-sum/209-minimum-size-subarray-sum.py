import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         using binary search in o(n)log(n)
        # def tar(pre,i,n,pr):
        #     l=i
        #     h=n-1
        #     if pre[h]<pr:
        #         return math.inf
        #     out=math.inf
        #     while l<=h:
        #         m=(l+h)//2
        #         if pre[m]==pr:
        #             return m
        #         elif pre[m]>pr:
        #             out=m
        #             h=m-1
        #         else:
        #             l=m+1
        #     return out        
        # n=len(nums)
        # pre=[0]*n
        # pre[0]=nums[0]
        # for i in range(1,n):
        #     pre[i]=pre[i-1]+nums[i]
        # mini=math.inf
        # for i in range(n):
        #     if i==0:
        #         pr=target
        #     else:
        #         pr=target+pre[i-1]
        #     mini=min(mini,tar(pre,i,n,pr)-i+1)    
        # if mini==math.inf:
        #     return 0
        # return mini
        
        n=len(nums)
        ans=math.inf
        i=0
        j=0
        sumi=0
        while j<n and i<n:
            sumi+=nums[j]
            while sumi>=target:
                ans=min(j-i+1,ans)
                sumi-=nums[i]
                i+=1
            j+=1
        if ans==math.inf:
            return 0
        return ans
                