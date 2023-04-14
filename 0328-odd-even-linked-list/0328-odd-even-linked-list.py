# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        root = head
        odd = head
        even = head.next
        even_save = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            
            even.next= even.next.next
            even = even.next
                
            
        odd.next = even_save
        
        return root
        