class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 写个暴力把 o(n^2)
        res = 0
        n = len(prices)

        for i in range(len(prices)-1):
            price = prices[i]
            cmax = max(prices[i+1:n])
            profit = cmax - price
            res = max(res, profit)

        return res
