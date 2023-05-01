class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        
        graph = collections.defaultdict(list)
        
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
        
        visited = set()
        checked = set()
        
        def dfs(v):
            if v in visited:
                return False
            
            if v not in checked:
                visited.add(v)
                for w in graph[v]:
                    if not dfs(w):
                        return False
                visited.remove(v)
                
                checked.add(v)
                
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True