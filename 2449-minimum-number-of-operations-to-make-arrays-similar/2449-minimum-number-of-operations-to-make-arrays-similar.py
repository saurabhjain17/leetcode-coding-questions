class Solution:
    def makeSimilar(self, nums: List[int], cost: List[int]) -> int:
        
        even_n=[]
        odd_n=[]
        nums.sort()
        for i in nums:
            if i&1==0:
                even_n.append(i)
            else:
                odd_n.append(i)
        odd_c=[]
        even_c=[]
        cost.sort()
        for i in cost:        
            if i&1==0:
                even_c.append(i)
            else:
                odd_c.append(i)
        n=len(even_n)
        m=len(even_c)
        ans=0
        i=j=0
        # print(even_n)
        # print(even_c)
        while i<n and j<m:
            if even_n[i]==even_c[j]:
                i+=1
                j+=1
            elif even_n[i]>even_c[j]: 
                ans+=(even_n[j]-even_c[i])//2
                j+=1
                i+=1
            else:
                ans+=(even_c[j]-even_n[i])//2
                i+=1
                j+=1
        n=len(odd_n)
        m=len(odd_c)
        i=j=0
        while i<n and j<m:
            if odd_n[i]==odd_c[j]:
                i+=1
                j+=1
            elif odd_n[i]>odd_c[j]:  
                ans+=(odd_n[j]-odd_c[i])//2
                j+=1
                i+=1
            else:
                ans+=(odd_c[j]-odd_n[i])//2
                i+=1
                j+=1
        return ans//2        
                