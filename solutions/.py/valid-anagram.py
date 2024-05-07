class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        d = {}
        if len(s) != len(t): return False
        for b in s:
            a[b] = a[b] + a.get(b, 0) if a.get(b,0) else 1
        for c in t:
            d[c] = d[c] + d.get(c, 0) if d.get(c,0) else 1
        for b in s:
            if a.get(b, 0) != d.get(b, 0): return False
        return True