class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[0]*numCourses
        deg=[0]*numCourses
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
            if adj[nod]!=0:
                for tem in adj[nod]:
                    deg[tem]-=1
                    if deg[tem]==0:
                        q.append(tem)
                        counti+=1
        print(counti)                
        return counti==numCourses                