from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n=len(nums)
        dic=Counter(nums)
        maxi=0
        for i in nums:
            if (i+1) in dic:
                maxi=max(maxi,dic[i]+dic[i+1])
        return maxi        
        