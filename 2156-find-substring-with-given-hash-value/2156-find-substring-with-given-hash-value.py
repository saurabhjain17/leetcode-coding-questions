class Solution:
    # def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    #     n=len(s)
    #     dic={chr(i-1+ord("a")):i for i in range(1,27)}
    #     # print(dic)
    #     last=0
    #     ne=1
    #     for i in range(k):
    #         last+=(dic[s[i]]*ne)
    #         ne*=power
    #     last_ans=last%modulo
    #     # print(last,last_ans)
    #     if last_ans==hashValue:
    #         return s[:k]
    #     tem=power**(k-1)
    #     for i in range(1,n-k+1):
    #         last-=dic[s[i-1]]
    #         last//=power
    #         last+=(dic[s[i+k-1]]*tem)
    #         last_ans=last%modulo
    #         if last_ans==hashValue:
    #             return s[i:i+k]
    def subStrHash(self, s, p, m, k, hashValue):
        def val(c):
            return ord(c) - ord('a') + 1
            
        res = n = len(s)
        pk = pow(p,k,m)
        cur = 0

        for i in range(n - 1, -1, -1):
            cur = (cur * p + val(s[i])) % m
            if i + k < n:
                cur = (cur - val(s[i + k]) * pk) % m
            if cur == hashValue:
                res = i
        return s[res: res + k]
            
            