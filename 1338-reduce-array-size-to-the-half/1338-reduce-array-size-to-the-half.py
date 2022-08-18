from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length=len(arr)
        to_remove=math.ceil(length/2)
        counti=0
        dic=Counter(arr)
        max_len=[]
        for i in dic:
            max_len.append(dic[i])
        max_len.sort(reverse=True)
        i=0
        while to_remove>0:
            counti+=1
            to_remove-=max_len[i]
            i+=1
        return counti    