class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n=len(mapping)
        m=len(nums)
        dic=dict()
        
        for num in nums:
            tem=num
            if tem==0:
                ne=str(mapping[0])
            else: 
                ne=""
                while tem>0: 
                    ne=str(mapping[tem%10])+ne
                    tem//=10
            ne=int(ne)
            if ne not in dic:
                dic[ne]=[]
            dic[ne].append(num)
        lis=list(dic.keys())
        lis.sort()
        ans=[]
        for num in lis:
            ans+=dic[num]
        return ans    