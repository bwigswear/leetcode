class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        size = m
        for a in nums2:
            for b in nums1:
                if index == size:
                    nums1.insert(index, a)
                    size += 1
                    break
                if a < b:
                    nums1.pop()
                    nums1.insert(index, a)
                    size += 1
                    break
                else:
                    index+=1
                    continue
            index = 0
        del nums1[size:]
