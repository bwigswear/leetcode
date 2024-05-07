class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        front = 0
        back = len(nums) - 1
        while front <= back:
            if nums[front] == val:
                nums[front] = nums[back]
                back-=1
            else:
                k+=1
                front+=1
        return k

        