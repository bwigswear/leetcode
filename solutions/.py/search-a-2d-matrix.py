class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        front = 0
        back = m * n - 1
        index = int(back / 2)
        while(1):
            current = matrix[int(index / n)][int(index % n)]
            if current == target:
                return True
            elif front >= back:
                return False
            elif current < target:
                front = index + 1
                index = (front + back) / 2
            elif current > target:
                back = index - 1
                index = (front + back) / 2