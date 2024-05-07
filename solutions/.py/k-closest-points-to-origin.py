class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 0: return []
        h = []
        heapq.heapify(h)
        size = 0
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if size < k:
                heapq.heappush(h, [-1 * distance, point])
                size+=1
            elif distance < -1 * h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, [-1 * distance, point])

        return [x[1] for x in h]