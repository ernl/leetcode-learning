# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1_index = 0
        v1_aux = l1
        value1 = 0
        while v1_aux:
            value1 = value1 + v1_aux.val*(10**v1_index)
            v1_aux = v1_aux.next
            v1_index = v1_index + 1
        
        v2_index = 0
        v2_aux = l2
        value2 = 0
        while v2_aux:
            value2 = value2 + v2_aux.val*(10**v2_index)
            v2_aux = v2_aux.next
            v2_index = v2_index + 1
        addV1V2 = value1 + value2
        numbers = str(addV1V2)
        addList = []
        for char in numbers:
            addList.append(int(char))
        l3 = ListNode(addList.pop())
        l3_aux = l3
        while (addList != []):
            l3_aux.next = ListNode(addList.pop())
            l3_aux = l3_aux.next
        return l3
