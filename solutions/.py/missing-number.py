class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 1: return 0
        if 0 not in nums: return 0
        max = 0
        sum = 0
        for a in nums:
            if a > max: max = a 
            sum+=a
        
        b = 0
        for a in range(max + 1):
            b+=a

        dif = b - sum
        return dif if dif > 0 else max + 1