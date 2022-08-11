import heapq
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans=""
        dic=Counter(s)
        size=0
        heap=[]
        for i in dic:
            heapq.heappush(heap,(-ord(i),i))
            size+=1
        while heap:
            if size==1:
                val,a=heapq.heappop(heap)
                ans+=a*min(dic[a],repeatLimit)
                break
            val,a=heapq.heappop(heap)
            val,b=heapq.heappop(heap)
            size-=2
            while dic[a]>0 and dic[b]>0:
                if dic[a]<=repeatLimit:
                    
                    ans+=a*dic[a]
                    dic[a]=0
                    break
                ans+=a*repeatLimit
              
                ans+=b
                dic[a]-=repeatLimit
                dic[b]-=1
            if dic[a]>0:
                heapq.heappush(heap,(-ord(a),a)) 
                size+=1
            if dic[b]>0:
                heapq.heappush(heap,(-ord(b),b))  
                size+=1
        return ans     
        