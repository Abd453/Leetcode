class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = Counter(arr1)
        ans = []
        for i in arr2:
            ans += ([i] * d[i])
        hold, s = [], set(arr2)
        for i in d:
            if i not in s:
                hold.append(i)
        hold.sort()
        for i in hold:
            ans += ([i] * d[i])
        return ans