class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        istack = [0]
        tstack = [temperatures[0]]
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(tstack) > 0 and temperatures[i] > tstack[-1]:
                index = istack.pop()
                ret[index] = i - index
                tstack.pop()
            tstack.append(temperatures[i])
            istack.append(i)

        return ret