class Solution:
    def myAtoi(self, s: str) -> int:
        int_result = 0
        stack = []
        sign = "N/A"
        for char in s:
            stack_len = len(stack)
            if char == "." or (char == " " and (stack_len or sign != "N/A")):
                break
            elif sign == "N/A" and not stack_len and char in {"+","-"}:
                sign = char
            elif char in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                stack.append(int(char))
            elif char != " ":
                break
        
        for i in range(len(stack)):
            int_result += stack.pop() * 10**(i)
        if sign == "-":
            int_result = -int_result

        if int_result < -pow(2,31):
            int_result = -pow(2,31)
        elif int_result > pow(2,31) - 1:
            int_result = pow(2,31) - 1
        return int_result