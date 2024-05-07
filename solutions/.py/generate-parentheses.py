class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 0: return []

        ret = []

        def a(stack, size, open):
            nonlocal n
            if size == n * 2:
                nonlocal ret
                ret.append(stack)
                return
            if n * 2 - size == open:
                stack+=open*")"
                ret.append(stack)
                return
            stack+="("
            a(stack, size + 1, open + 1)
            stack = stack[:-1]
            if open > 0:
                stack+=")"
                a(stack, size + 1, open - 1)
        a("", 0, 0)
        return ret