class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1],x[0]))
        heap=[]
        time=0
        counti=0
        n=len(courses)
        for i in range(n):
            heapq.heappush(heap,-courses[i][0])
            counti+=1
            time+=courses[i][0]
            if time>courses[i][1]:
                m=-heapq.heappop(heap)
               
                time-=m
                counti-=1
        return counti       