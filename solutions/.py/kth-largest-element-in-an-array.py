class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = []
        for c, b in enumerate(nums):
            if c < k:
                heapq.heappush(a, b)
            else:
                heapq.heappush(a, b)
                heapq.heappop(a)

            
        return heapq.heappop(a)