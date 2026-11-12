class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        
        suffix = [1] * len(nums)
        result = [1] * len(nums)
        #regular prefix product
        s = 1
        for c in range(0, len(nums)):
            s *= nums[c]
            prefix.append(s)
        n = 1
        for c in reversed(range(len(nums))):
            n *= nums[c]
            suffix[c] = n
        for x in range(0, len(nums)):
            if x == 0:
                result[x] = suffix[x + 1]
            elif x == len(nums) - 1:
                result[x] = prefix[x - 1]
            else:
                result[x] = prefix[x - 1] * suffix[x + 1]

        return result
            