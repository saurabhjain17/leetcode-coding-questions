class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n=len(players)
        m=len(trainers)
        i=0
        j=0
        counti=0
        while i<n and j<m:
            if players[i]<=trainers[j]:
                counti+=1
                i+=1
            j+=1
        return counti    