# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        rev = None
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow =slow, rev, slow.next
            
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        return not rev