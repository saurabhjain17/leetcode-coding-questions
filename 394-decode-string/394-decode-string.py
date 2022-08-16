class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        seti=set([str(i) for i in range(10)])
        for i in s:
            if i!="]":
                stack.append(i)
            else:
                out=""
                k=stack.pop(-1)
                while k!="[":
                    out=k+out
                    k=stack.pop(-1)
                digit="" 
                while stack and stack[-1] in seti:
                    digit=stack[-1]+digit
                    stack.pop(-1)
                if digit=="":
                    digit="1"
                ans=out*int(digit)
                stack.append(ans)
                # print(stack)   
        return "".join(stack)       