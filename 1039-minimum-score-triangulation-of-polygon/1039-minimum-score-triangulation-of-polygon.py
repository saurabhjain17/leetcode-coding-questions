class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        ans=dict()
        def rec(start,end):
            if start+1>=end:
                return 0
            if (start,end) not in ans:
                op=1e10
                for i in range(start+1,end):
                      op=min(op,rec(start,i)+rec(i,end)+values[start]*values[i]*values[end])
                      # print(op)  
                ans[(start,end)] =op
            return ans[(start,end)]
        return rec(0,len(values)-1)