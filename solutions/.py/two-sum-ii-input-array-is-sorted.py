class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1
        if b < 1: return None
        while a < b:
            if numbers[a] + numbers[b] == target:
                return [a + 1, b + 1]
            elif numbers[a] + numbers[b] > target:
                b-=1
            else:
                a+=1

        return None