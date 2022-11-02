class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi=0
        
        ct=0
        i=0
        j=0
        n=len(s)
        dic={chr(i+ord("A")):0 for i in range(26)}
        # print(dic)
        while j<n:
            dic[s[j]]+=1
            if ct<dic[s[j]]:
                ct=dic[s[j]]
            while (j-i+1)-ct>k:
                dic[s[i]]-=1
                i+=1
                ct=0
                for c in dic:
                    ct=max(ct,dic[c])
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi    