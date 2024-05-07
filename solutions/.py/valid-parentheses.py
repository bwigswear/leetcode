class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        dict = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b in opens:
                a.append(b)
            elif b in closes:
                if len(a) == 0: return False
                if a.pop() != dict[b]:
                    return False
        return not len(a)