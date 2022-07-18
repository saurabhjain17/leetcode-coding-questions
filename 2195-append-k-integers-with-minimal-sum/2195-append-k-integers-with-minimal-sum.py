class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums=list(set(nums))
        nums.sort()
        n=len(nums)
        if nums[0]-1>=k:
            return int(k*(k+1)//2)
        total=int((nums[0]-1)*(nums[0])//2)
        # print(nums)
        # print(total)
        k-=(nums[0]-1)
        for i in range(1,n):
            
                
            tem=nums[i]-nums[i-1]-1
            if tem==0 or k<=0:
                continue
            if tem<=k:
                k-=tem
                total+=int(((nums[i])*(nums[i]-1)/2)-((nums[i-1]+1)*(nums[i-1])/2))
            else:
                total+=int(((nums[i-1]+k)*(nums[i-1]+k+1)/2)-((nums[i-1]+1)*(nums[i-1])/2))
                k=0
                return total
                break
            # print(total,i)
        # while i<n and k>0:
        #     if nums[i]==val:
        #         i+=1
        #         val+=1
        #     else:
        #         total+=val
        #         val+=1
        #         k-=1
        if k==0:
            return total
        total+=int(((nums[-1]+k+1)*(nums[-1]+k)/2)-((nums[-1])*(nums[-1]+1)/2))
        return total