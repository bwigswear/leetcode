class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        sup = []
        sup.append(sub)

        def b(i, sub, sup):
            for j, num in enumerate(nums[i+1:]):
                new = sub[:]
                new.append(num)
                sup.append(new)
                b(j + i + 1, new, sup)


        for i, num in enumerate(nums):
            sub = [num]
            sup.append(sub)
            b(i, sub, sup)

        return sup