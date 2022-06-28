class Solution:
    def minDeletions(self, s: str) -> int:
        dic=dict()
        for i in s:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        les=[]
        for i in dic:
            les.append(dic[i])
        les.sort()
        les=les[::-1]
        last=les[0]-1
        n=len(les)
        counti=0
        # print(les)
        for i in range(1,n):
            if les[i]==last:
                last=max(last-1,0)
                continue
            elif les[i]<last:
                last=les[i]-1
                continue
            else:
                counti+=les[i]-last
                last=max(last-1,0)
        return counti        