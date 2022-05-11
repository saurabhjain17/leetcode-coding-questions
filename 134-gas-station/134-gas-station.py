class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total=0
        sumi=0
        start=0
        for i in range(n):
            
            sumi+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if sumi<0:
                
                start=i+1
                sumi=0
        if total>=0:
            return start
        return -1