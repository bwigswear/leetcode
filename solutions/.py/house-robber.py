class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a = [0] * n
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        a[0], a[1] = nums[0], nums[1]
        for b in range(2, n):
            a[b] = max(a[:b-1]) + nums[b]
        return max(a[n-1], a[n-2])