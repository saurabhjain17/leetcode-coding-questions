class Solution:
    def minPartitions(self, n: str) -> int:
        maxi="0"
        for i in n:
            if i=="9":
                return 9
            if i>maxi:
                maxi=i
        return maxi    