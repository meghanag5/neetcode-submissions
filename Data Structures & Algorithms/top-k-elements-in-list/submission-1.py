class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        guide = {}
        freq = [[] for i in range(len(nums) + 1)]
        # counts and stores the value in dict
        for item in nums:
            guide[item] = 1 + guide.get(item, 0)
        # num.value : count
        # puts the value and freq by freq position
        for x, y in guide.items():
            freq[y].append(x)
        
        res = []
        for i in range(len(freq) -1 , 0, -1):
            for l in freq[i]:
                res.append(l)
                if len(res) == k:
                    return res

        


                
        