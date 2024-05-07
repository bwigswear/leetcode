class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        a = 0
        b = len(string) - 1
        while a < b:
            if not string[a].isalnum():
                a+=1
                continue
            elif not string[b].isalnum():
                b-=1
                continue
            else:
                if string[a] != string[b]:
                    return False
                else:
                    a+=1
                    b-=1
        return True