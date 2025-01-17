class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            index = len(digits) - 1
            while index >= 0:
                if digits[index] == 9:
                    digits[index] = 0
                else:
                    digits[index] += 1
                    return digits
                index-=1
            digits.insert(0, 1)

        return digits