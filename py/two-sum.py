class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        for number in nums:
            j = 0
            for number2 in nums:
                if(number + number2)  == target and (i != j):
                    return [i,j]
                j = j +1
            i = i +1