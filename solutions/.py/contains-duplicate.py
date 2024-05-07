class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for a in range(1, len(nums)):
            if nums[a] == nums[a-1]:
                return True

        return False