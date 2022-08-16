class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      twoSum_list = sorted(nums, reverse=True)
      pointer_top = twoSum_list[0]
      pointer_bottom = twoSum_list[-1]
      
      while 1:
        if pointer_bottom + pointer_top == target:
          index1 = -1
          index2 = -1
          for i in range(len(nums)):
            if nums[i] == pointer_top and index1 == -1:
              index1 = i
            elif nums[i] == pointer_bottom:
              index2 = i
          return [index1, index2]

        elif (pointer_bottom + pointer_top) < target:
          # Move bottom to the left
          twoSum_list.pop(-1)
          pointer_bottom = twoSum_list[-1]
        elif (pointer_bottom + pointer_top) > target:
          # Move top to the right
          twoSum_list.pop(0)
          pointer_top = twoSum_list[0]