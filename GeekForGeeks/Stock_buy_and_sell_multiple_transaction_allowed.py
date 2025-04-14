from typing import List


class Solution:
    def maximumProfit(self, price) -> int:
        # code here
        n = len(price)
        profit = 0
        buy = 0
        hold = 0
        
        for i in range(n-1):
            if price[i] < price[i+1] and hold == 0:
                buy = i
                hold = 1
            elif price[i] > price[i+1] and hold == 1:
                profit += price[i] - price[buy]
                hold = 0
        
        if price[-1] > price[buy] and hold == 1:
            profit += price[-1] - price[buy]
            
        
        return profit
