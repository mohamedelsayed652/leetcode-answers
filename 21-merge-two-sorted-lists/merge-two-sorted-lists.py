# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        dummy = ListNode()
        temp = dummy

        while list1  and list2:
            if list1.val <= list2.val: #if node in list1 is smaller than node in list two
                temp.next = list1
                list1 = list1.next
        
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
        temp.next = list1 or list2

        return dummy.next


