class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Scenarios:
        1. Encounter 0
            -0 before -> bad
            -3-9 before -> bad
            -1-2 before -> current and last dp now equal dp - 2
        2. Encounter 1-9
            -0 before -> same as dp -1
            -1 before -> dp + 1
            -2 before -> dp + 1 if 1-6
            -3-9 before -> same as dp
        """
        if s[0] == '0': return 0
        dp = []
        dp.append(1)
        
        for i in range(1, len(s)):
            a = int(s[i])
            b = int(s[i - 1])
            if a == 0:
                if b == 0 or b > 2:
                    return 0
                elif len(dp) == 1:
                    dp.append(1)
                else:
                    dp[i - 1] = dp[i - 2]
                    dp.append(dp[i - 2])
            else:
                if b == 0:
                    dp.append(dp[i - 1])
                elif b == 1:
                    if len(dp) == 1:
                        dp.append(2)
                    else:
                        dp.append(dp[i - 1] + dp[i - 2])
                elif b == 2 and (a < 7 and a > 0):
                    if len(dp) == 1:
                        dp.append(2)
                    else:
                        dp.append(dp[i - 1] + dp[i - 2])
                else:
                    dp.append(dp[i - 1])
        return dp.pop()