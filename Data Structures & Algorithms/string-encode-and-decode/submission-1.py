class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res += str(len(item)) + "#" + item #encoding item    
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # iterating through list to find length and then the string
        while i < len(s):
            j = i 
            # assuming i = 0 in start "5#Count4#Hand"; i = 0, j = 0
            while s[j] != "#":
                j += 1 # poitns at # ; j = 1; item = (j + 1)2 : len + j + 1 = 7, splicing excludes last
            length = int(s[i:j])
            string = s[j + 1 : j + 1 + length]

            res.append(string)
            i = j + 1 +length
        return res



