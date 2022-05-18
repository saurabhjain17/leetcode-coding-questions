class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        counti=0
        n=len(nums)
        for i in range(n-2):
            k=i+2
            j=i+1
            while j<n and k<n:
                if j>=k:
                    k=j+1
                while   k<n and nums[i]+nums[j]>nums[k]:
                    k+=1
                if k==n:
                    p=k-j-1
                    counti+=(p*(p+1)//2)
                    print(1)
                    
                else:
                    
                    counti+=(k-j-1)
                    # print(k-j-1,k,j)
                    j+=1
        return counti        