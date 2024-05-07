class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict: return True
        
        trues = {-1}
        for i in range(0, len(s)):
            for a in trues:
                if s[a+1:i+1] in wordDict:
                    trues.add(i)
                    break

        if len(s) - 1 in trues: return True
        return False