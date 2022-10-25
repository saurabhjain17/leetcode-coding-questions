# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rec(self,root):
        if root is None or root.next is None:
            return root
        ppr=None
        cur=root
        nex=root.next
        while cur:
            cur.next=ppr
            ppr=cur
            cur=nex
            if nex:
                nex=nex.next
        return ppr    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if (head==None or head.next==None or head.next.next==None):
            return
        fast=slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        t=slow.next    
        slow.next=None
        fast=t
        slow=head
       
        fast=self.rec(fast)
         
        while fast:
            t=slow.next
            slow.next=fast
            fast=fast.next
            slow.next.next=t
            slow=t
        return head    
