class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n=len(queries)
        dic=dict()
        for i in range(n):
            if queries[i] not in dic:
                dic[queries[i]]=[]
            dic[queries[i]].append(i)
        arr=list(sorted(dic.keys()))    
        ans=[0]*n
        items.sort()
        i=0
        maxi=0
        m=len(items)
        for j in arr:
            while i<m and items[i][0]<=j:
                
                maxi=max(items[i][1],maxi)
                i+=1
            for k in dic[j]:
                ans[k]=maxi
        return ans        