import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N=len(nums)
        n=N//3
        leftheap=[]
        rightheap=[]
        left=[]
        right=[]
        for i in range(n):
            heapq.heappush(leftheap,-nums[i])
        sumi=-sum(leftheap)    
        left.append(sumi)    
        for i in range(n,2*n):
            sumi+=nums[i]
            heapq.heappush(leftheap,-nums[i])
            sumi+=heapq.heappop(leftheap)
            left.append(sumi)
            
        for i in range(N-1,2*n-1,-1):
            heapq.heappush(rightheap,nums[i])
        sumi=sum(rightheap)    
        right.append(sumi)    
        for i in range(2*n-1,n-1,-1):
            sumi+=nums[i]
            heapq.heappush(rightheap,nums[i])
            sumi-=heapq.heappop(rightheap)
            right.append(sumi)
        right=right[::-1]    
        mini=1e10
        for i in range(len(left)):
            mini=min(mini,left[i]-right[i])
        return mini    