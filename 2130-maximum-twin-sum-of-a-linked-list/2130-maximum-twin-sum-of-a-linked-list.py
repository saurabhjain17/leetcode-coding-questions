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
        p=length//2    
        ans=[0]*p 
        nod=head
        
        
        for i in range(p):
            ans[i]+=nod.val
            nod=nod.next
        p=p-1    
        for i in range(p,-1,-1):
            ans[i]+=nod.val
            nod=nod.next
        return max(ans)    
            