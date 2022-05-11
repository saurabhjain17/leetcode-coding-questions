class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        ga=sum(gas)
        cos=sum(cost)
        if cos>ga:
            return -1
        sumi=0
        start=0
        for i in range(n):
            sumi+=gas[i]-cost[i]
            if sumi<0:
                start=i+1
                sumi=0
        return start        