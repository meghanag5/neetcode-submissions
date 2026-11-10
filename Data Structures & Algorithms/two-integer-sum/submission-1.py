class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for item in range(len(nums)):
            complement = target - nums[item] 
            if complement in nums:
                complement_index = nums.index(complement)
                if complement_index != item:
                    ans.append(item)
                    ans.append(complement_index)
                    return sorted(ans)