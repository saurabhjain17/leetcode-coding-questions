class Node:
    def __init__(self,val,mini,nod_next=None):
        self.val=val
        self.mini=mini
        self.next=nod_next
        
class MinStack:

    def __init__(self): 
        
        self.stk=None  
    def push(self, val: int) -> None:
        
        if self.stk is None:
            self.stk=Node(val,val)
        else:
            t=self.stk.mini
            x=self.stk
            self.stk=Node(val,min(t,val),x)
    def pop(self) -> None:
        
        x=self.stk
        self.stk=self.stk.next
        x.next=None
    def top(self) -> int:
        return self.stk.val

    def getMin(self) -> int:
        return self.stk.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()