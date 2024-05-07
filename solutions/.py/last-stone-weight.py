class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        b = stones
        for a in range(len(b)):
            b[a] = -1 * b[a]
        heapq.heapify(b)
        while len(b) > 1:
            c = -1 * heapq.heappop(b)
            d = -1 * heapq.heappop(b)
            if c != d:
                heapq.heappush(b, -1 * (c - d))
        if b:
            return -1 * b[0]
        else:
            return 0