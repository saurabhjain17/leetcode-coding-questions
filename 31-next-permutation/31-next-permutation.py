class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                t=i
                break
        if t==-1:
            nums= nums.reverse()
            return nums
        else:
            end=-1
            for i in range(n-1,t,-1):
                if nums[i]>nums[t]:
                    end=i
                    break
            nums[t],nums[end]=nums[end],nums[t]
            j=n-1
            i=t+1
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            return nums    
#             print(nums[:t+1])
#             p=nums[t+1:][::-1]
           
            
#             print(p)
#             nums=nums[:t+1]+p
#             print( nums)
#             return nums
            # if len(p)==0:
            #     p=[]
            # p=p.reverse()
            # return nums[:t+1]+p
        
        