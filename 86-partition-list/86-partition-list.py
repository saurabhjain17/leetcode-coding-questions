# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=ListNode(0)
        dummy2=ListNode(0)
        nd1=dummy1
        nd2=dummy2
        tem=head
        while tem:
            if tem.val<x:
                nd1.next=tem
                nd2.next=None
                nd1=nd1.next
            else:
                nd2.next=tem
                nd1.next=None
                nd2=nd2.next
            tem=tem.next
        nd1.next=dummy2.next
        return dummy1.next