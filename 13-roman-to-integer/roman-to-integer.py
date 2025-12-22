class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1,'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        result = 0
        for key, value in enumerate(s):
            if key + 1 < len(s) and dic[value] < dic[s[key+1]]:
                result -= dic[value]
            else:
                result += dic[value]
        return result
        
       