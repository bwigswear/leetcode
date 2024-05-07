class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: return None
        if n == 1: return s
        max = 1
        ret = 0, 0
        i = 1
        while i < n:
            l = int(i - 0.5)
            r = int(i + 0.5)
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    if r - l + 1 > max: max = r - l + 1; ret = l, r
                    l-=1
                    r+=1
                else:
                    break
            i+=1
        
        i = 1
        while i < n:
            l = i - 1
            r = i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    if r - l + 1 > max: max = r - l + 1; ret = l, r
                    l-=1
                    r+=1
                else:
                    break
            i+=1
        return s[ret[0]:ret[1]+1]