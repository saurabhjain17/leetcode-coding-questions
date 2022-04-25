class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cab=len(connections)
        if n>cab+1:
            return -1
        vis=[0]*n
        adj=[set() for i in range(n)]
        for i,j in connections:
            adj[i].add(j)
            adj[j].add(i)
        counti=0    
        def dfs(ind,vis,adj):
            vis[ind]=1
            for nu in adj[ind]:
                if vis[nu]==0:
                    dfs(nu,vis,adj)
        for i in range(n):
            if vis[i]==0:
                counti+=1
                dfs(i,vis,adj)
        return counti -1       