import heapq
from collections import Counter
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        heap=[]
        n=len(nums1)
        num=[abs(nums1[i]-nums2[i]) for i in range(n)]
        dic=Counter(num)
        size=0
        k=k1+k2
        for i in dic:
            if i!=0:
                heapq.heappush(heap,(-i,dic[i]))
                size+=1
        print(heap)    
        while size>1 and k>0:    
            val1,ct=heapq.heappop(heap)
            val2,dt=heapq.heappop(heap)
            if val1==0:
                return 0
            val1=-val1
            val2=-val2
            size-=2
            if (val1-val2)*ct<=k:
                
                k-=(val1-val2)*ct
                val1=val2
                heapq.heappush(heap,(-val1,ct+dt))
                size+=1
            else:
                heapq.heappush(heap,(-val2,dt))
                size+=1
                # print(heap)
                while k>=ct:
                    k-=ct
                    val1-=1
                ne=ct-k    
                heapq.heappush(heap,(-val1,ne))
                size+=1
                heapq.heappush(heap,(-(val1-1),k))
                size+=1
                k=0
                 
        if k>0 and size>0:
            print(heap,k)
            val1,ct=heapq.heappop(heap) 
            if val1==0:
                return 0
            
            size-=1
            val1=-val1
            if val1*ct<=k:
                return 0
            else:
                while k>=ct:
                    k-=ct
                    val1-=1
                ne=ct-k 
                heapq.heappush(heap,(-val1,ne))
                size+=1
                heapq.heappush(heap,(-(val1-1),k))
                size+=1
                k=0
        ans=0
        # print(heap)
        for i,j in heap:
            ans+=((-i)**2)*j
        return ans    