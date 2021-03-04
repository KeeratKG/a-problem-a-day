# 4th March 2021 

'''
Problem: 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
#         '''
#         Identify min value. Then max from any index that is greater than that of min value. Subtract both and return the result. 
#         '''
#         arr = []
#         buy = min(prices)
#         buy_index =  prices.index(buy)
#         print(buy_index)
#         for i in range(buy_index, len(prices)):
#             arr.append(prices[i])
#         print(arr)
#         sell = max(arr)
        
#         maxprofit = sell - buy 
        
#         return maxprofit

            '''
            The previous approach is incorrect. To maximise the profit you may not always need the absolute minimum. Sometimes a bigger value can generate more profit than a zero profit at the minimum. See eg: [2,4,1] for reference. 
            Thus, the selection of suitable min and evaluation of max profit has to be done simultaneously, not sequentially. 
            '''

            min_till_now = prices[0]
            max_profit = 0
            for price in prices[1:]:
                if price < min_till_now:
                    min_till_now = price
                else:
                    diff = price - min_till_now
                    if max_profit < diff:
                        max_profit = diff
            return max_profit
