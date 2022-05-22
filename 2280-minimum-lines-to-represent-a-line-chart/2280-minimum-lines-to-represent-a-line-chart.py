import math
class Solution:
#     def getReducedForm(self,y,x):
#         ans= math.gcd(abs(y),abs(x))

#         # get sign of result
#         sign = (y<0)^(x < 0)

#         if (sign):
#             return (-abs(y)//ans,abs(x)//ans)
#         else:
#             return (abs(y)//ans,abs(x)//ans)
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        stockPrices.sort(key = lambda x: x[0])
        
        if n == 1:
            return 0
        
        pre_delta_y = stockPrices[0][1] - stockPrices[1][1]
        pre_delta_x = stockPrices[0][0] - stockPrices[1][0]
        num = 1
        
        for i in range(1, n-1):
            cur_delta_y = stockPrices[i][1] - stockPrices[i+1][1]
            cur_delta_x = stockPrices[i][0] - stockPrices[i+1][0]
            
            if pre_delta_y * cur_delta_x != pre_delta_x * cur_delta_y:
                num += 1
                pre_delta_x = cur_delta_x
                pre_delta_y = cur_delta_y
        
        return num
#         stockPrices.sort(key=lambda x:(x[0],x[1]))
#         print(stockPrices)
#         dic=dict()
        
#         n=len(stockPrices)
#         if n<3:
#             return n-1
    
#         slop=(stockPrices[1][1]-stockPrices[0][1])/(stockPrices[1][0]-stockPrices[0][0])
#         dic[slop]=[stockPrices[0]]
       
#         ans=1
#         for i in range(2,n):
#             slop2=(stockPrices[i][1]-stockPrices[i-1][1])/(stockPrices[i][0]-stockPrices[i-1][0])
#             if slop!=slop2:
#                 slop=slop2
#                 ans+=1
#                 # if slop2 not in dic:
#                 #     ans+=1
#                 #     dic[slop2]=[stockPrices[i]]
#                 #     slop=slop2
#                 # else:
#                 #     tem=slop2
#                 #     flag=0
#                 #     for point in dic[slop2]:
#                 #         if (stockPrices[i][1]-point[1])/(stockPrices[i][0]-point[0])==tem:
#                 #             flag=1
#                 #             break
#                 #     if flag==0:
#                 #         ans+=1
#                 #         dic[slop2].append(stockPrices[i])
#                 # slop=slop2        
#         return ans      