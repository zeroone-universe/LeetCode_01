class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        Q=[(0,k)]
        dist = collections.defaultdict(list)
        graph = collections.defaultdict(list)
        
        for start,end,time in times:
            graph[start].append([end,time])
            
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node]= time
                for end,w in graph[node]:
                    alttime = w + time
                    heapq.heappush(Q, (alttime, end))
            
        if len(dist) == n:
            return max(dist.values())
        
        return -1