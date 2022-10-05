class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        seti=set([str(i) for i in range(10)])
        digi=[]
        ltr=[]
        for log in logs:
            if log[-1] in seti:
                digi.append(log)
            else:
                ltr.append(log)
        n=len(ltr)
        for i in range(n):
            ltr[i]=list(ltr[i].split())
        dic=dict()
        for log in ltr:
            p=tuple(log[1:])
            if p not in dic:
                dic[p]=[]
            dic[p].append(log[0])
        for log in dic:
            dic[log].sort()
        ans=[]    
        for log in sorted(dic.keys()):
            for i in dic[log]:
                ans.append(" ".join([i]+list(log)))
                
        return ans+digi        