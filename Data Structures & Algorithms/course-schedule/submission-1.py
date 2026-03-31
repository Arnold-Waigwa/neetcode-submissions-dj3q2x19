class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        create an adjacency list graph using a hashmap
        crs: [prerequesites]

        """
        adjacency = defaultdict(list)
        visited, completed = set(), set()
        for crs, pre in prerequisites:
            adjacency[crs].append(pre)
        
        #detect the cycle using dfs
        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True
            visited.add(course)
            for pre in adjacency[course]:
                if not dfs(pre):
                    return False

            completed.add(course)
            visited.remove(course)
            adjacency[course] = []
            return True
            


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 

        

