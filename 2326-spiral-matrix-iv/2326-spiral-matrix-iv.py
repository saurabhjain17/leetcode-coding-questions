# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat=[[-1]*n for i in range(m)]
        top=0
        left=0
        right=n-1
        bottom=m-1
        while head is not None:
            if left>right:
                break
            i=left    
            while i<=right and head:
                mat[top][i] = head.val
                head=head.next  
                i+=1
            
            top += 1;
            if (top > bottom):
                break
 
            i=top
            while i<=bottom and head:
                mat[i][right] =head.val
                head=head.next
                i+=1
            right -= 1;

            if (left > right):
                break

            i=right
            while i>=left and head:
                mat[bottom][i] = head.val
                head=head.next
                i-=1
            bottom -= 1;

            if (top > bottom):
                break

            i=bottom
            while head and i>=top:
                mat[i][left] = head.val
                head=head.next
                i-=1
            left += 1
        return mat     
            