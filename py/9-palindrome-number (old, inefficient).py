import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNumber = str(x)
        i = 0
        reps = math.floor(len(strNumber)/2)
        for character in strNumber:
            if(i < reps):
                if(strNumber[i] != strNumber[len(strNumber)-1-i]):
                    return False
            i = i + 1
        return True