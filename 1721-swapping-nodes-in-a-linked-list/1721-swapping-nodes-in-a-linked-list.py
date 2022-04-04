# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t=k
        fir=head
        while t>1:
            fir=fir.next
            t-=1
        slow=head
        fast=fir
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.val,fir.val=fir.val,slow.val
        return head