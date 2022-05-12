from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        dic=Counter(nums)
        op=[]
        def per(tem,ind,n,coun):
            if ind==n:
                op.append(tem.copy())
                return
            for i in coun:
                if coun[i]>0:
                    tem.append(i)
                    coun[i]-=1
                    per(tem,ind+1,n,coun)
                    tem.pop(-1)
                    coun[i]+=1
        per([],0,n,dic)
        return op
        
    