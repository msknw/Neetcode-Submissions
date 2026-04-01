class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming: O(n)
        # 这个真有点意思把 +1 

        res = 0
        minBuy = prices[0]

        for sell in prices:
            res = max(res, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return res

