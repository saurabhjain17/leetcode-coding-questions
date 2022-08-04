class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        vis=set()
        global longest
        def bfs(nod,vis,dp,dis):
            global longest 
            if nod ==-1:
                return
            if nod in dp:
                longest=max(longest,dis-dp[nod])
                return
            if nod in vis:
                return
            vis.add(nod)
            dp[nod]=dis
            bfs(edges[nod],vis,dp,dis+1)
        longest=-1
        for i in range(len(edges)):
            if i not in vis:
                bfs(i,vis,dict(),0)
        return longest        
#         longest=-1
#         n=len(edges)
#         vis=set()
#         global ans
#         ans=-1
#         def bfs(nod,start,counti,tem,Flag):
#             global ans
#             if nod==start and Flag:
#                 vis.union(tem)
#                 ans=max(ans,counti)
#                 return
#             if nod==-1 :
#                 vis.union(tem)
#                 return
#             if nod in tem:
#                 return
#             tem.add(nod)
#             if nod<len(edges):
#                 bfs(edges[nod],start,counti+1,tem,True)
#         for i in range(n):
#             if edges[i]!=-1 and i not in vis:
#                 bfs(i,i,0,set(),False)
                
#         return ans       
         
          
          
                