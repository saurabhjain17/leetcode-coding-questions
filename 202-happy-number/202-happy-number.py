class Solution:
    def isHappy(self, n: int) -> bool:
        seti=set()
        
        while n!=1:
            seti.add(n)
            ne=0
            while n>0:
                tem=n%10
                ne+=tem*tem
                n//=10
            if ne in seti:
                return False
            seti.add(ne)
            n=ne
        return True    
                