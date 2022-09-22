class Node:
    def __init__(self):
        self.link=[None]*2
class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                p[cur] = {}
            p = p[cur]
                
    def getMax(self, num):
        if not self.root: 
            return -1
        p, ans = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                ans |= (1 << i)
            else:
                p = p[cur]
        return ans       
            
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        trie=Trie()
        query=[]
        n=len(nums)
        q=len(queries)
        for i in range(q):
            query.append([queries[i][1],queries[i][0],i])
        query.sort()    
        i=0
        op=dict()
        ans=[-1]*q
        for a,x,j in query:
            while i<n and a>=nums[i]:
                trie.insert(nums[i])
                i+=1
            if i>0:
                if (x,a) in op:
                    ans[j]=op[(x,a)]
                else:    
                    p=trie.getMax(x)
                    ans[j]=p
                    op[(x,a)]=p
                # for k in dic[(x,a)]:
                #     ans[k]=p
        return ans        