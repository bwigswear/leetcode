class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        int = 0
        for a in nums:
            int = a ^ int
        return int