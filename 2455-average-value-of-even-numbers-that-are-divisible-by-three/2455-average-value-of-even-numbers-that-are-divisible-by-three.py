import math
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        leng=0
        sumi=0
        for i in nums:
            if i%6==0:
                sumi+=i
                leng+=1
        if leng==0:
            return 0
        return math.floor(sumi/leng)