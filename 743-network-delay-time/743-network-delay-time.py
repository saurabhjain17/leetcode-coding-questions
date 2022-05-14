import heapq
import math
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[-1]*(n+1)
        for i in times:
            if adj[i[0]]==-1:
                adj[i[0]]=[-1]*(n+1)
            adj[i[0]][i[1]]=i[2]   
        heap=[]
        dis=[math.inf]*(n+1)
        dis[k]=0
        heapq.heappush(heap,(0,k))
        # return adj
        while heap:
            dist,nod=heapq.heappop(heap)
            if adj[nod]!=-1:
                for ne_nod in range(1,n+1):
                    if adj[nod][ne_nod]!=-1:
                        if dis[ne_nod]>dist+adj[nod][ne_nod]:
                            dis[ne_nod]=dist+adj[nod][ne_nod]
                            heapq.heappush(heap,(dis[ne_nod],ne_nod))
        p= max(dis[1:]) 
        if p==math.inf:
            return -1
        return p