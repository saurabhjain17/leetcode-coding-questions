class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seti=set(nums)
        for i in nums:
            val=0
            k=i
            while k>0:
                val*=10
                val+=k%10
                k//=10
            seti.add(val)
        return len(seti)    