# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # odd=ListNode(0)
        # even=ListNode(0)
        odd=head
        even=head.next
        x=even.next
        even.next=None
        odd.next=None
        y=even
        z=odd
        ind=1
        
        while x is not None:
            if ind==1:
                z.next=x
                z=z.next
                x=x.next
                z.next=None
            else:
                y.next=x
                y=y.next
                x=x.next
                y.next=None
            ind=(ind+1)%2
        z.next=even
        return  odd
            
        