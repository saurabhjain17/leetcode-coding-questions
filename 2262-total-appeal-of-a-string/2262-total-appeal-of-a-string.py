class Solution:
    def appealSum(self, s: str) -> int:
        n=len(s)
        dic=dict()
        counti=0
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]]=[]
            dic[s[i]].append(i)   
        for ch in dic:
            dic[ch].append(n)
            p=len(dic[ch])
            for j in range(p-1):
                counti+=(dic[ch][j]+1)*(dic[ch][j+1]-dic[ch][j])
        return counti        