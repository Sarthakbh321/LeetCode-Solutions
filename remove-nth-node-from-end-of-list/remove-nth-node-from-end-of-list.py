# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: 
        
        i,j = 0,1
        a = head
        b = ListNode()
        b.next = head
        og = b
        
        while(a != None):
            if(j-i > n):
                i+=1
                b = b.next
            
            j += 1
            a = a.next
        

        target = b.next
        ne = target.next
        b.next = ne
        
        return og.next