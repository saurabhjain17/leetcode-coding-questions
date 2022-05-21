# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        def rec(node,k):
            if node is None or node.next is None:
                return node
            t=1
            tem=node
            new=None
            while t<k and tem:
                tem=tem.next
                t+=1
            if tem is None:
                return node
            if tem:
                new=tem.next
                tem.next=None
            ppre=None
            cur=node
            nex=node.next
            while cur:
                cur.next=ppre
                ppre=cur
                cur=nex
                if nex:
                    nex=nex.next
            node.next=rec(new,k)
            return ppre
        temi=ListNode(0)
        temi.next=rec(head,k)
        return temi.next