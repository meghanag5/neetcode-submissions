from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for item in strs:
            sort = " ".join(sorted(item))
            ans[sort].append(item) 
        return list(ans.values())