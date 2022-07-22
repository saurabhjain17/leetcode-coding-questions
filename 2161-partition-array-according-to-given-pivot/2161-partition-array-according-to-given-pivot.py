class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        ans=[]
        same=0
        for i in nums:
            if i<pivot:
                ans.append(i)
            elif i==pivot:
                same+=1
        for i in range(same):
            ans.append(pivot)
        for i in nums:
            if i>pivot:
                ans.append(i)
        return ans        