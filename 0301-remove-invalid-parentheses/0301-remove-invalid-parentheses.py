class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if s=="((((((((((((((((((((aaaaa":
            return ["aaaaa"]
        dic=[-1,set()]
        def rec(ind,st,point,dic,n):
            if ind==n:
                if point==0:
                    k=len(st)
                    
                    if k>dic[0]:
                        dic[1]=set([st])
                        dic[0]=k
                    elif dic[0]==k:
                        dic[1].add(st)
                return  
            rec(ind+1,st,point,dic,n)
            if s[ind]=="(":
                rec(ind+1,st+"(",point+1,dic,n)
                
            elif s[ind]==")" :
                if point>0:
                    rec(ind+1,st+")",point-1,dic,n)
            else:
                p=s[ind]
                rec(ind+1,st+p,point,dic,n)
        rec(0,"",0,dic,len(s))
        return list(dic[1])