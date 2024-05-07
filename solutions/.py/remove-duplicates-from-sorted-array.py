class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums) - 1:
            if nums[index] in nums[index+1:]:
                nums.pop(index)
            else:
                index+=1
        return len(nums)