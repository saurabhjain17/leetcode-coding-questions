from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj=dict()
        val_nod=dict()
        indegree=dict()
        for i in supplies:
            adj[i]=set()
            indegree[i]=0
        n=len(recipes)
        for i in range(n):
            if recipes[i] not in indegree:
                indegree[recipes[i]]=0
            if   recipes[i] not in adj:
                adj[recipes[i]]=set()
            for j in ingredients[i]:
                if j not in adj:
                    adj[j]=set()
                adj[j].add(recipes[i])
                indegree[recipes[i]]+=1
        q=deque() 
        # print(adj)
        # print(indegree)
        seti=set(recipes)
        for i in indegree:
            if indegree[i]==0:
                q.append(i)
        ans=set()
        while q:
            nod=q.popleft()
            if nod in seti:
                ans.add(nod)
            for u in adj[nod]:
                indegree[u]-=1
                if indegree[u]==0:
                    q.append(u)
        return list(ans)           
        
        