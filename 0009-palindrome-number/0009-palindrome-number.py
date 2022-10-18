class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x >0 and x%10 == 0 ):
            return False
        result = 0
        while(result < x):
            result = result *10 + x %10
            x = x//10
        return True if (result == x or x == result//10) else False