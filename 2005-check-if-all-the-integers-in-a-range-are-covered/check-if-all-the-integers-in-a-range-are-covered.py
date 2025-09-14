class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        
        for start, end in ranges:
            diff[start] += 1
            diff[end + 1] -= 1
        
        covered = 0
        for i in range(1, 51):
            covered += diff[i]
            if left <= i <= right and covered <= 0:
                return False
        
        return True
