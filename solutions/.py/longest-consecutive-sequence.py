class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for a in nums:
            d[a] = 1
        
        for a in d:
            n = a
            while n != None:
                if d.get(n - 1, 0) > 0:
                    n-=1
                    d[a]+=d[n]
                    d[n] = -1
                else:
                    n = None
        max = 0
        for a in d:
            max = d[a] if d[a] > max else max
        return max