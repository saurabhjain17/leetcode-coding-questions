
from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = point = ListNode(0)
        q = PriorityQueue()
        k=0
        for l in lists:
            if l:
                q.put((l.val,k, l))
                k+=1
                
        while not q.empty():
            val,t, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val,k, node))
                k+=1
        return head.next