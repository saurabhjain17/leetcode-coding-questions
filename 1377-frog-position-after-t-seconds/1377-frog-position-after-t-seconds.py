class Solution:
    def fin_path(self,adj,cur,vis,path,time,target):
        if time==0:
            if cur==target:
                return True
            else:
                return False
        length=len(adj[cur])    
        if cur==target:
            if length<=1:
                return True
            return False
        
        path.append(cur)
        vis[cur]=1
        for i in adj[cur]:
            if vis[i]==0:
                if self.fin_path(adj,i,vis,path,time-1,target)==True:
                    return True
        path.pop(-1)
        vis[cur]=0
        return False
                
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        path=[]
        vis=[0]*(n+1)
        adj=[[] for i in range(n+1)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        if len(adj[1])==0 and target==1:
            return 1.00000    
        self.fin_path(adj,1,vis,path,t,target)
        if len(path)==0:
            return 0.00000
        # if len(adj[1])==0 and target==1:
        #     return 1.00000
        ans=len(adj[path[0]])
        for i in range(1,len(path)):
            ans*=len(adj[path[i]])-1
        # print(ans) 
        # print(path)
        return 1/ans    
        