class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seti=dict()
        counti=0
        for i in nums:
            if (k-i) in seti and seti[k-i]>0:
                counti+=1
                seti[k-i]-=1
            else:
                try:
                    seti[i]+=1
                except:
                    seti[i]=1
        return counti        