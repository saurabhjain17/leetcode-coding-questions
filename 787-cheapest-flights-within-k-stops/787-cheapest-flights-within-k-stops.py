import math
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic=dict()
        adj=[[] for i in range(n)]
        for u,v,c in flights:
            adj[u].append([v,c])
        def rec(src,dest,stop):
            if src==dest:
                    return 0
            if  stop>=k+1:
                return math.inf
            if (src,stop) not in dic:
                t=math.inf
                for v,c in adj[src]:
                    t=min(t,c+rec(v,dest,stop+1))
                dic[(src,stop)]=t
            return dic[(src,stop)]
        ans=rec(src,dst,0)
        if ans==math.inf:
            return -1
        return ans