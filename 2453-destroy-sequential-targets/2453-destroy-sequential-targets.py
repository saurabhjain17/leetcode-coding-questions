class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mp=dict()
        mx=-1
        for i in nums:
            k=i%space
            if k not in mp:
                mp[k]=0
            mp[k]+=1
            mx=max(mx,mp[k])
        ans=1e10
        for i in nums:
            if mx==mp[i%space]:
                ans=min(ans,i)
        return ans        
            