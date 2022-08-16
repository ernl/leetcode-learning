class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        lenList = len(digits) - 1
        for index, number in enumerate(digits):
            res += number * 10**(lenList - index)
        res += 1
        res_list = []
        for char in str(res):
            res_list.append(char)
        return res_list