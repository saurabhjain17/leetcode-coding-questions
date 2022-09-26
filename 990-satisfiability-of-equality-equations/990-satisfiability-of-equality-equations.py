
   
class Solution:
    def parent(self,x,par):
        if par[x]==x:
            return x
        par[x]=self.parent(par[x],par)
        return par[x]
    def union(self,a,b,par,rank):
        x=self.parent(a,par)
        y=self.parent(b,par)
        if x==y:
            return
        else:
            if rank[x]<rank[y]:
                par[x]=y
            elif rank[x]>rank[y]:
                par[y]=x
            else:
                par[x]=y
                rank[y]+=1
            return    
    def equationsPossible(self, equations: List[str]) -> bool:
        rank=[0]*26
        par=[i for i in range(26)]
        val=ord("a")
        for eq in equations:
            if eq[1]=="=":
                self.union(ord(eq[0])-val,ord(eq[3])-val,par,rank)
        for eq in equations:
            if eq[1]=="!":
                if self.parent(ord(eq[0])-val,par)==self.parent(ord(eq[3])-val,par):
                    return False
        return True        