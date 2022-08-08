from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            nums[i]-=i
        dic=Counter(nums)
        total=(n*(n-1))//2
        for i in dic:
            total-=((dic[i]*(dic[i]-1))//2)
        return int(total)    