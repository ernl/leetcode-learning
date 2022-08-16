# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        already_seen = set()
        ptr_linked_list = head
        previous_ptr = None
        
        while ptr_linked_list is not None:
            if ptr_linked_list.val in already_seen:
                previous_ptr.next = ptr_linked_list.next
            else:
                already_seen.add(ptr_linked_list.val)
                previous_ptr = ptr_linked_list
            ptr_linked_list = ptr_linked_list.next
        return head