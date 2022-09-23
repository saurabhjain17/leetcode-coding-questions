class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        q=len(queries)
        upper=set([chr(i+ord("A")) for i in range(26)])
        pt=len(pattern)
        ans=[True]*q
        for i in range(q):
            query=queries[i]
            qr=len(query)
            j=k=0
            while j<qr and k<pt:
                if query[j]==pattern[k]:
                    j+=1
                    k+=1
                elif query[j] in upper and query[j]!=pattern[k]:
                    ans[i]=False
                    break
                else:
                    j+=1
            if k<pt:
                ans[i]=False
            while j<qr:
                if query[j] in upper:
                    ans[i]=False
                    break
                j+=1    
        return ans           