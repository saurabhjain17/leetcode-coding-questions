class Solution:
    def istrue(self,wd,arr,n):
        counti=0
        for i in range(n):
            if wd[i]!=arr[i]:
                counti+=1
        return counti<=2        
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n=len(queries)
        m=len(dictionary)
        p=len(queries[0])
        ans=[]
        for fir in queries:
            for word in dictionary:
                if self.istrue(fir,word,p):
                    ans.append(fir)
                    break
        return ans            