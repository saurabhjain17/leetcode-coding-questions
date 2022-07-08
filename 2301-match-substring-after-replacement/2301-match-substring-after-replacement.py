class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        dic=dict()
        for u,v in mappings:
            if u not in dic:
                dic[u]=set()
            dic[u].add(v)
        n=len(s)
        m=len(sub)
        for i in range(n-m+1):
            flag=0
            for j in range(m):
                if not((s[i+j]==sub[j]) or (sub[j]  in dic and s[i+j] in dic[sub[j]])):
                    flag=1
                    # print(i+j,j)
                    break
                    
            if flag==0:
                return True
        return False    