class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        length=1
        seti=set()
        size=0
        for i in rolls:
            if i not in seti:
                seti.add(i)
                size+=1
            if size==k:
                length+=1
                size=0
                seti=set()
        return length        