class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            return sum(int(d) for d in str(x))
        
        for i, num in enumerate(nums):
            if digit_sum(num) == i:
                return i
        return -1