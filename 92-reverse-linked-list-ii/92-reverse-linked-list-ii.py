# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,nod,right):
        x=0
        tem=nod
        while x<right:
            tem=tem.next
            x+=1
        rig=tem.next
        tem.next=None
        pprv=rig
        cur=nod
        nex=cur.next
        while cur:
            cur.next=pprv
            pprv=cur
            cur=nex
            if nex:
                nex=nex.next
        
        return pprv
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left==right:
            return head
        dummy=ListNode(0,head)
        nod=dummy
        left-=1
        right-=1
        
        while left:
            nod=nod.next
            left-=1
            right-=1
        nod.next=self.rev(nod.next,right)
        return dummy.next