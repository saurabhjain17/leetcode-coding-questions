import math
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=sum(cardPoints)
        if n==k:
            return total
        k=n-k
        mini=math.inf
        sumi=sum(cardPoints[:k])
        mini=min(mini,sumi)
        for i in range(1,n-k+1):
           
            sumi=sumi+cardPoints[i+k-1]-cardPoints[i-1]
            mini=min(mini,sumi)
        return total-mini    