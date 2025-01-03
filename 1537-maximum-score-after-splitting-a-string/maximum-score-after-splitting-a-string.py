class Solution:
    def maxScore(self, s: str) -> int:
        total = s.count('1')
        prefix = 0
        suffix = total
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                prefix += 1
            else: 
                suffix -= 1

            max_score = max(max_score, prefix + suffix)
        
        return max_score

