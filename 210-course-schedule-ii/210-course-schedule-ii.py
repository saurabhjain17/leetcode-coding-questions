class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[0]*numCourses
        deg=[0]*numCourses
        op=[]
        for course in prerequisites:
            if adj[course[1]]==0:
                adj[course[1]]=[]
            adj[course[1]].append(course[0])
            deg[course[0]]+=1
        q=[]
        counti=0
        for i in range(numCourses):
            if deg[i]==0:
                q.append(i)
                counti+=1
        while q:
            nod=q.pop(0)
            op.append(nod)
            if adj[nod]!=0:
                for tem in adj[nod]:
                    deg[tem]-=1
                    if deg[tem]==0:
                        q.append(tem)
                        counti+=1
                        
        if  counti!=numCourses:
            return []
        return op