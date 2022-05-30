class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        p=1
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        if dividend<0 and divisor<0:
            dividend*=-1
            divisor*=-1
            
        elif dividend<0 or divisor<0:
            p=-1
            if dividend<0:
                dividend*=-1
            elif divisor<0:
                divisor*=-1
        if dividend<divisor:
            return 0
        counti=0
        
        
        while divisor<=dividend:
            ct=1
            ot=divisor
            if divisor==dividend:
                counti+=1
                break
            while ot+ot<=dividend:
                ot+=ot
                ct+=ct
            dividend-=  ot
            counti+=ct
        return counti*p    