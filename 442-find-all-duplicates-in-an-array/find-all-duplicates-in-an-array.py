class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()  # A set to track the numbers we already seen
        dupes = set()  # A set to track the numbers already seen twice
        for n in nums :  # for each number of the given list
            if n in seen :  # if we already seen this number before
                dupes.add(n)  # it is a duplicate
            else:  # if we haven't seen this number
                seen.add(n)  # add it to the seen ones
        return list(dupes)  # return a list of the duplicates numbers