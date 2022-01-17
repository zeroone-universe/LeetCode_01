# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        up=0
        root=head=ListNode(0)
        while l1 or l2 or up:
            
            value=up
            if l1:
                value+=l1.val
                l1=l1.next
            if l2:
                value+=l2.val
                l2=l2.next
            
            if value>=10:
                up=1
                head.next=ListNode(value-10)
                head=head.next
            else:
                up=0
                head.next=ListNode(value)
                head=head.next
                
        return root.next
            