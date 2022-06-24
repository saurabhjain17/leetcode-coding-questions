import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        A = [-a for a in target]
        heapq.heapify(A)
        while True:
            a = -heapq.heappop(A)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)
        # n=len(target)
        # if 0 in target:
        #     return False
        # if n==1:
        #     return target[0]==1
        # if n==2 and (target[0]==1 or target[1]==1):
        #     return True
        # heap=[]
        # for i in target:
        #     heapq.heappush(heap,-i)
        # sumi=sum(target)
        # m=-heapq.heappop(heap)
        # while m!=1:
        #     if sumi<2*m:
        #         ne_sumi=-sum(heap)
        #         if ne_sumi==0:
        #             return m==1
        #         p=m%ne_sumi
        #         if p==0:
        #             return False
        #         sumi=sumi-m+p
        #         heapq.heappush(heap,-p)
        #         m=-heapq.heappop(heap)
        #     else:
        #         return False
        # return True    