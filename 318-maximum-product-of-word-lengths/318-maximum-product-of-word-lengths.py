class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxi=0
        n=len(words)
        for i in range(n-1):
            seti=set()
            length1=0
            for j in words[i]:
                length1+=1
                seti.add(j)
            for j in range(i+1,n)  :
                length2=0
                flag=0
                for k in words[j]:
                    length2+=1
                    if k in seti:
                        flag=1
                        break
                if flag==0:
                    maxi=max(maxi,length1*length2)
        return maxi              