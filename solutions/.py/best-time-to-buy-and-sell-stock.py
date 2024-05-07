class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0
        buy = 0
        sell = 1
        a = 0
        b = 1

        while b < len(prices):
            if prices[sell] - prices[buy] < prices[b] - prices[a]:
                sell = b
                buy = a
            if prices[b] < prices[a]:
                a = b
            b+=1
        
        profit = prices[sell] - prices[buy]
        return profit if profit > 0 else 0