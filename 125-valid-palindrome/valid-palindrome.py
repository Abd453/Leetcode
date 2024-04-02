class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''.join(c.lower() for c in s if c.isalnum())
        return k == k[::-1] or len(k) <= 1
