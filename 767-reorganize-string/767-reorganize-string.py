import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans=""
        dic=Counter(s)
        n=len(dic)
        heap=[]
        for i in dic:
            heapq.heappush(heap,(-dic[i],i))
        while n>1:
            key1,val1=heapq.heappop(heap)
            key2,val2=heapq.heappop(heap)
            n-=2
            ans+=val1+val2
            key1+=1
            key2+=1
            if key1!=0:
                heapq.heappush(heap,(key1,val1))
                n+=1
            if key2!=0:
                heapq.heappush(heap,(key2,val2))   
                n+=1
        if n==0:
            return ans
        if n==1:
            key,val=heapq.heappop(heap)
            if key<-1:
                return ""
            else:
                return ans+val*(-key)
                