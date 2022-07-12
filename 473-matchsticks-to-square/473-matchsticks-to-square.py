class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        sumi=sum(matchsticks)
        n=len(matchsticks)
        if (sumi/4)%1!=0:
            return False
        sumi//=4
        dic=dict()
        def rec(n,matchsticks,sumi1,sumi2,sumi3,sumi4,sumi,dic):
            if sumi1>sumi or sumi2>sumi or sumi3>sumi or sumi4>sumi:
                return False
            if n==0:
                if sumi1!=sumi or sumi3!=sumi or sumi2!=sumi or sumi4!=sumi:
                    return False
                return True
                
                
            
            if (n,sumi1,sumi2,sumi3,sumi4) not in dic:
                t=matchsticks[n-1]
                dic[(n,sumi1,sumi2,sumi3,sumi4)]=rec(n-1,matchsticks,sumi1+t,sumi2,sumi3,sumi4,sumi,dic) or rec(n-1,matchsticks,sumi1,sumi2+t,sumi3,sumi4,sumi,dic) or rec(n-1,matchsticks,sumi1,sumi2,sumi3+t,sumi4,sumi,dic) or rec(n-1,matchsticks,sumi1,sumi2,sumi3,sumi4+t,sumi,dic) 
            return  dic[(n,sumi1,sumi2,sumi3,sumi4)]
        return rec(n,matchsticks,0,0,0,0,sumi,dic)