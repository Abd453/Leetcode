class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
             return False
        # return Counter(s) == Counter(t)
        count = [0]*26

        for char in s:
            count[ord(char)-ord('a')]+=1

        for char in t:
            count[ord(char)-ord('a')]-=1
        return all(x == 0 for x in count)

        