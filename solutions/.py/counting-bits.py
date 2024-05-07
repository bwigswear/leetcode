class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n + 1):
            bits = 0
            n = i
            while n > 0:
                if n & 1:
                    bits+=1
                n = n >> 1
            a.append(bits)
        return a