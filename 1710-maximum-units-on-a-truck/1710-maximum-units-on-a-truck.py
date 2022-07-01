class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1])
        boxTypes=boxTypes[::-1]
        ans=0
        i=0
        n=len(boxTypes)
        while truckSize>0 and i<n:
            if boxTypes[i][0]<=truckSize:
                truckSize-=boxTypes[i][0]
                ans+=boxTypes[i][0]*boxTypes[i][1]
            else:
                ans+=truckSize*boxTypes[i][1]
                break
            i+=1
        return ans    