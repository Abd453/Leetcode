class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n=len(nums)
        for i in range(n):
            curr = 0
            for j in range(i,n):
                curr = math.gcd(curr,nums[j])  # You can use math.gcd or gcd. Both will work.
                if(curr == k): 
                    count += 1 
        return count