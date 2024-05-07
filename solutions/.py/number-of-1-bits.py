class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 0
        while n > 0:
            if n & 1 == 1:
                a+=1
            n = n >> 1
        return a