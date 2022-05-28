class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        tem=set(nums)
        for i in zip(*nums):
            x=list(i)
            ans=''.join(x)
            if ans not in  tem:
                return ans
        for i in range(n+2):    
            p=bin(i)[2:]
            x=len(p)
         
            p="0"*(n-x)+p
            if p not in tem:
                return p