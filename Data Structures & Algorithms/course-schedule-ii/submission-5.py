class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited, completed = set(), set()
        adjacency = defaultdict(list)
        for crs, pre in prerequisites:
            adjacency[crs].append(pre)

        
        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True
            visited.add(course)
            for pre in adjacency[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            completed.add(course)
            res.append(course)
            return True
            
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
