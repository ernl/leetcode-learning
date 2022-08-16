class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = []
        space = False
        for char in s:
            if char != " " and not space:
                temp.append(char)
            elif char != " ":
                temp = []
                temp.append(char)
                space = False
            else:
                space = True
        return len(temp)