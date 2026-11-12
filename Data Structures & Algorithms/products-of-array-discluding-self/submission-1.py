class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # [1, 2, 3, 4]
        p = 1
        for x in range(len(nums)):
            result[x] = p
            p *= nums[x]
        # [1, 1, 2, 6]

        s = 1
        # s = 12
        for x in reversed(range(len(nums))):
            result[x] = s * result[x]
            s *= nums[x]
        # [24, 12, 8, 6]

        return result
            
            