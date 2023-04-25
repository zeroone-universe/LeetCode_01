# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = root = ListNode(0)
        queue = []
        
        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(queue, (lists[idx].val, idx, lists[idx]))
            
        
        while queue:
            node = heapq.heappop(queue)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
        
            if result.next:
                heapq.heappush(queue, (result.next.val, idx, result.next))
                
        return root.next