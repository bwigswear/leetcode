class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        a=0
        b=0
        c={}
        c[s[0]] = 0
        currentmax = 1
        max = 1
        while b < len(s):
            if b == len(s) - 2:
                if s[b + 1] in c or s[b+1] == s[b] or s[b+1] == s[a]:
                    break
                else:
                    currentmax+=1
                    if currentmax > max: max = currentmax
                    break
            if s[b+1] == s[b]:
                c.clear()
                b+=1
                a=b
                c[s[b]] = b
                currentmax = 1
            elif s[b+1] == s[a]:
                a+=1
                b+=1
                c[s[b]] = b
            elif s[b+1] in c:
                d = c[s[b+1]]
                for i in range(a, d):
                    del c[s[i]]
                    currentmax-=1
                c[s[d]] = b+1
                a = d
            else:
                c[s[b+1]] = b+1
                b+=1
                currentmax+=1
                if currentmax > max: max = currentmax

        return max