class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic=dict()
        for i in words:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        ans=0
        midi=0
        for i in dic:
            if dic[i]>0:
                if i[0]==i[1]:
                    if dic[i]%2==0:
                        ans+=2*dic[i]
                        
                        dic[i]=0
                        continue
                    else:
                        if midi==0:
                            ans+=2*dic[i]
                            midi=1
                        else:
                            ans+=2*(dic[i]-1)
                        dic[i]=0    
                else:
                    tem=i[1]+i[0]
                    if tem in dic:
                        ans+=min(dic[i],dic[tem])*4
                        dic[tem]=0
                        dic[i]=0
                # print(ans,i)        
        return ans                
        