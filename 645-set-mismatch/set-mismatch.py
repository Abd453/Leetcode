class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep,mis = None,None
        N = len(nums)
        sumAct = sum(nums)
        sumExp = sum([i for i in range(1, N+1)])
        prodExp = reduce(mul, [i for i in range(1, N+1)])
        prodAct = reduce(mul,nums)
        mis = round((sumAct- sumExp)/ ((prodAct/prodExp)-1))
        rep = (sumAct - sumExp)+mis

        return [rep, mis]