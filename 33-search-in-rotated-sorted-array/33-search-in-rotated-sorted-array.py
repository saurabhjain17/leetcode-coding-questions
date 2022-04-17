class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        low=0
        end=len(nums)-1
        while low<=end:
            mid=(low+end)//2
            if nums[mid]==target:
                return mid
            if nums[low]==target:
                return low
            if nums[end]==target:
                return end
            if low==end:
                if nums[mid]==target:
                    return mid
                return -1
            if nums[mid]>nums[end]:
                if target>nums[mid]:
                    low=mid+1
                elif target>nums[end]:
                    end=mid-1
                else:
                    low=mid+1
            elif nums[mid]<=nums[end]:
                if nums[end]<target:
                    end=mid-1
                elif target>nums[mid]:
                    low=mid+1
                else:
                    end=mid-1                                 


        return -1      