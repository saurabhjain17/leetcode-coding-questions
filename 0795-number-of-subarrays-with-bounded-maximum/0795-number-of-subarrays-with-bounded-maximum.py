class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        st=[0]
        n=len(nums)
        lefti=[-1]*n
        if nums[0]<left or nums[0]>right:
            lefti[0]=0
            
        for i in range(1,n):
            if nums[i]>right or nums[i]<left:
                st.append(i)
                lefti[i]=i
                continue
            while st and nums[st[-1]]<=nums[i]  :
                st.pop(-1)
            if st:
                lefti[i]=st[-1]
            st.append(i)
        st=[n-1]
        righti=[n]*n
        if nums[-1]<left or nums[-1]>right:
            lefti[-1]=n-1
        for i in range(n-2,-1,-1):
            if nums[i]>right or nums[i]<left:
                st.append(i)
                righti[i]=i
                continue
            while st and nums[st[-1]]<nums[i] :
                st.pop(-1)
            if st:
                righti[i]=st[-1]
            st.append(i)
        ans=0
        # print(lefti)
        # print(righti)
        for i in range(n):
            ans+=(i-lefti[i])*(righti[i]-i)
        return ans    