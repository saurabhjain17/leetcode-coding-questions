class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        n=len(matrix[0])
        high=len(matrix)-1
        count=False
        while low<high:
            mid =(low+high)//2
            if matrix[mid][n-1]<target:
                low=mid+1
            elif matrix[mid][0]>target:
                high=mid-1
            elif matrix[mid][n-1]>=target and matrix[mid][0]<=target:   
                count=True
                break
        if count or (matrix[low][n-1]>=target and matrix[low][0]<=target): 
            tmid=(low+high)//2
            low=0
            high=n-1
           
            while low<high:
                mid=(low+high)//2
                if matrix[tmid][mid]==target:
                    return True
                elif matrix[tmid][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            if matrix[tmid][low]==target:
                return True
        return False    