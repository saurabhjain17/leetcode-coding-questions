
from queue import Queue
class MyStack:

    def __init__(self):
        self.q=Queue()

    def push(self, x: int) -> None:
        self.q.put(x)
        length=self.q.qsize()
        while length>1:
            self.q.put(self.q.get())
            length-=1
        

    def pop(self) -> int:
        return self.q.get()

    def top(self) -> int:
        top=self.q.get()
        self.push(top)
        return top

    def empty(self) -> bool:
        return self.q.qsize()==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()