# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        ptr = head
        while ptr is not None:
            count += 1
            ptr = ptr.next
        
        ptr = head
        for i in range(count // 2):
            ptr = ptr.next
        
        return ptr
        