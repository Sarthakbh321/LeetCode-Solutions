# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        index = 0
        while(fast != None):
            fast = fast.next
            index += 1
            
            if(index%2 == 0):
                slow  = slow.next
                
        return slow