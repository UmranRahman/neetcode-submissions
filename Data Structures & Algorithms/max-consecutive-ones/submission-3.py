class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest = 0
        count = 0
        for i in nums:
            if i == 0:
                if count > highest:
                    highest = count
                count = 0
                continue
            count += 1
        if count > highest:
            return count
        else:
            return highest