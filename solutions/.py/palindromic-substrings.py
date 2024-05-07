class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ret = n
        if n == 0: return 0
        if n == 1: return 1
        i = 0.5
        while i < n:
            l = int(i - 0.5)
            r = int(i + 0.5)
            while l >= 0 and r < n:
                if s[l] == s[r]: 
                    ret+=1
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
                    ret+=1
                    l-=1
                    r+=1
                else:
                    break
            i+=1

        return ret