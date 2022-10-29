class Solution:
    def oddString(self, words: List[str]) -> str:
        n=len(words)
        m=len(words[0])
        lis=[]
        for i in range(1,m):
            lis.append(ord(words[0][i])-ord(words[0][i-1]))
        pis=[]    
        for i in range(1,m):
            pis.append(ord(words[1][i])-ord(words[1][i-1]))
        if lis==pis:
            
            for j in range(2,n):
                tem=[]
                for i in range(1,m):
                    tem.append(ord(words[j][i])-ord(words[j][i-1]))
                if tem!=lis:
                    return words[j]
        else:
            tem=[]    
            for i in range(1,m):
                tem.append(ord(words[2][i])-ord(words[2][i-1]))
            if tem==lis:
                return words[1]
            else:
                return words[0]