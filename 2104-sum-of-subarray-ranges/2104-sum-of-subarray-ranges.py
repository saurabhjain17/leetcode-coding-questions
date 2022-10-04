class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        st=[]
        left=[1]*n
        st.append(0)
        for i in range(1,n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop(-1)
            left[i]=i+1
            if st:
                left[i]=i-st[-1]
            st.append(i)
        right=[1]*n
        st=[n-1]
        for i in range(n-2,-1,-1):
            while st and nums[st[-1]]>nums[i]:
                st.pop(-1)
            right[i]=n-i
            if st:
                right[i]=st[-1]-i
            st.append(i)  
        res=0
        for i in range(n):
            res-=nums[i]*left[i]*right[i]
        st=[]
        left=[1]*n
        st.append(0)
        for i in range(1,n):
            while st and nums[st[-1]]<=nums[i]:
                st.pop(-1)
            left[i]=i+1
            if st:
                left[i]=i-st[-1]
            st.append(i)
        right=[1]*n
        st=[n-1]
        for i in range(n-2,-1,-1):
            while st and nums[st[-1]]<nums[i]:
                st.pop(-1)
            right[i]=n-i
            if st:
                right[i]=st[-1]-i
            st.append(i)     
        # print(left,right)    
        for i in range(n):
            res+=nums[i]*left[i]*right[i]
        return res        