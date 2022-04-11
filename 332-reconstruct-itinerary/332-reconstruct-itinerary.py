class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        def dfs(depart):
            while graph[depart]:
                dfs(graph[depart].pop(0))
            result.append(depart)
            
        dfs("JFK")
        return result[::-1]