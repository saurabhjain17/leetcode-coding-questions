
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
#         i=1
#         n=len(s)
#         if k>n :return s
#         stack=[(s[0],1)]
#         length=1
        
#         while i<n:
#             if length==0:
#                 stack.append((s[i],1))
#                 length+=1
#             else:
#                 if s[i]==stack[-1][0]:
#                     stack.append((s[i],stack[-1][1]+1))
#                 else:
#                     stack.append((s[i],1))
#                 length+=1
#             if stack[-1][1]==k:
#                 t=k
#                 while t:
#                     stack.pop(-1)
#                     length-=1
#                     t-=1
#             i+=1
#         out=""  
        
#         for i in stack:
#             out+=i[0]
#         return out    
            stck = [['$', 0]]     # a placeholder to mark stack is empty. This eliminates the need to do an empty check later
        
            for c in s:
                if stck[-1][0] == c:
                    stck[-1][1]+=1 # update occurences count of top element if it matches current character
                    if stck[-1][1] == k:
                        stck.pop()
                else:
                    stck.append([c, 1])            

            return ''.join(c * cnt for c, cnt in stck)
                    
           