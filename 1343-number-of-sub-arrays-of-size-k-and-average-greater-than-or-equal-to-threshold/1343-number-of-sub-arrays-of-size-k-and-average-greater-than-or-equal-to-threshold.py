class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        n=len(arr)
        test=k*threshold    
        p=0
        for i in range(k):
            p+=arr[i]
        count=0
        if p>=test:
            count+=1
        for i in range(k,n):
            
            p=p-arr[i-k]+arr[i]
            if p>=test:
                count+=1
        return count        