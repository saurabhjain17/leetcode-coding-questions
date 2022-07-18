import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[nums[0]]
        n=len(nums)
        size=1
        for i in range(1,n):
            p=math.gcd(nums[i],stack[-1])
            if p>1:
                stack[-1]=int((nums[i]*stack[-1])//p)
                while size>1:
                    tem= math.gcd(stack[-2],stack[-1])
                    if tem==1:
                        break
                    prod=stack[-1]*stack[-2]
                    stack.pop(-1)
                    stack[-1]=int(prod//tem)
                    size-=1
            else:
                stack.append(nums[i])
                size+=1
        return stack        
        