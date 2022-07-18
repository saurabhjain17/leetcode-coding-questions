class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        mini=min(numsDivide)
        seti=set(numsDivide)
        dic=Counter(nums)
        nums=list(set(nums))
        nums.sort()
        ans=0
        for i in nums:
            if i>mini:
                break
            flag=0
            for j in seti:
                if j%i!=0:
                    flag=1
                    break
            if flag==0:
                return ans
            if flag==1:
                ans+=dic[i]
        return -1       