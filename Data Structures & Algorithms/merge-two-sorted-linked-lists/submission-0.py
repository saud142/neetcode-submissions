# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        container = []
        p1 = list1
        p2 = list2

        while(p1 != None):
            container.append(p1.val)
            p1 = p1.next
    
        while(p2 != None):
            container.append(p2.val)
            p2 = p2.next     
            
        container.sort() 

        dummy = ListNode(0)
        tail = dummy

        for value in container:
            tail.next = ListNode(value)
            tail = tail.next
        return dummy.next    
            