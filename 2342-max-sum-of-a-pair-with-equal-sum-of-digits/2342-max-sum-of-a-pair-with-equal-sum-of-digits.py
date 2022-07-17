class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic=dict()
        for i in nums:
            x=i
            total=0
            while x>0:
                total+=x%10
                x//=10
            if total not in dic:
                dic[total]=[i]
            else:
                if len(dic[total])<2:
                    dic[total].append(i)
                else:
                    maxi=max(dic[total])
                    mini=min(dic[total])
                    dic[total]=[maxi,max(i,mini)]
        ans=-1
        for i in dic:
            if len(dic[i])>1:
                ans=max(ans,sum(dic[i]))
        return ans    
                        