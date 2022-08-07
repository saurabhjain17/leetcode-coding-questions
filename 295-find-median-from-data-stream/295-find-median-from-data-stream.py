class MedianFinder:

    def __init__(self):
        self.left_heap=[]
        self.left_size=0 
        self.right_heap=[]
        self.right_size=0
        self.median=-1e10
    def addNum(self, num: int) -> None:
        if self.left_size==self.right_size:
            if self.median>=num:
                heapq.heappush(self.left_heap,-num)
                self.left_size+=1
            else:
                heapq.heappush(self.right_heap,num)
                self.right_size+=1
        elif  self.left_size<self.right_size:
            if self.median>=num:
                heapq.heappush(self.left_heap,-num)
                self.left_size+=1   
            else:
                
                heapq.heappush(self.right_heap,num)
                heapq.heappush(self.left_heap,-heapq.heappop(self.right_heap))
                self.left_size+=1
        else:
            if self.median>=num:
                heapq.heappush(self.left_heap,-num)
                heapq.heappush(self.right_heap,-heapq.heappop(self.left_heap)) 
                self.right_size+=1
            else:
                
                heapq.heappush(self.right_heap,num)
                self.right_size+=1
        if self.left_size==self.right_size:
            self.median=(-self.left_heap[0]+self.right_heap[0])/2
        elif  self.left_size>self.right_size:
            self.median=-self.left_heap[0]
        else:
            self.median=self.right_heap[0]
                


    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()