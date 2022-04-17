class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=[-1,-1]
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]>target:
                end=mid-1
            elif  nums[mid]<target:
                start=mid+1
            else:
                if (mid==0 or nums[mid]!=nums[mid-1] ) :
                    x[0]=mid
                    break
                else:
                      end=mid-1   

                    
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]>target:
                end=mid-1
            elif  nums[mid]<target:
                start=mid+1
            else:
                if (mid==len(nums)-1 or nums[mid]!=nums[mid+1] ) :
                    x[1]=mid
                    break  
                else:
                    start=mid+1
        return x            