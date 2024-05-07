class Solution:
    def rob(self, nums: List[int]) -> int:
        
        b = len(nums)
        if b == 0: return None
        if b == 1: return nums[0]
        if b == 2: return max(nums[0], nums[1])
        if b == 3: return max(nums)

        def a(nums):
            nums[0] = nums[0]
            nums[1] = nums[1]
            nums[2] = nums[2] + nums[0]
            i = 3
            while i < len(nums):
                nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])
                i+=1
            return max(nums[len(nums)-1], nums[len(nums)-2])

        return max(a(nums[1:]), a(nums[:-1]))