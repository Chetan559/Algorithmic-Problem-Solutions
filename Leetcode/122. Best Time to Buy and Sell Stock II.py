class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            margin = prices[i] - prices[i-1]
            if margin > 0:
                res += margin
        
        return res