class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        def search(current, index, target):
            if target == 0:
                print(current)
                ret.append(current[:])
                return
            if target < 0 or index == len(candidates):
                return
            current.append(candidates[index])
            search(current, index, target - candidates[index])
            current.pop()
            search(current, index + 1, target)

        search([], 0, target)
        return ret