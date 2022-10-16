class Solution:
    def countTime(self, time: str) -> int:
         
        ans=1
        if time[4]=="?":
            ans*=10
            flag=1
        if time[3]=="?":
            ans*=6
            flag=1
        if time[0]=="?" and time[1]=="?":
            ans*=24
        elif time[1]=="?":
            if time[0]=="0" or time[0]=="1":
                ans*=10
            else:
                ans*=4
        elif time[0]=="?":
            if time[1] in ["0","1","2","3"]:
                ans*=3
            else:
                ans*=2
        return ans        
            
            