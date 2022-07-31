class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n=len(grades)
        counti=(-1+(1+8*n)**.5)//2
        return int(counti)