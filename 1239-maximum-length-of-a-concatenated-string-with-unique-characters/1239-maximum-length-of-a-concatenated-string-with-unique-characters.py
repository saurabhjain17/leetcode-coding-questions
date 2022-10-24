class Solution:
    def maxLength(self, arr: List[str]) -> int:
        lis=[]
        for i in arr:
            vis=set()
            flag=0
            for j in i:
                if j in vis:
                    flag=1
                    break
                vis.add(j)
            if flag==0:
                lis.append(i)
        def rec(seti,n):
            if n==-1:
                ans[0]=max(ans[0],len(seti))
                return 
            flag=0
            for i in arr[n]:
                if i in seti:
                    flag=1
                    break

            rec(seti,n-1)
            if flag==0:
                for i in arr[n]:
                    seti.add(i)
                rec(seti,n-1)
                for i in arr[n]:
                    seti.discard(i)
        arr=lis            
        ans=[0]
        rec(set(),len(arr)-1)
        return ans[0] 