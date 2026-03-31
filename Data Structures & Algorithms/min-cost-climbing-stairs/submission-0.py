class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #lets first do backtracking to untangle
        min_cost = float("inf")
        def dfs(i, amt):
            nonlocal min_cost
            if i >= len(cost):
                min_cost = min(min_cost, amt)
                return
            
            dfs(i + 1, amt + cost[i])
            dfs(i + 2, amt + cost[i])
        for i in range(2):
            dfs(i, 0)
        return min_cost
                
