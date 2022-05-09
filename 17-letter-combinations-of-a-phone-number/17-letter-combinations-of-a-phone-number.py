class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        out=[]
        n=len(digits)
        if n==0:
            return out
        def bac(digits,dic,out,ind,n,tem):
            if ind==n:
                out.append(tem)
                return
            for i in dic[digits[ind]]:
                bac(digits,dic,out,ind+1,n,tem+i)
        bac(digits,dic,out,0,n,"")
        return out