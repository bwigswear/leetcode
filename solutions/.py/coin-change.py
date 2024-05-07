class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if len(coins) == 0: return 0

        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min = None
            for coin in coins:
                if i - coin < 0:
                    continue
                if dp[i - coin] == -1:
                    continue
                if min == None:
                    min = dp[i - coin]
                    continue
                if dp[i - coin] < min:
                    min = dp[i - coin]
            if min != None:
                dp[i] = min + 1
        return dp[amount]
                