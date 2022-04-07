class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        counti=0 
        ele=-1
        for i in nums:
            if counti==0:
                ele=i
                counti+=1
            elif i==ele:
                counti+=1
            else:
                counti-=1
        return ele       