class Solution:
#["code", "Hand", "Dog"]
#[4, 4, 3]
    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res += str(len(item)) + "#" + item
        return res
# "4#code4#Hand3#Dog"
    def decode(self, s: str) -> List[str]:
        i = 0 # pointer throughout string
        res = [] # result output
        while i < len(s): #iterates through string length
            j = i # incremental pointer
            while s[j] != "#": # checks for split
                j += 1 # keep goign till # is found
            # once # is found get number length
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            i = j + 1 + length
            res.append(word)
        return res