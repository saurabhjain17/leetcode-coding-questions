class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix=nums.copy()
        modu=10**9+7
        n=len(nums)
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
        left=[-1]*n
        right=[n]*n
        st=[0]
        for i in range(1,n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop(-1)
            if st:
                left[i]=st[-1]
            st.append(i)    
        st=[n-1]        
        for i in range(n-2,-1,-1):
            while st and nums[st[-1]]>nums[i]:
                st.pop(-1)
            if st:
                right[i]=st[-1]
            st.append(i)
        maxi=0
        for i in range(n):
            lefti=0
            if left[i]>-1:
                lefti=prefix[left[i]]
            righti=prefix[right[i]-1]
            maxi=max(maxi,nums[i]*(righti-lefti))
            # maxi%=modu
        return maxi %modu
        