class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n==0:
            return -1
        if n<10:
            return -1
        arr=[]
        k=n
        while k>0:
            arr.append(k%10)
            k//=10
        arr=arr[::-1]
        k=-1
        leng=len(arr)
        for i in range(leng-2,-1,-1):
            if arr[i]<arr[i+1]:
                k=i
                break
        if k==-1:
            return -1
        for i in range(leng-1,-1,-1):
            if arr[i]>arr[k]:
                j=i
                break
        arr[j],arr[k]=arr[k],arr[j]
        # print
        p=k+1
        q=leng-1
        while p<q:
            arr[p],arr[q]=arr[q],arr[p]
            p+=1
            q-=1
        num=0
        for i in arr:
            num*=10
            num+=i
        if num<=2**31-1:    
            return num  
        return -1