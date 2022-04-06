class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        dic=Counter(arr)
        n=len(arr)
        total=0
        i=0
        while i<n-2:
            j=i+1
            k=n-1
            new=target-arr[i]
            while j<k and j<n and k>-1:
                if arr[j]+arr[k]==new:
                    if arr[i]==arr[k]:
                        p=dic[arr[i]]
                        total=total+(p*(p-1)*(p-2)//6)
                    elif arr[j]==arr[k]:
                        p=dic[arr[j]]
                        tem=p*(p-1)//2
                        total+=tem*dic[arr[i]]
                    elif arr[i]==arr[j]:
                        p=dic[arr[j]]
                        tem=p*(p-1)//2
                        total+=tem*dic[arr[k]]
                    else:
                        total+=dic[arr[i]]*dic[arr[j]]*dic[arr[k]]
                    j+=1
                    k-=1
                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while k>j and arr[k]==arr[k+1]:
                        k-=1
                        
                elif arr[j]+arr[k]>new:
                    
                        k-=1
                else:
                    j+=1
            i+=1        
            while i<n-2 and arr[i]==arr[i-1]:
                i+=1
        return total%(10**9+7)           
            