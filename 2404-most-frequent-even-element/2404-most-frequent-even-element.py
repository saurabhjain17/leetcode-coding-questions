from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic=Counter(nums)
        ans=-1
        freq=0
        for i in dic:
            if i%2==0 :
                if dic[i]>freq:
                    ans=i
                    freq=dic[i]
                elif dic[i]==freq:
                    ans=min(ans,i)
        return ans            