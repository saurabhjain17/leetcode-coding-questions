import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        n=len(stations)
        heap=[]
        counti=0
        las=0
        i=0
        des=0
        if n==0:
            if startFuel>=target:
                return 0
            return -1   
        while i<n and des<target:
            if target>=stations[i][0]:
                if startFuel>=stations[i][0]-las:
                    startFuel-=(stations[i][0]-las)
                    heapq.heappush(heap,-stations[i][1])
                    des=stations[i][0]
                    las=stations[i][0]
                    i+=1
                    continue
                else:
                    startFuel-=(stations[i][0]-las)
                    while heap and startFuel<0:
                        counti+=1
                        startFuel-=heapq.heappop(heap)
                    heapq.heappush(heap,-stations[i][1]) 
                    des=stations[i][0]
                    las=stations[i][0]
                    i+=1
                    if startFuel<0:
                        return -1
            else:
                if startFuel>=target-las:
                    startFuel-=(target-las)
                    
                    des=target
                    las=target
                    break
                else:
                    startFuel-=(target-las)
                    while heap and startFuel<0:
                        counti+=1
                        startFuel-=heapq.heappop(heap)
                    
                    des=target
                    las=target
                    
                    if startFuel<0:
                        return -1
                    break
        if target >stations[-1][0]:
            to_reach=target-stations[-1][0]
            sumi=-sum(heap)+startFuel
            if sumi<to_reach:
                return -1
            to_reach-=startFuel
            startFuel=0
            while to_reach>0:
                to_reach+=heapq.heappop(heap)
                counti+=1
        return counti        
                
                    