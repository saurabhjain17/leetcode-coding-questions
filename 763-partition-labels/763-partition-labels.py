class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        op=[]
        start=0
        end=len(s)
        dic=dict()
        for i in range(end-1,-1,-1):
            if s[i] not in dic:
                dic[s[i]]=i
        while start<end:
            i=start
            right=i
            while i<end and i<=right:
                right=max(right,dic[s[i]])
                i+=1
            op.append(i-start)
            start=i
        return op    