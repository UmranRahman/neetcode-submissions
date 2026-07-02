class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_indices = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen_indices:
                return [seen_indices[diff], i]
            seen_indices[nums[i]] = i