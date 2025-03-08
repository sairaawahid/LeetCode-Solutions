# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        dummy = head
        power = 0

        while dummy:
            dummy = dummy.next
            power += 1
        
        power -= 1
        res = 0

        while head:
            res += head.val * (2**power)
            power -= 1
            head = head.next
        
        return res