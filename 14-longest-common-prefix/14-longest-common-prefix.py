class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=""
        for i in zip(*strs):
            seti=set(i)
            if len(seti)==1:
                out+=list(seti)[0]
            else:
                return out
        return out    