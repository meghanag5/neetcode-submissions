class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_h, t_h = {}, {}
        for x in range(len(s)):
            s_h[s[x]] = 1 + s_h.get(s[x], 1) # if item exists add one if it doesnt put a 1
            t_h[t[x]] = 1 + t_h.get(t[x], 1)
        for l, c in s_h.items():
            if l not in t_h.keys() or t_h[l] != c:
                return False
        return True

