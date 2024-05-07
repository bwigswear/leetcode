class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1: return 0
        if n == 2: return min(cost[0], cost[1])
        a = [0] * n
        a[0], a[1] = cost[0], cost[1]
        for b in range(2, n):
            a[b] = min(a[b-1], a[b-2]) + cost[b]
        return min(a[n - 1], a[n - 2])