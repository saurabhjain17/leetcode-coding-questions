class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[pushed[0]]
        n=len(pushed)
        i=1
        j=0
        counti=1
        while i<n:
            while i<n and (counti==0 or popped[j]!=stack[-1]):
                stack.append(pushed[i])
                i+=1
                counti+=1
            while j<n and counti>0 and  stack[-1]==popped[j]:
                stack.pop(-1)
                counti-=1
                j+=1
        while j<n and stack[-1]==popped[j]:
                stack.pop(-1)
                j+=1
        if j<n:
            return False
        return True