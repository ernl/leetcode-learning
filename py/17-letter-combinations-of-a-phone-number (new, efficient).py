class Solution(object):
    def letterCombinations(self, digits):
        mapping = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
        output = []
        
        def backtrack(i, string):
            if len(string) == len(digits):
                
                output.append(string)
                return
            for char in mapping[digits[i]]:
                backtrack(i+1, string+char)
        if len(digits) > 0:
            backtrack(0,"")
        return output
