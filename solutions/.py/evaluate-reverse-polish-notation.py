class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"*", "/", "+", "-"}
        for a in tokens:
            if a in ops:
                c = stack.pop()
                b = stack.pop()
                if a == "*":
                    stack.append(b * c)
                elif a == "/":
                    if b * c >= 0:
                        stack.append(b // c)
                    else:
                        stack.append(-1 * (-1 * b // c))
                elif a == "+":
                    stack.append(b + c)
                else:
                    stack.append(b - c)
            else:
                stack.append(int(a))
        
        print(6 // -132)
        return stack[0]