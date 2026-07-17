class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for day, price in enumerate(prices):
            if day == 0:
                continue
            profit = price - lowest_price
            max_profit = max(max_profit, profit)
            lowest_price = min(lowest_price, price)
        return max_profit