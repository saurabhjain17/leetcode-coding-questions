class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic=dict()
        x="abcdefghijklmnopqrstuvwxyz"
        i=0
        for j in key:
            if j not in dic and j!=" ":
                dic[j]=x[i]
                i+=1
        ans=""
        for i in message:
            if i==" ":
                ans+=i
            else:
                ans+=dic[i]
        return ans        