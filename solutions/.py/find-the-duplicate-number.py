class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort() 
        for a in range(len(nums)): 
            if nums[a] == nums[a+1]: return nums[a]