class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # def digit_sum(x: int) -> int:
        #     return sum(int(d) for d in str(x))
        
        # for i, num in enumerate(nums):
        #     if digit_sum(num) == i:
        #         return i
        # return -1
        for i in range(len(nums)):
            num = nums[i]
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            if s == i:
                return i
        return -1