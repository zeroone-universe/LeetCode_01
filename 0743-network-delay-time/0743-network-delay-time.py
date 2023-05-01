class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        dist = collections.defaultdict(int)
        
        for time in times:
            graph[time[0]].append((time[1], time[2]))
        
        Q = [(0, k)]
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for end, weight in graph[node]:
                    alttime = time + weight
                    heapq.heappush(Q,(alttime, end))
        
        output = -1
        
        if len(dist.values()) == n:
            return max(dist.values())
        return -1
            