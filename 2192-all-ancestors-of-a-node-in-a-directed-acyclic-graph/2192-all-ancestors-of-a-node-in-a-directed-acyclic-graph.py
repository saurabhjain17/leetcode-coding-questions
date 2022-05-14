class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges.sort(key=lambda x:(x[0],x[1]))
        
        op=[set() for i in range(n)]
        deg=[0]*n
        adj=[[] for i in range(n)]
        for i in edges:
            deg[i[1]]+=1
            adj[i[0]].append(i[1])
        q=[]
        for i in range(n):
            if deg[i]==0:
                q.append(i)
        while q:
            nod=q.pop(0)
            for tem in adj[nod]:
                deg[tem]-=1
                if deg[tem]==0:
                    q.append(tem)
                op[tem].add(nod)    
                op[tem]=op[tem].union(op[nod])
                
        for i in range(n):
            
            op[i]=list(op[i])
            op[i].sort()
        return op    