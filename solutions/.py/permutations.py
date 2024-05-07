class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        index = 0

        a = set()
        size = 0
        n = len(nums)
        sets = []

        def search(set, array, size, sets):
            if size == n:
                sets.append(array)
                return
            for num in nums:
                if num not in set:
                    set.add(num)
                    array.append(num)
                    search(set.copy(), array[:], size + 1, sets)
                    array.pop()
                    set.remove(num)
            

        search(a, [], 0, sets)
        return sets