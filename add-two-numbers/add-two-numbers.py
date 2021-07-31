# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = l1
        
        while(l1 != None or l2 != None):        
            if(l2 == None):
                l1.val += carry
            else:
                l1.val += l2.val + carry
                
            
            carry = l1.val//10
            curr = l1.val%10
            l1.val = curr
            
            if(l1.next == None and carry > 0):
                l1.next = ListNode(0)
                        
            
            if(l2 != None):
                if(l2.next != None and l1.next == None):
                    l1.next = ListNode(0)
                l2 = l2.next
                
            l1 = l1.next
        
        
        return head
            