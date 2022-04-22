class MyHashMap:

    def __init__(self):
        self.bucket_size=10**6
        self.lis=[None]*self.bucket_size
        

    def put(self, key: int, value: int) -> None:
        self.lis[key%self.bucket_size]=value

    def get(self, key: int) -> int:
        ind=key%self.bucket_size
        if self.lis[ind]==None:
            return -1
        return self.lis[ind]

    def remove(self, key: int) -> None:
        self.lis[key%self.bucket_size]=None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)