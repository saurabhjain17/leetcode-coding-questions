class Solution:
    def nearestPalindromic(self, nums: str) -> str:
        
        num=int(nums)
        if num<11:
            return str(num-1)
        d = []
        n = 0
        tn = num
        while tn:
            d.append(str(tn%10))
            tn = tn//10
            n+=1
        d = d[::-1]
        st = "".join(d)
        candidats = []
        candidats.append("9"*(n-1))
        candidats.append("1"+"0"*(n-1)+"1")
        prefix = int(st[:(n+1)//2])
        for pre in [prefix-1, prefix, prefix+1]:
            spre = str(pre)
            if n%2==0:
                p=(spre+spre[::-1])
            else:
                p=(spre+spre[::-1][1:])
            if p!=nums:
                candidats.append(p)
        return (sorted(candidats,key = lambda x: (abs(num-int(x)),int(x)))[0])
		