class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seti=dict()
        counti=0
        for i in nums:
            if (k-i) in seti and seti[k-i]>0:
                counti+=1
                seti[k-i]-=1
            else:
                if i not in seti:
                    seti[i]=1
                else:
                    seti[i]+=1
        return counti        