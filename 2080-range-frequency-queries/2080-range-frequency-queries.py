from collections import Counter
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dic=dict()
        n=len(arr)
        for i in range(n):
            if arr[i] not in self.dic:
                    self.dic[arr[i]]=[]
            self.dic[arr[i]].append(i)       
    def query(self, left: int, right: int, value: int) -> int:
        start=0
        if value not in self.dic:
            return 0
        end=len(self.dic[value])-1
        ans1=end
        while start<=end:
             mid=(start+end)//2
             p=self.dic[value][mid] 
             if p>right:
                    end=mid-1
             else:
                ans1=mid
                start=mid+1
        start=0
        end=len(self.dic[value])-1
        ans2=start
        while start<=end:
             mid=(start+end)//2
             p=self.dic[value][mid] 
             if p<left:
                    start=mid+1
             else:
                ans2=mid
                end=mid-1
        if self.dic[value][ans1]>=left and self.dic[value][ans1]<=right:        
             return ans1-ans2 +1
        return 0    


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)