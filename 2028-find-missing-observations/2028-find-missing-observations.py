class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        sumi=(n+m)*mean-sum(rolls)
        print(sumi)
        lis=[1]*n
        sumi-=n
        if sumi<0:
            return []
        p=5*n
        
        for i in range(n):
            if sumi<=5:
                lis[i]+=sumi
                sumi=0
                break
            else:
                lis[i]+=5
                sumi-=5
        if sumi>0:
            return []
        return lis
        