class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        new_s = {}
        new_t = {}
        for item in range(len(s)):
            new_s[s[item]] = 1 + new_s.get(s[item], 0)
            new_t[t[item]] = 1 + new_t.get(t[item], 0)
        for item in new_s:
            if new_s[item] != new_t.get(item, 0):
                return False
        return True
