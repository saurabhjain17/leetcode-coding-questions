class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle=[]
        n=len(s)
        for i in range(n):
            if s[i]=="|":
                candle.append(i)
        prefix=[]
        size=0
        for i in s:
            if i=="*":
                if size==0:
                    prefix.append(1)
                    
                else:
                    prefix.append(prefix[-1]+1)
                size+=1
                
            else:
                if size==0:
                    prefix.append(0)
                    
                else:
                    prefix.append(prefix[-1])
                size+=1
                
        # print(prefix)        
        ans=[]
        # print(candle)
        candle_length=len(candle)
        for u,v in queries:
            if candle_length<2:
                ans.append(0)
                continue
            ind=candle[0]
            low=0
            high=candle_length-1
            while low<=high:
                mid=(low+high)//2
                if candle[mid]>=u and candle[mid]<=v:
                    # print("OK",candle[mid])
                    ind=candle[mid]
                    low=mid+1
                elif candle[mid]<u:
                    low=mid+1
                elif candle[mid]>v:
                    high=mid-1
            ind2=candle[-1]
            low=0
            high=candle_length-1
            while low<=high:
                mid=(low+high)//2
                if candle[mid]>=u and candle[mid]<=v:
                    ind2=candle[mid]
                    high=mid-1
                elif candle[mid]<u:
                    low=mid+1
                elif candle[mid]>v:
                    high=mid-1 
            # print(ind,ind2)        
            if ind>ind2:
                ans.append(prefix[ind]-prefix[ind2])
            else:
                ans.append(0)
        return ans        