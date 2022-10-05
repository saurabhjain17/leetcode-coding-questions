class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        modu=10**9+7
        left=[1]*n
        right=[1]*n
        st=[0]
        for i in range(1,n):
            while st and arr[st[-1]]>=arr[i]:
                st.pop(-1)
            left[i]=i+1
            if st:
                left[i]=i-st[-1]
            st.append(i)
        st=[n-1]    
        for i in range(n-2,-1,-1):
            while st and arr[st[-1]]>arr[i]:
                st.pop(-1)
            right[i]=n-i
            if st:
                right[i]=st[-1]-i
            st.append(i)
        ans=0
        for i in range(n):
            ans+=left[i]*right[i]*arr[i]
            ans%=modu
        # print(left,right)    
        return ans     