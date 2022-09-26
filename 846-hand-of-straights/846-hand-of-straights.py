import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic=Counter(hand)
        heap=list(dic.keys())
        heapq.heapify(heap)
        while heap:
            tem=[]
            i=0
            las=None
            while heap and i<groupSize:
                if las==None or las+1==heap[0]:
                    
                    las=heapq.heappop(heap)
                    dic[las]-=1
                    tem.append(las)
                    i+=1
                else:
                    return False
            if i<groupSize:
                 return False
            for i in tem:
                if dic[i]>0:
                    heapq.heappush(heap,i)
        return True            