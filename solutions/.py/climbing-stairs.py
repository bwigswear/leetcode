class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        a = [0] * n
        a[0] = 1
        a[1] = 2
        for b in range(2,n):
            a[b] = a[b-1] + a[b-2]
        return a[n-1]