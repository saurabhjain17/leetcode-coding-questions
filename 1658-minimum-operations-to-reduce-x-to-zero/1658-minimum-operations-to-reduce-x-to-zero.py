class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sui=0
        
        maxi=-1
        if sum(nums)<x:
            return -1
        op=sum(nums)-x
        i=j=0
        n=len(nums)
        while (i<=j and j<n and i<n) or sui>=op :
            if sui==op:
                maxi=max(j-i,maxi)
                sui-=nums[i]
                i+=1
            elif sui<op:
                sui+=nums[j]
                j+=1
            else:
                sui-=nums[i]
                i+=1
        if maxi==-1:
            return -1
        return n-maxi
                