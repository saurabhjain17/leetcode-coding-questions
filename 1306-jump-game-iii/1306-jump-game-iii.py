class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        dp=[-1]*n
        vis=set()
        if 0 not in arr:
            return False
        if arr[start]==0:
            return True
        vis.add(start)
        def rec(arr,dp,ind,n,vis):
            
            if arr[ind]==0:
                return True
            if dp[ind]==-1:
                
                left=right=False
                if ind-arr[ind]>-1:
                    if dp[ind-arr[ind]]!=-1:
                        return dp[ind-arr[ind]]
                    elif (ind-arr[ind]) in vis:
                        left=False
                        
                    else:
                        vis.add(ind-arr[ind])
                        left=rec(arr,dp,ind-arr[ind],n,vis)
                if ind+arr[ind]<n:
                    if dp[ind+arr[ind]]!=-1:
                        return dp[ind+arr[ind]]
                    elif (ind+arr[ind]) in vis:
                        right=False
                        
                    else:
                        vis.add(ind+arr[ind])  
                        right=rec(arr,dp,ind+arr[ind],n,vis) 
                dp[ind]=left or right
            return dp[ind]
        return rec(arr,dp,start,n,vis)