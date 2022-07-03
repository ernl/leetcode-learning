class Solution(object):
    def letterCombinations(self, digits):
        mapping = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        output = []
        if len(digits) >= 1:
            for char1 in mapping[int(digits[0])-2]:
                if len(digits) >= 2:
                    for char2 in mapping[int(digits[1])-2]:
                        if len(digits) >= 3:
                            for char3 in mapping[int(digits[2])-2]:
                                if len(digits) >= 4:
                                    for char4 in mapping[int(digits[3])-2]:
                                        output.append(char1+char2+char3+char4)
                                else:
                                    output.append(char1+char2+char3)
                        else:
                            output.append(char1+char2)
                else:
                    output.append(char1)
        return output
