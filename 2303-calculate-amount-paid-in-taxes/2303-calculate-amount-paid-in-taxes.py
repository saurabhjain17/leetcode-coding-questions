class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total=0
        if income==0:
            return 0.00000
        i=0
        n=len(brackets)
        while i<n and income>0:
            if i==0:
                if brackets[i][0]<=income:
                    total+=(brackets[i][0]*(brackets[i][1]/100))
                    income-=brackets[i][0]
                    
                else:
                    total+=(income*(brackets[i][1]/100))
                    income=0
                    break
                    
            elif brackets[i][0]-brackets[i-1][0]<=income:
                m=brackets[i][0]-brackets[i-1][0]
                total+=(m*(brackets[i][1]/100))
                income-=m
               
            else:
                total+=(income*(brackets[i][1]/100))
                income=0
                break
            i+=1    
        return total+0.00000        
        