import queue
class Solution:
    def sholdenter(self,fir,sec,n):
        counti=0
        i=0
        while i<n and counti<2:
            if fir[i]!=sec[i]:
                counti+=1
            i+=1
        if counti<2:
            return True
        return False
                
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n=len(wordList)
        t=len(beginWord)
        if endWord not in wordList:
            return 0
        ans_ind=wordList.index(endWord)
        dp=[0]*n
        q=queue.Queue()
        q.put((beginWord,1))
        size=1
        while size>0:
            nod,dis=q.get()
            size-=1
            for i in range(n):
                if dp[i]==0 and self.sholdenter(wordList[i],nod,t):
                    if i==ans_ind:
                        return dis+1
                    else:
                        dp[i]=1
                        q.put((wordList[i],dis+1))
                        size+=1
        return 0                