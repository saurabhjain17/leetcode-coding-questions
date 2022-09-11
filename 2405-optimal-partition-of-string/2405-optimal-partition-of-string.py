class Solution:
    def partitionString(self, s: str) -> int:
        counti=0
        vis=set()
        for i in s:
            if i in vis:
                counti+=1
                vis=set()
            vis.add(i)
                
        return counti+1        