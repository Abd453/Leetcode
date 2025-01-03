class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        Sum = sum(nums)
        current_sum = 0
        answer = 0

        for i in range(len(nums)-1):
            current_sum += nums[i]
            if current_sum >= Sum - current_sum:
                answer += 1
        return answer
        