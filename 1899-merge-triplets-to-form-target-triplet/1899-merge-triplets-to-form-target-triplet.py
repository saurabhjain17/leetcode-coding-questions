class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a=b=c=0
        for i,j,k in triplets:
            if i<=target[0] and j<=target[1] and k<=target[2]:
                if i==target[0]:
                    a=1
                if j==target[1]:
                    b=1
                if k==target[2]:
                    c=1
        return a and b and c            