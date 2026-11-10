class Solution:
    # [2, 3, 6, 2, 7, 3]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freqency into a dict
        # store the value in dict with 1 if it exisst just increment it by 1
        guide = {}
        freq = [[] for item in range(len(nums) + 1)] 
        for item in nums:
            guide[item] = 1 + guide.get(item, 0)
        # {2, 3, 6, 7,} key/ number
        # {2, 3, 1, 1,} value/ count
        # now we need the count(value) and the number(key) and store key at position = value
        for number, count in guide.items():
            freq[count].append(number)
        # [[], [], [], [], [], [], []]
        # [ 0,  1,  2,  3,  4,  5,  6]
        res = []
        # iterate backwards through the freq array
        for i in range(len(freq) - 1, 0, -1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res

        
            