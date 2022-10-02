class Node:
      def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild=None
class Solution:
    def checkCount(self,start,mid,end,d):
        global counti
        global arr
        l=start
        r=mid+1
        while l<=mid and r<=end:
            if arr[l]<=arr[r]+d:
                counti+=end-r+1
                l+=1
            else:
                r+=1
        # arr=arr[:start]+sorted(arr[start:end+1])+arr[end+1:]        
        l=start
        r=mid+1
        tem=[]
        while l<=mid and r<=end:
            if arr[l]<=arr[r]:
                tem.append(arr[l])
                l+=1
            else:
                tem.append(arr[r])
                r+=1
        while l<=mid:
            tem.append(arr[l])
            l+=1
        while r<=end:
            tem.append(arr[r])
            r+=1
        l=start        
        for i in range(len(tem)):
            arr[l+i]=tem[i]
                
    def mergeSort(self,start,end,d):
        global arr
        if start==end:
            return
        mid=(start+end)//2
        self.mergeSort(start,mid,d)
        self.mergeSort(mid+1,end,d)
        self.checkCount(start,mid,end,d)
        
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n=len(nums1)
        global arr
        arr=[0]*n
        for i in range(n):
            arr[i]=nums1[i]-nums2[i]
         
       
        global counti
        counti=0
        self.mergeSort(0,n-1,diff)
        
        return counti