class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        new_list=sorted(costs,key=lambda l:(l[0]-l[1]))
        price=0
        for i in range(len(costs)//2):
            price+=new_list[i][0]
        for i in range(len(costs)//2,len(costs)):
            price+=new_list[i][1]
        return price    
        