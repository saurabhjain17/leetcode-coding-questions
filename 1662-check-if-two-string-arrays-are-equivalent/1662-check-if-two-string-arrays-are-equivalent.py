class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n1=len(word1)
        n2=len(word2)
        m1=len(word1[0])
        m2=len(word2[0])
        k1=k2=i=j=0
        while i<n1 and j<n2:
            if k1==m1:
                k1=0
                i+=1
                if i<n1:
                  
                   m1=len(word1[i])
            if k2==m2:
                k2=0
                j+=1
                if j<n2:
                   m2=len(word2[j])
            if i==n1 or j==n2:
                break
            if word1[i][k1]!=word2[j][k2]:
                return False
            k1+=1
            k2+=1
        if i<n1 or j<n2:
            return False
        return True    
                