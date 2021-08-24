# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head):
        length = 0
        while(head != None):
            length += 1
            head = head.next
        return length
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        if(lenA > lenB):
            headA,headB = headB,headA
        
        for i in range(abs(lenB-lenA)):
            headB = headB.next
        
        # print(headA, headB)
        while(headA and headB and headA is not headB):
            headA = headA.next
            headB = headB.next
        
        
        return headA