class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            if target - nums[a] in nums[a + 1:]:
                return [a, nums[a+1:].index(target - nums[a]) + a + 1]