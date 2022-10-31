class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n=len(formula)
        stack=[collections.Counter()]
        i=0
        while i<n:
            if formula[i]=="(":
                stack.append(collections.Counter())
                i+=1
               
            elif formula[i]==")":
                # print(stack,i)
                top=stack.pop(-1)
                i+=1
                strt=i
                while i<n and formula[i].isdigit():
                    i+=1
                mult=int(formula[strt:i] or 1)

                for name,val in top.items():
                    # print(name,val)
                    
                    stack[-1][name]+=val*mult
            else:
                
                strt=i
                i+=1
                while i<n and formula[i].islower():
                    i+=1
                name=formula[strt:i]
                strt=i
                
                while i<n and formula[i].isdigit():
                    i+=1
                
                mult=int(formula[strt:i] or 1)
                
                stack[-1][name]+=mult
                
        return "".join(name+ (str(stack[-1][name]) if stack[-1][name]>1 else "") for name in sorted(stack[-1]))       
                    