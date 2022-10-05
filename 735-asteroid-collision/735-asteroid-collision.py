class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        st=[a[0]]
        n=len(a)
        for i in range(1,n):
            if a[i]<0:
                while st and st[-1]>0 and st[-1]<-a[i]:
                    st.pop(-1)
                if not st or st[-1]<0:
                    st.append(a[i])
                elif st[-1]==-a[i]:
                    st.pop(-1)
                    
                    
                # print(st)    
            else:
                st.append(a[i])
        return st        
        