class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * 26
        
        for c in s:
            freq[ord(c) - ord('a')] += 1
    
        for c in t:
            freq[ord(c) - ord('a')] -= 1
        steps = 0
        
        for x in freq:
            if x > 0:
                steps += x
        
        return steps
        