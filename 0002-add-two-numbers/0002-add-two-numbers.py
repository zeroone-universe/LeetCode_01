# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = head = ListNode(0)
        idx = 0
        up = 0
        
        num = 0
        while l1 or l2 or up:
            num =0
            if l1:
                num += l1.val
                l1=l1.next
            if l2:
                num+= l2.val
                l2 = l2.next
            if up:
                num+= up
                up = 0
            up, num = divmod(num, 10)
            
            node = ListNode(num)
            root.next = node
            root = root.next
        
        return head.next
            
                
                
            