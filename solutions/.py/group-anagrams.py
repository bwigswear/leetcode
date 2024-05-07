class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = {}
        for a in strs:
            b = ''.join(sorted(a))
            if dd.get(b, 0) == 0:
                dd[b] = [a]
            else:
                dd[b].append(a)

        return dd.values()