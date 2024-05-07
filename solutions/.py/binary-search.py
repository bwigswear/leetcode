class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        a = 0
        b = len(nums) - 1
        c = (a + b) // 2
        while a <= b:
            if nums[c] == target:
                return c
            elif nums[c] < target:
                a = c + 1
                c = (a + b) // 2
            elif nums[c] > target:
                b = c - 1
                c = (a + b) // 2
        return -1