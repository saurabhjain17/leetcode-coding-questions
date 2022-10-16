class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num+1):
            
            k=str(i)
            k=int(k[::-1])
            if i+k==num:
                
                return True
        return False   