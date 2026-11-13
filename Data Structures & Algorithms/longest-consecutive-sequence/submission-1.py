class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # iterate through the list each number -1 !exists = a start
        if len(nums) == 0:
            return 0
        guide = {}
        new = set(nums) # removes duplicates
        for item in new:
            prev = item -1 
            count = 1
            if prev not in new:
                
                guide[item] = 0
                n = item + 1
                while n in new:
                    count += 1
                    n += 1
                guide[item] = count
        return max(guide.values())

            
            
