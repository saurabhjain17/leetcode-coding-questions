class DLLNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.map=dict()
        self.capacity=capacity
        self.head=DLLNode(0,0)
        self.tail=DLLNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.count=0

    def get(self, key: int) -> int:
        if key in self.map:
            node=self.map[key]
            result=node.val
            self.deleteNode(node)
            self.addTohead(node)
            return result
            
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node=self.map[key]
            node.val=value
            self.deleteNode(node)
            self.addTohead(node)
        else:
            node=DLLNode(key,value)
            self.map[key]=node
            if self.count<self.capacity:
                self.count+=1
                self.addTohead(node)
            else:
                del self.map[self.tail.prev.key]
                self.deleteNode(self.tail.prev)
                self.addTohead(node)
    def deleteNode(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def addTohead(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)