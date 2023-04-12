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
        
        stack = []
        
        node = head
        
        stack.append(node.val)
        
        while node.next:
            node = node.next
            stack.append(node.val)
            
        return stack == stack[::-1]