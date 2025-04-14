class Solution:
    def maximumProfit(self, prices):
        # code here
        profit = 0
        
        n = len(prices)
        index = 0
        min_price = 10000
        max_price = 0
        
        for i in range(1, n):
            if prices[i-1] < prices[i] and prices[i-1] < min_price:
                index = i -1
                min_price = prices[i-1]
                # print(min_price)
            
            if prices[i-1] > min_price and (prices[i-1] - min_price) > profit:
                profit = prices[i-1] - min_price
            # elif prices[i-1] > min_price and i-1 > index and prices[i-1] > max_price:
            #     # print(prices[i-1])
            #     max_price = prices[i-1]
            #     print(max_price)
            
            # if max_price - min_price > profit:
            #     print(min_price, max_price)
            #     profit = max_price - min_price
            #     print(profit)
        
        if prices[-1] > min_price and (prices[-1] - min_price) > profit:
            profit = prices[-1] - min_price
        
        # min = 0
        # max = 0
        
        # for i in range(n-1):
        #     if prices[i] < prices[min]:
        #         min = i
                
        # for i in range(min, n):
        #     if prices[i] > prices[i-1]:
        #         max = i

        # print(min, max)
        # if prices[max] >= prices[min] and max > min:
        #     profit = prices[max] - prices[min]

        return profit