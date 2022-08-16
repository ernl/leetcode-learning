class Solution:
    def isValid(self, s: str) -> bool:
        str_to_list = list(s)
        stack = []

        for el in str_to_list:
          if el in {"{", "(", "["}:
            stack.append(el)
          elif el in {"}", ")", "]"} and len(stack) > 0:
            last_el = stack[-1]
            if (el == "}" and last_el == "{") or (el == ")" and last_el == "(") or (el == "]" and last_el == "["):
              stack.pop(-1)
            else:
                return False
          else:
            return False
            
        if len(stack) == 0:
            return True
        return False