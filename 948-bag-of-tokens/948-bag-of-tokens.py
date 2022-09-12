class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i=0
        tokens.sort()
        j=len(tokens)-1
        counti=0
        maxi=0
        while i<=j:
            if tokens[i]<=power:
                power-=tokens[i]
                i+=1
                counti+=1
                maxi=max(counti,maxi)
            elif counti>0:
                counti-=1
                power+=tokens[j]
                j-=1
            else:
                break
        return maxi        