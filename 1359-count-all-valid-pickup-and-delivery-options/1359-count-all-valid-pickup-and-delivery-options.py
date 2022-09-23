class Solution:
    def countOrders(self, n: int) -> int:
        modu=10**9+7
        def fact(n):
            ans=1
            for i in range(2,n+1):
                ans*=i
                ans%=modu
            return ans    
        def rec(p,d,n):
            if p==n and d==n:
                return 1
            if p>n or d>n:
                return 0
            if (p,d) not in dp:
                ans=0
                if p>d:
                    ans=rec(p+1,d,n)
                    ans+=(p-d)*rec(p,d+1,n)
                elif p==d:
                    ans=rec(p+1,d,n)%modu
                dp[(p,d)]=ans%modu
            return dp[(p,d)]
        dp=dict()
        op=rec(0,0,n)
        po=fact(n)*2
        return ((op)*fact(n))%modu