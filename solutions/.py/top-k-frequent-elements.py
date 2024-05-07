class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for a in nums:
            if d.get(a, 0) == 0:
                d[a] = 1
            else:
                d[a]+=1

        a = []
        heapq.heapify(a)
        for b in d:
            heapq.heappush(a, (d[b], b))
            if len(a) > k: heapq.heappop(a)
        
        r = []
        for b in a:
            r.append(b[1])

        return r