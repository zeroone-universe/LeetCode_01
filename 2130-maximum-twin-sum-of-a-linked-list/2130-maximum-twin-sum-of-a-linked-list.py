# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        first_half = []
        
        max_sum = 0
        
        fast = head
        
        while fast:
            first_half.append(head.val)
            head = head.next
            fast = fast.next.next
        
        first_half = first_half[::-1]
        
        for val in first_half:
            max_sum = max(max_sum, head.val + val)
            head = head.next
            
        return max_sum
            