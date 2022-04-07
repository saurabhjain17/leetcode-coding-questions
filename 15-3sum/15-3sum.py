class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if n<3:
            return []
        nums.sort()
      
        i=0
        output=[]
        while i<n:
            left=i+1
            right=n-1
            while left<right:
                # print(nums[left],nums[right],nums[i])
                if nums[left]+nums[right]==-nums[i]:
                    output.append([nums[i],nums[left],nums[right]])
                    k=left+1
                    while k<= right and nums[k]==nums[left]:
                              k+=1
                    left=k
                    k=right-1
                    while k>= left and nums[k]==nums[right]:
                              k-=1
                    right=k
                elif nums[left]+nums[right]<-nums[i]:  
                    left+=1
                else:
                    right-=1
            k=i+1
            while k<n and nums[k]==nums[i]:
                k+=1
            i=k
        return output 