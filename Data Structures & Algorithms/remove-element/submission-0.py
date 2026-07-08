class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while val in nums and i <= k:
            if val == nums[i]:
                k -= 1
                nums.remove(nums[i])
                i -= 1
            i += 1
        return k