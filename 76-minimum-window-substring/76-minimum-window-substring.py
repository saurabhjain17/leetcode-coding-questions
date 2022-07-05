from collections import Counter
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        start=end=-1
        n=len(t)
        dic2=Counter(t)
        counti=len(dic2)
        dic1=dict()
        j=0
        i=0
        mini=math.inf
        while (j<m and i<m ) or counti==0:
            if counti!=0:
                if s[j] not in dic1:
                    dic1[s[j]]=0
                if s[j] in dic2:    
                    if dic1[s[j]]==dic2[s[j]]-1:
                        counti-=1
                dic1[s[j]]+=1
                j+=1
            else:
                if mini>(j-i):
                    mini=j-i
                    start=i
                    end=j
                if s[i] in dic2 and dic1[s[i]]==dic2[s[i]]:
                    counti+=1
                dic1[s[i]]-=1
                i+=1
        if mini==math.inf:
            return ""
        return s[start:end]
                    
        