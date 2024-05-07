class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        l = len(self.left)
        r = len(self.right)

        if l > r:
            if (self.left[0] * -1) < num:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, num * -1)
                heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        elif r > l:
            if self.right[0] > num:
                heapq.heappush(self.left, num * -1)
            else:
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))
        else:
            if l == 0:
                heapq.heappush(self.left, num * -1)
            else:
                if num < self.right[0]:
                    heapq.heappush(self.left, num * -1)
                else:
                    heapq.heappush(self.right, num)

    def findMedian(self) -> float:
        l = len(self.left)
        r = len(self.right)

        if l == r:
            return ((-1 * self.left[0]) + self.right[0]) / 2
        elif l > r:
            return -1 * self.left[0]
        else:
            return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()