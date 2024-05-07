class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums) - 2:
            if nums[index] in nums[index+2:]:
                nums.pop(index)
            else:
                index+=1
        return len(nums)