class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        
        # reversed_number = 0
        # original_x = x
    
        # while x > 0:
        #     digit = x % 10
        #     reversed_number = reversed_number * 10 + digit
        #     x //= 10
        # return original_x == reversed_number
    
        if str(x)[::-1] == str(x):
            return True
        return False
        