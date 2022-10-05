class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        out=[]
        s="123456789"
        mini=len(str(low))
        maxi=len(str(high))
        for i in range(mini,maxi+1):
            for j in range(0,9-i+1):
                k=int(s[j:j+i])
                if k>=low and k<=high:
                    out.append(k)
        return out            