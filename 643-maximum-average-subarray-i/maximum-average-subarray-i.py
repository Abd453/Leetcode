class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        max_av = 0

        for i in range(k):
            current_sum += nums[i]
        max_av = current_sum / k
        
        for i in range(k, len(nums)):
            #max_av =  current_sum / k
            current_sum += nums[i] - nums[i-k]
            max_av = max(max_av, current_sum/k)
        return max_av
        