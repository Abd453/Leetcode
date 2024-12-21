class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        preSum = 0
        result = []
        for i in range(len(nums)):
            preSum += nums[i]
            result.append(preSum)
        return result