class Solution:
    def reverseBits(self, n: int) -> int:
        a = 0
        result = 0
        while a < 32:
            if n & (2 ** a):
                result += 2 ** (31 - a)
            a+=1
        return result