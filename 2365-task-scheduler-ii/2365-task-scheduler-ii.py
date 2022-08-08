class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        dic=dict()
        day=1
        for i in range(len(tasks)):
            if tasks[i] not in dic or dic[tasks[i]]+space<day:
                
                dic[tasks[i]]=day
                day+=1
            else:
                day=dic[tasks[i]]+space+1
                dic[tasks[i]]=day
                day+=1
        print(dic)        
        return day-1          