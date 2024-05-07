class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        seen = set()

        while num != 1:
            if num in seen: return False
            seen.add(num)
            newnum = 0
            string = str(num)
            for char in string:
                newnum += int(char) ** 2
            num = newnum

        return True