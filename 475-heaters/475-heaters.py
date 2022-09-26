class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        m=len(houses)
        n=len(heaters)
        j=0
        maxi=0
        for house in houses:
            las=1e20
            while j<n and las>=abs(heaters[j]-house):
                las=abs(heaters[j]-house)
                j+=1
            j-=1
            maxi=max(las,maxi)
            # print(maxi,j,house)
        return maxi    