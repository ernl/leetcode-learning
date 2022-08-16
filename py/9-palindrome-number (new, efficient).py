class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNumber = str(x)
        if (list(reversed(strNumber))) == list(strNumber):
            return True
        return False