# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length=0
        nod=head
        while nod:
            length+=1
            nod=nod.next
        ans=[0]*(length//2) 
        nod=head
        
        for i in range(length//2):
            ans[i]+=nod.val
            nod=nod.next
        for i in range(length//2-1,-1,-1):
            ans[i]+=nod.val
            nod=nod.next
        return max(ans)    
            