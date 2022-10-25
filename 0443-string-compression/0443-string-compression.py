class Solution:
    def compress(self, chars: List[str]) -> int:
        ans=[chars[0]]
        counti=1
        n=len(chars)
        seti=set([str(i) for i in range(10)])
        for i in range(1,n):
            if chars[i-1]==chars[i]:
                counti+=1
            else: 
                
               
                if counti>1:
                    t=[]
                    while counti>0:
                        t.append(str(counti%10))
                        counti//=10
                    t=t[::-1]
                    ans.extend(t)
                ans.append(chars[i])
                counti=1
               
            
        if counti>1:
                    t=[]
                    while counti>0:
                        t.append(str(counti%10))
                        counti//=10
                    t=t[::-1]
                    ans.extend(t)
        m=len(ans)            
        for i in range(m):
            chars[i]=ans[i]
        return m    
                   