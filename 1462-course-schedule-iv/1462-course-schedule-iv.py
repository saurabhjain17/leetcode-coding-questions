class Solution:
    def checkIfPrerequisite(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
       
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
                
        ans=[]
        for query in queries:
            if query[0] in op[query[1]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans        